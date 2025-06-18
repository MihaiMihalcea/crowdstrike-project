# score_opportunities.py

import os
import time
import math
import json
import re
import pandas as pd
from dotenv import load_dotenv
from openai_client import chat_completion
from tqdm import tqdm
from prompt import PROMPT_SYSTEM, PROMPT_TEMPLATE

# ─── CONFIG ──────────────────────────────────────────────────────────────────
load_dotenv()  # loads OPENAI_API_KEY and OPENAI_MODEL from .env

class Scorer:
    def __init__(self, input_file=None, output_file=None, model_name=None, temperature=0.3):
        self.input_file   = input_file  or os.getenv("SCORE_INPUT_FILE",  "synthetic_opportunities.csv")
        self.output_file  = output_file or os.getenv("SCORE_OUTPUT_FILE", "scored_opportunities.csv")
        self.model_name   = model_name  or os.getenv("OPENAI_MODEL",       "gpt-3.5-turbo")
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
        Try json.loads; if it fails, extract first {...} block and retry.
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
        opp = self.sanitize_opportunity(opportunity)
        # 2. Build and send prompt
        user_content = PROMPT_TEMPLATE % json.dumps(opp, indent=2)
        messages = [
            {"role": "system", "content": PROMPT_SYSTEM},
            {"role": "user",   "content": user_content}
        ]
        start = time.time()
        try:
            resp = chat_completion(messages=messages, model=self.model_name, temperature=self.temperature)
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
        df      = pd.read_csv(self.input_file)
        records = df.to_dict(orient="records")
        results = []
        for opp in tqdm(records, desc="Scoring opportunities", unit="opp"):
            results.append(self.score_opportunity(opp))
        pd.DataFrame(results).to_csv(self.output_file, index=False)
        print(f"Saved {len(results)} scored opportunities to '{self.output_file}'")

# scorer.py

def main():
    """CLI entry-point for scoring."""
    Scorer().run()
