from constants import public_companies, stages, lead_sources
from opportunity_themes_data import opportunity_themes
from faker import Faker
import random

fake = Faker()

# Your generate_opportunity() here

assert len(public_companies) == len(opportunity_themes)

def generate_opportunity(index):
    company = public_companies[index]  # one opportunity per company
    opportunity_data = {
        "Opportunity ID": f"OPP-{1000 + index}",
        "Account Name": company,
        "Stage": stages[0],
        "Close Date": fake.date_between(start_date="+30d", end_date="+120d"),
        "Amount": round(random.uniform(10000, 250000), 2),
        "Owner": fake.name(),
        "Created Date": fake.date_between(start_date="-30d", end_date="today"),
        "Lead Source": random.choice(lead_sources),
    }

    # 50% chance to include MEDDPICC and theme-aligned data
    if random.random() < 0.5:
        theme = opportunity_themes[index]  # one-to-one mapping with company
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

if __name__ == "__main__":
    for i in range(len(public_companies)):  # assuming 50 companies
        opportunity = generate_opportunity(i)
        print(f"\nOpportunity {i+1}:")
        for key, value in opportunity.items():
            print(f"{key}: {value}")

