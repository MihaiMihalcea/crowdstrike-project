import os
import csv
import time
import math
import json
import re
import pandas as pd
from dotenv import load_dotenv
from openai_client import chat_completion
from tqdm import tqdm
from prompt import PROMPT_SYSTEM, PROMPT_TEMPLATE

# ─── CONFIG ────────────────────────────────────────────────────
load_dotenv()  # loads OPENAI_API_KEY and OPENAI_MODEL from .env

class Scorer:
    """
    Encapsulates the scoring pipeline:
      - read CSV
      - sanitize each record
      - send prompt to OpenAI
      - parse and enrich response
      - write scored data to CSV
    """
    def __init__(self,
                 input_file: str,
                 output_file: str,
                 model_name: str | None = None,
                 temperature: float = 0.3):
        """
        Initialize pipeline.

        Args:
        input_file:  path to the synthetic opportunities CSV.
        output_file: path to write the scored CSV.
        model_name:  API model to use (falls back to OPENAI_MODEL env var).
        temperature: sampling temperature for the model.
        """
        self.input_file   = input_file
        self.output_file  = output_file
        # pick up ENV var if not explicitly given:
        self.model_name = (
                model_name
                or os.getenv("OPENAI_MODEL")
                or "gpt-3.5-turbo"
                )
        self.temperature  = temperature
    @staticmethod
    def sanitize_opportunity(opportunity: dict) -> dict:
        """Convert NaN/Timestamps to safe JSON values."""
        clean = {}
        for k, v in opportunity.items():
            if hasattr(v, "isoformat"):  # datetime or Timestamp
                clean[k] = v.isoformat()
            elif isinstance(v, float) and math.isnan(v):
                clean[k] = ""
            else:
                clean[k] = v
        return clean
    @staticmethod
    def parse_json_with_fallback(text: str, opp_name: str) -> dict:
        """
        Try json.loads; if it fails, extract first entry block and retry.
        Logs unparseable cases.
        """
        try:
            return json.loads(text)
        except json.JSONDecodeError:
            # Attempt to pluck the first JSON object
            m = re.search(r"\{.*}", text, flags=re.DOTALL)
            if m:
                try:
                    return json.loads(m.group(0))
                except json.JSONDecodeError:
                    pass
            # Logging for inspection
            print(f"\n🛑 Failed to parse JSON for opportunity: {opp_name}")
            print("Raw output was:\n", repr(text), "\n")
            # Return minimal error structure
            return {
                "task_summary":     "parse_error",
                "opportunity_name": opp_name,
                "score":            0,
                "explanation":      "Could not parse model output as JSON.",
                "risk_score":       7,
                "risk_level":       "red"
            }

    def score_opportunity(self, opportunity: dict) -> dict:
        """Score a single opportunity, timing the call and handling errors."""
        opp = self.sanitize_opportunity(opportunity)
        user_content = PROMPT_TEMPLATE % json.dumps(opp, indent=2)
        messages = [
            {"role": "system", "content": PROMPT_SYSTEM},
            {"role": "user",   "content": user_content}
        ]
        start = time.time()
        try:
            resp = chat_completion(messages=messages, temperature=self.temperature)
            end = time.time()
            raw = resp.choices[0].message.content.strip()
            data = self.parse_json_with_fallback(raw, opp.get("Opportunity Name", "Unknown"))
            # Enforce the fixed task_summary if you wish:
            # data["task_summary"] = "Evaluate deal qualification and risk using MEDDPICC framework."
            # Fill in metadata
            data["processing_time"] = round(end - start, 3)
            data["tokens_used"]     = getattr(resp.usage, "total_tokens", 0)
            data["model"]           = self.model_name
            data["status"]          = data.get("status", "success")
        except Exception as e:
            end = time.time()
            data = {
                "task_summary":     "error",
                "opportunity_name": opp.get("Opportunity Name", ""),
                "score":            0,
                "explanation":      f"Error during scoring: {e}",
                "risk_score":       7,
                "risk_level":       "red",
                "processing_time":  round(end - start, 3),
                "tokens_used":      0,
                "model":            self.model_name,
                "status":           "error"
            }
        return data

    def run(self):
        """Run the full pipeline with a tqdm progress bar."""
        df      = pd.read_csv(self.input_file)
        records = df.to_dict(orient="records")
        results = [self.score_opportunity(opp) for opp in tqdm(records, desc="Scoring opportunities")]

        # build DataFrame & clean
        cleaned = pd.DataFrame(results)
        cleaned = cleaned.fillna("")  # no NaNs or None

        # enforce column order
        cols = [
            "task_summary", "opportunity_name", "score",
            "risk_score", "risk_level", "processing_time",
            "tokens_used", "model", "status", "explanation"
        ]

        # validation: all required columns present
        missing = set(cols) - set(cleaned.columns)
        assert not missing, f"Missing columns in scored output: {missing}"

        # validation: non-empty DataFrame
        assert len(cleaned) > 0, "Scoring produced an empty result set"

        cleaned = cleaned[cols]

        # save with clean CSV settings
        cleaned.to_csv(
            self.output_file,
            index=False,
            encoding="utf-8-sig",
            quoting=csv.QUOTE_MINIMAL,
            lineterminator="\n"
        )
        print(f"Saved {len(cleaned)} scored opportunities to '{self.output_file}'")

def main():
    """CLI entry-point for scoring."""
    Scorer().run()
