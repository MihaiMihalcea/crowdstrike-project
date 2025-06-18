from constants import public_companies, stages, lead_sources
from opportunity_themes_data import opportunity_themes
from faker import Faker
import random

fake = Faker()

# Your generate_opportunity() here

assert len(public_companies) == len(opportunity_themes)

def generate_opportunity(index: int, include_meddpicc: bool) -> dict:
    """
    Create one synthetic opportunity record.

    Args:
      index: index into public_companies & opportunity_themes lists.
      include_meddpicc: whether to populate MEDDPICC fields.

    Returns:
      A dict mapping CSV column names to values.
    """
    company = public_companies[index]  # one opportunity per company
    opportunity_data = {
        "Opportunity ID": f"OPP-{1000 + index}",
        "Account Name": company,
        "Stage": stages[0],
        "Close Date": fake.date_between(start_date="+30d", end_date="+120d"),
        "Amount": f"${random.randint(100000, 2500000)}",
        "Owner": fake.name(),
        "Created Date": fake.date_between(start_date="-30d", end_date="today"),
        "Lead Source": random.choice(lead_sources),
    }

    # 50% chance to include MEDDPICC and theme-aligned data
    if include_meddpicc:
        theme = opportunity_themes[index]  # now used below
        opportunity_data.update({
            "Opportunity Name": f"{company} - {theme.theme}",
            "Metrics": theme.metrics,
            "Decision Criteria": theme.decision_criteria,
            "Decision Process": theme.decision_process,
            "Identify Pain": theme.identify_pain,
            "Opportunity Type": theme.opportunity_type,
            "Paper Process": theme.paper_process,
            "Competition": theme.competition,
            "Category": theme.category,
            "Notes": (
                f"Why: {theme.notes['why']} "
                f"Why Now: {theme.notes['why_now']} "
                f"Why This Product: {theme.notes['why_this_product']}"
            ),
            "Economic Buyer": fake.name(),
            "Champion": fake.name()
        })
    else:
        # Fill MEDDPICC and theme-aligned fields with None
        for field in [
            "Opportunity Name", "Metrics", "Decision Criteria", "Decision Process",
            "Identify Pain", "Opportunity Type", "Paper Process", "Competition",
            "Category", "Notes", "Economic Buyer", "Champion"
        ]:
            opportunity_data[field] = None

    return opportunity_data