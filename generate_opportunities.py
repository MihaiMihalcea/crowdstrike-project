import pandas as pd
import random
import numpy as np
from faker import Faker

fake = Faker()

public_companies = [
    "Microsoft", "Apple", "Amazon", "Alphabet", "Meta",
    "NVIDIA", "Salesforce", "Adobe", "Netflix", "Tesla",
    "Oracle", "IBM", "Intel", "Cisco", "Qualcomm",
    "Uber", "Airbnb", "Zoom", "Snowflake", "Palantir"
]

stages = ["Stage 1 - Discovery"]
lead_sources = ["Web", "Partner", "Event", "Referral", "Outbound", "Inbound"]
opportunity_types = ["New Business", "Upsell", "Renewal"]


def generate_opportunity(index):
    company = random.choice(public_companies)
    opportunity = {
        "Opportunity ID": f"OPP-{1000 + index}",
        "Opportunity Name": f"{company} - Opportunity {index + 1}",
        "Account Name": company,
        "Stage": stages[0],
        "Close Date": fake.date_between(start_date="+30d", end_date="+120d"),
        "Amount": round(random.uniform(10000, 250000), 2),
        "Owner": fake.name(),
        "Created Date": fake.date_between(start_date="-30d", end_date="today"),
        "Opportunity Type": random.choice(opportunity_types),
        "Lead Source": random.choice(lead_sources),
        "Notes": generate_notes()
    }

    # Randomly decide whether to include MEDDPICC
    if random.random() < 0.5:
        opportunity.update(generate_meddpicc_fields())
    else:
        opportunity.update({field: None for field in medd_fields})

    return opportunity

def generate_notes():
    why = fake.sentence(nb_words=8)
    why_now = fake.sentence(nb_words=6)
    why_this_product = fake.sentence(nb_words=7)
    return f"Why: {why} | Why Now: {why_now} | Why This Product: {why_this_product}"

medd_fields = [
    "Metrics", "Economic Buyer", "Decision Criteria", "Decision Process",
    "Paper Process", "Identify Pain", "Champion", "Competition"
]

def generate_meddpicc_fields():
    return {
        "Metrics": fake.sentence(nb_words=6),
        "Economic Buyer": fake.name(),
        "Decision Criteria": fake.sentence(nb_words=5),
        "Decision Process": fake.sentence(nb_words=6),
        "Paper Process": fake.sentence(nb_words=4),
        "Identify Pain": fake.sentence(nb_words=5),
        "Champion": fake.name(),
        "Competition": random.choice(public_companies)
    }

opportunities = [generate_opportunity(i) for i in range(50)]
df = pd.DataFrame(opportunities)

df.to_csv("synthetic_opportunities.csv", index=False)
print("CSV file saved!")
