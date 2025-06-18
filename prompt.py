# Single source of truth for all prompts.

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
"""  # Data will be formated in a dictionary.