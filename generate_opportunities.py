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

medd_fields = [
    "Metrics", "Economic Buyer", "Decision Criteria", "Decision Process",
    "Paper Process", "Identify Pain", "Champion", "Competition"
]

cost_types = ["operational costs", "cloud infrastructure spend", "customer acquisition cost"]
metric_names = ["customer retention", "sales pipeline velocity", "NPS score", "revenue per employee"]
percentages = ["10%", "25%", "40%", "50%"]
timeframes = ["quarter", "6 months", "fiscal year"]
amounts = ["$100K", "$250K", "$1M"]
business_reasons = ["poor churn rates", "recent funding", "executive mandate", "competitive pressure"]

def generate_realistic_metric():
    template = random.choice(metrics_templates)
    return template.format(
        cost_type=random.choice(cost_types),
        percentage=random.choice(percentages),
        timeframe=random.choice(timeframes),
        amount=random.choice(amounts),
        metric_name=random.choice(metric_names),
        business_reason=random.choice(business_reasons)
    )

class OpportunityTheme:
    def __init__(self, theme, metric, decision_criteria, decision_process, identify_pain, notes):
        self.theme = theme
        self.metric = metric
        self.decision_criteria = decision_criteria
        self.decision_process = decision_process
        self.identify_pain = identify_pain
        self.notes = notes  # Dictionary with keys: why, why_now, why_this_product

    def to_meddpicc_dict(self):
        return {
            "Metrics": self.metric,
            "Decision Criteria": self.decision_criteria,
            "Decision Process": self.decision_process,
            "Identify Pain": self.identify_pain,
            "Notes": f"Why: {self.notes['why']} Why Now: {self.notes['why_now']} Why This Product: {self.notes['why_this_product']}"
        }

themes = [
    OpportunityTheme(
        theme="Reduce onboarding churn",
        metric="Reduce onboarding churn rate from 15% to 5%.",
        decision_criteria="Requires detailed onboarding analytics and personalized onboarding journeys.",
        decision_process="Evaluating 2 vendors with pilot testing. Decision expected in Q3.",
        identify_pain="High churn in the first 14 days due to unclear value delivery and poor UX.",
        notes={
            "why": "Onboarding drop-off is the #1 reason users leave.",
            "why_now": "CS leadership just tied their bonus to reducing churn.",
            "why_this_product": "Our platform provides deep onboarding analytics and guided flows."
        }
    ),
    OpportunityTheme(
        theme="Consolidate tech stack",
        metric="Reduce SaaS tooling spend by 25% this fiscal year.",
        decision_criteria="Needs a solution that combines analytics, engagement, and CRM integrations.",
        decision_process="Procurement-led RFP with 4 stakeholders. Decision in next 60 days.",
        identify_pain="Overlapping tools with redundant functionality causing inefficiencies.",
        notes={
            "why": "Tool sprawl is causing reporting headaches and increased costs.",
            "why_now": "CFO has frozen new tool purchases until consolidations happen.",
            "why_this_product": "We unify multiple functions with one integrated platform."
        }
    ),
    OpportunityTheme(
        theme="Expand into new market segment",
        metric="Increase revenue from SMBs by 40% in the next two quarters.",
        decision_criteria="Needs scalable onboarding, self-service setup, and chat-based support.",
        decision_process="Pilot program approved for 3 vendors. Decision by end of Q2.",
        identify_pain="Current platform is optimized for enterprise, not SMB self-service flows.",
        notes={
            "why": "They want to diversify revenue and reduce dependence on enterprise clients.",
            "why_now": "New CRO is pushing hard into the SMB space.",
            "why_this_product": "Our solution supports rapid deployment and SMB-tailored onboarding."
        }
    ),
    OpportunityTheme(
        theme="Improve forecasting accuracy",
        metric="Achieve >90% forecast accuracy by end of fiscal year.",
        decision_criteria="Must integrate with SFDC, support AI-driven insights, and customizable dashboards.",
        decision_process="RevOps and Sales Ops will lead a joint vendor evaluation.",
        identify_pain="Inconsistent data and manual reporting are eroding trust in forecasts.",
        notes={
            "why": "Leadership can't rely on current forecast data to plan resources.",
            "why_now": "Board flagged forecast inaccuracy as a key risk during last review.",
            "why_this_product": "We bring real-time pipeline health scoring and automated rollups."
        }
    ),
    OpportunityTheme(
        theme="Shorten sales cycle",
        metric="Reduce average sales cycle from 90 to 60 days.",
        decision_criteria="Needs better qualification tools and automation during discovery.",
        decision_process="Sales enablement team is testing various tools in parallel.",
        identify_pain="Deals stall early due to lack of standardized qualification.",
        notes={
            "why": "Speed to close directly impacts their cash flow and quota coverage.",
            "why_now": "Sales VP was just tasked with increasing velocity across regions.",
            "why_this_product": "We embed structured discovery flows that integrate into CRM."
        }
    ),
    OpportunityTheme(
        theme="Prepare for IPO compliance",
        metric="Achieve SOX compliance readiness by end of year.",
        decision_criteria="Must include audit trail, access controls, and automated documentation.",
        decision_process="Led by Finance and Legal. Budget approved already.",
        identify_pain="Their current process is mostly manual and lacks auditability.",
        notes={
            "why": "Compliance is non-negotiable as part of their IPO plan.",
            "why_now": "They're starting audit dry runs this quarter.",
            "why_this_product": "Our solution is used by 100+ pre-IPO companies for SOX prep."
        }
    ),
    OpportunityTheme(
        theme="Increase NPS",
        metric="Improve NPS from 42 to 60 by year-end.",
        decision_criteria="Looking for proactive engagement workflows and CS analytics.",
        decision_process="CS team owns this, reporting to COO weekly.",
        identify_pain="They react to churn but struggle to act on early signals.",
        notes={
            "why": "Retention is starting to slip due to customer experience issues.",
            "why_now": "They just lost a major client due to slow CS response.",
            "why_this_product": "We help CS identify risks earlier and take automated action."
        }
    ),
    OpportunityTheme(
        theme="Reduce support ticket volume",
        metric="Cut Tier 1 tickets by 30% through self-service and automation.",
        decision_criteria="Needs searchable help center, chatbots, and analytics.",
        decision_process="Support and Product teams evaluating in tandem.",
        identify_pain="Support is overwhelmed and response times are slipping.",
        notes={
            "why": "High ticket volume is driving down satisfaction and increasing costs.",
            "why_now": "New VP of Support is focusing on operational efficiency.",
            "why_this_product": "We automate Tier 1 requests and provide deflection analytics."
        }
    ),
    OpportunityTheme(
        theme="Boost upsell conversion",
        metric="Grow upsell revenue by 20% this quarter.",
        decision_criteria="Requires lifecycle marketing tools and usage-based triggers.",
        decision_process="Marketing and CS are co-owning a 3-month pilot.",
        identify_pain="Sales lacks insight into expansion-ready accounts.",
        notes={
            "why": "Expansion revenue is underperforming versus plan.",
            "why_now": "They just rolled out usage-based pricing and need tooling.",
            "why_this_product": "We provide in-app targeting and upsell triggers based on usage."
        }
    ),
    OpportunityTheme(
        theme="Centralize analytics stack",
        metric="Unify reporting across departments with a single BI tool.",
        decision_criteria="Must integrate with Snowflake, Redshift, and GA4.",
        decision_process="Data Engineering owns the RFP, involving 5 departments.",
        identify_pain="Teams use disconnected tools and can't agree on KPIs.",
        notes={
            "why": "Conflicting metrics are slowing down decisions.",
            "why_now": "Their CEO mandated a single source of truth by Q3.",
            "why_this_product": "We connect to all major data sources and enforce metric governance."
        }
    ),
    OpportunityTheme(
        theme="Automate manual finance tasks",
        metric="Save 500+ hours per year in manual reconciliation and reporting.",
        decision_criteria="Requires GL sync, approval workflows, and audit tracking.",
        decision_process="Finance ops running side-by-side trial with 2 vendors.",
        identify_pain="Their current process involves dozens of spreadsheets and errors.",
        notes={
            "why": "They can't close books on time or explain variances quickly.",
            "why_now": "They failed their last internal audit on process documentation.",
            "why_this_product": "Our platform automates reconciliation and reporting with audit compliance."
        }
    ),
    OpportunityTheme(
        theme="Modernize legacy systems",
        metric="Decommission 3 legacy platforms by end of year.",
        decision_criteria="Cloud-native, secure, scalable, and proven with large orgs.",
        decision_process="IT and Ops teams are mapping out migration paths.",
        identify_pain="Legacy tools are expensive to maintain and lack integrations.",
        notes={
            "why": "Tech debt is slowing innovation and causing outages.",
            "why_now": "Recent outage triggered executive-level mandate.",
            "why_this_product": "We’ve replaced legacy systems at 50+ F500 firms."
        }
    ),
    OpportunityTheme(
        theme="Improve demo-to-close rate",
        metric="Increase conversion from 25% to 40% in Q3.",
        decision_criteria="Needs better qualification, personalization, and follow-up.",
        decision_process="Sales enablement testing new playbooks and tooling.",
        identify_pain="Demos are generic and not aligned with customer goals.",
        notes={
            "why": "They spend too much time on low-likelihood deals.",
            "why_now": "New Head of Enablement wants to enforce sales process rigor.",
            "why_this_product": "We embed qualification workflows and tailored demo prep."
        }
    ),
    OpportunityTheme(
        theme="Reduce employee turnover",
        metric="Improve retention from 78% to 90% by year-end.",
        decision_criteria="Needs engagement analytics and pulse survey automation.",
        decision_process="HR is leading pilot with input from People Ops.",
        identify_pain="Attrition is high among new hires and top performers.",
        notes={
            "why": "Losing talent is impacting morale and project delivery.",
            "why_now": "Just missed hiring goals due to burnout and churn.",
            "why_this_product": "We surface early disengagement signals and automate check-ins."
        }
    ),
    OpportunityTheme(
        theme="Enable data privacy compliance",
        metric="Achieve GDPR + CCPA compliance audit pass by Q4.",
        decision_criteria="Supports user consent, access logs, and export requests.",
        decision_process="Led by Legal and Security with IT support.",
        identify_pain="No centralized system for handling user data rights.",
        notes={
            "why": "Non-compliance risks legal and reputational fallout.",
            "why_now": "They’re expanding into Europe and California.",
            "why_this_product": "We automate consent flows and DSR management."
        }
    ),
    OpportunityTheme(
        theme="Drive mobile adoption",
        metric="Grow mobile app usage by 60% YoY.",
        decision_criteria="Needs app engagement, push notifications, and A/B testing.",
        decision_process="Marketing and Product are jointly evaluating vendors.",
        identify_pain="Mobile retention is weak, especially post-install.",
        notes={
            "why": "Mobile users churn after first login — high CAC, low LTV.",
            "why_now": "App Store reviews flagged poor UX.",
            "why_this_product": "We provide onboarding, targeting, and experimentation tools."
        }
    ),
    OpportunityTheme(
        theme="Prepare for security audit",
        metric="Pass SOC 2 Type II audit by Q1 next year.",
        decision_criteria="Continuous monitoring, access control, and risk reporting.",
        decision_process="Security and IT teams vetting 3 tools.",
        identify_pain="No centralized view of risk posture or controls.",
        notes={
            "why": "Security risks threaten enterprise deals.",
            "why_now": "An enterprise client made SOC 2 a blocker.",
            "why_this_product": "We automate evidence collection and control mapping."
        }
    )
]

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
    }

    if random.random() < 0.5:
        theme = random.choice(themes)
        opportunity.update({
            "Metrics": theme.metric,
            "Decision Criteria": theme.decision_criteria,
            "Decision Process": theme.decision_process,
            "Identify Pain": theme.identify_pain,
            "Notes": f"Why: {theme.notes['why']} Why Now: {theme.notes['why_now']} Why This Product: {theme.notes['why_this_product']}"
        })
        opportunity["Economic Buyer"] = fake.name()
        opportunity["Champion"] = fake.name()
        opportunity["Paper Process"] = "Standard legal review and redlines in Q3."
        opportunity["Competition"] = random.choice(["Vendor A", "Vendor B", "Internal Build", "None"])
    else:
        for field in medd_fields + ["Notes", "Metrics"]:
            opportunity[field] = None

    return opportunity


def generate_meddpicc_fields():
    return {
        "Metrics": generate_realistic_metric(),
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
