from dataclasses import dataclass

@dataclass
class OpportunityTheme:
    """
    Encapsulates a single MEDDPICC-themed opportunity.
    Fields map directly to CSV columns and JSON schema.
    """
    theme: str
    metrics: str
    decision_criteria: str
    decision_process: str
    identify_pain: str
    notes: dict
    opportunity_type: str
    paper_process: str
    competition: str
    category: str

    def to_meddpicc_dict(self):
     """
     Return just the MEDDPICC-related fields as a dict suitable for CSV insertion.
     """
     return {
        "Metrics": self.metrics,
        "Decision Criteria": self.decision_criteria,
        "Decision Process": self.decision_process,
        "Identify Pain": self.identify_pain,
        "Notes": f"Why: {self.notes['why']} Why Now: {self.notes['why_now']} Why This Product: {self.notes['why_this_product']}"
    }