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
#from datetime import date

# ─── CONFIG ──────────────────────────────────────────────────────────────────
load_dotenv()  # loads OPENAI_API_KEY and OPENAI_MODEL from .env

INPUT_FILE   = "synthetic_opportunities.csv"
OUTPUT_FILE  = "scored_opportunities.csv"
MODEL_NAME   = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")

# ─── PROMPT ──────────────────────────────────────────────────────────────────
PROMPT_SYSTEM = "You are a helpful assistant."

PROMPT_TEMPLATE = """
You are a senior B2B sales strategist who specialises in enterprise deal-qualification
frameworks such as MEDDPICC.

1) Deal Score (0–100), normalized from raw 115 points:
  • Metrics are specific & measurable: +15  
  • Pain is urgent/critical: +15  
  • Champion identified & credible: +15  
  • Economic Buyer named: +10  
  • Decision Process described: +10  
  • Decision Criteria provided: +10  
  • Paper Process underway: +10  
  • Competition mentioned: +5  
  • Stage beyond Discovery: +10  
  • Close date < 60 days: +5  
  • Notes show urgency/momentum: +10  

2) Risk Score (0–7), +1 for each triggered:
  • Champion is missing  
  • Economic Buyer is missing  
  • Stage beyond Discovery AND no Paper Process  
  • Both Metrics and Pain missing  
  • Stage = Discovery AND Created Date > 45 days ago  
  • Close Date in past OR > 6 months out  
  • Notes lack urgency/executive signals  

3) Risk Level mapping:
  0–1 → "green"  
  2–3 → "yellow"  
  4–7 → "red"  

4) Explanation (25–40 words, strategist tone) must:
  • Weave together MEDDPICC elements + Notes  
  • End with a risk insight sentence, e.g.:  
    “Overall risk is low.”  
    “Moderate risk due to missing buyer access.”  
    “High risk: deal lacks urgency and key buying signals.”  

**Respond with ONLY this JSON schema** (no wrappers, no markdown):

{
  "task_summary":     string,
  "opportunity_name": string,
  "score":            integer,
  "explanation":      string,
  "risk_score":       integer,
  "risk_level":       string,
  "processing_time":  float,
  "tokens_used":      integer,
  "model":            string,
  "status":           string
}

Here is the data:
%s
"""  # we’ll format in a dict and the model name

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

def parse_json_with_fallback(text: str, opp_name: str) -> dict:
    """
    Try json.loads; if it fails, extract first {...} block and retry.
    Logs unparseable cases.
    """
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        # Attempt to pluck the first JSON object
        m = re.search(r'\{.*\}', text, flags=re.DOTALL)
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

# ─── SCORING LOGIC ────────────────────────────────────────────────────────────
def score_opportunity(opportunity: dict, model_name: str) -> dict:
    """
    Calls the model, parses JSON robustly, and fills defaults.
    Returns a dict ready to append to your results list.
    """
    # 1. Sanitize any NaNs or dates
    opp = sanitize_opportunity(opportunity)
    # 2. Build and send prompt
    user_content = PROMPT_TEMPLATE % json.dumps(opp, indent=2)
    messages = [
        {"role": "system", "content": PROMPT_SYSTEM},
        {"role": "user",   "content": user_content}
    ]
    start = time.time()
    try:
        resp = chat_completion(messages=messages, temperature=0.3)
        end = time.time()
        raw = resp.choices[0].message.content.strip()
        data = parse_json_with_fallback(raw, opp.get("Opportunity Name", "Unknown"))
        # Enforce the fixed task_summary if you wish:
        # data["task_summary"] = "Evaluate deal qualification and risk using MEDDPICC framework."
        # Fill in metadata
        data["processing_time"] = round(end - start, 3)
        data["tokens_used"]     = getattr(resp.usage, "total_tokens", 0)
        data["model"]           = model_name
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
            "model":            model_name,
            "status":           "error"
        }
    return data

# ─── MAIN ENTRY POINT ────────────────────────────────────────────────────────
def main():
    # load your opportunities
    df = pd.read_csv(INPUT_FILE)
    results = []

    # convert to list of dicts so tqdm knows the total
    records = [sanitize_opportunity(r) for _, r in df.iterrows()]
    # wrap with tqdm to display a progress bar
    for opp_dict in tqdm(records, desc="Scoring opportunities", unit="opp"):
        result = score_opportunity(opp_dict, MODEL_NAME)
    results.append(result)

    # save to CSV
    pd.DataFrame(results).to_csv(OUTPUT_FILE, index=False)
    print(f"Saved {len(results)} scored opportunities to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
