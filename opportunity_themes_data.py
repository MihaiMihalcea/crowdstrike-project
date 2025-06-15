from opportunity_theme import OpportunityTheme

opportunity_themes = [
    OpportunityTheme(
        theme="Improve lead qualification",
        metrics="Increase MQL to SQL conversion rate from 30% to 50%.",
        decision_criteria="Automation and accurate lead scoring is mandatory.",
        decision_process="Sales and Marketing jointly evaluating tools; decision in 6 weeks.",
        identify_pain="Too many unqualified leads passed to sales, causing inefficiency.",
        notes={
            "why": "Sales is frustrated with lead quality.",
            "why_now": "A new VP of Sales just joined with aggressive pipeline targets.",
            "why_this_product": "This platform uses AI to better score and qualify leads."
        },
        opportunity_type="Upsell",
        paper_process="Signed MSA, awaiting internal compliance check",
        competition="Salesforce",
        category="CRM"
    ),
    OpportunityTheme(
        theme="Reduce onboarding churn",
        metrics="Reduce onboarding churn rate from 15% to 5%.",
        decision_criteria="Requires detailed onboarding analytics and personalized onboarding journeys.",
        decision_process="Evaluating 2 vendors with pilot testing. Decision expected in Q3.",
        identify_pain="High churn in the first 14 days due to unclear value delivery and poor UX.",
        notes={
            "why": "Onboarding drop-off is the #1 reason users leave.",
            "why_now": "CS leadership just tied their bonus to reducing churn.",
            "why_this_product": "Our platform provides deep onboarding analytics and guided flows."
        },
        opportunity_type="New Business",
        paper_process="Legal review required, then IT security validation",
        competition="HubSpot",
        category="Customer Success"
    ),
    OpportunityTheme(
        theme="Speed up contract cycle",
        metrics="Cut average contract turnaround time from 18 to 7 days.",
        decision_criteria="Integration with DocuSign and redlining tools required.",
        decision_process="CFO and legal ops driving initiative; budget pre-approved.",
        identify_pain="Deals are getting stuck in legal review and approval chains.",
        notes={
            "why": "Faster deals = faster revenue.",
            "why_now": "Missed a major Q4 deal due to delays.",
            "why_this_product": "We integrate directly with their existing document stack."
        },
        opportunity_type="Pilot",
        paper_process="Expedited legal and procurement (1 week)",
        competition="Oracle",
        category="Legal Ops"
    ),
    OpportunityTheme(
        theme="Increase net retention",
        metrics="Improve NRR from 105% to 125% by year end.",
        decision_criteria="Must integrate with billing system and support playbooks.",
        decision_process="CFO-led growth initiative, involving finance and CS.",
        identify_pain="Accounts expand late or not at all; missed upsell signals.",
        notes={
            "why": "Growing revenue from existing customers is cost-efficient.",
            "why_now": "Board mandate to improve retention metrics post Series D.",
            "why_this_product": "Real-time expansion signals are built-in."
        },
        opportunity_type="Renewal",
        paper_process="Procurement review after finance sign-off",
        competition="Zendesk",
        category="Revenue Ops"
    ),
    OpportunityTheme(
        theme="Improve sales forecasting accuracy",
        metrics="Boost forecast accuracy from 60% to 90%.",
        decision_criteria="Native CRM integration and rep-level insights are key.",
        decision_process="Sales ops evaluating in coordination with CRO.",
        identify_pain="Inaccurate pipeline data is causing resource misallocation.",
        notes={
            "why": "Forecast misses lead to lost investor confidence.",
            "why_now": "Just missed Q2 forecast by 20%.",
            "why_this_product": "Provides weighted, rep-adjusted pipeline models."
        },
        opportunity_type="New Business",
        paper_process="Security and privacy compliance required",
        competition="Clari",
        category="Sales Ops"
    ),
    OpportunityTheme(
        theme="Optimize partner performance",
        metrics="Increase partner-attributed revenue by 30%.",
        decision_criteria="Channel attribution and customizable partner portals required.",
        decision_process="Channel head running proof-of-concept with 3 vendors.",
        identify_pain="Top partners are underperforming with unclear reporting.",
        notes={
            "why": "Partners drive 40% of total revenue.",
            "why_now": "New global partner program just launched.",
            "why_this_product": "Enables better enablement and real-time partner data."
        },
        opportunity_type="Pilot",
        paper_process="Simple vendor contract, 2-week turnaround",
        competition="Impartner",
        category="Channel"
    ),
    OpportunityTheme(
        theme="Reduce manual billing errors",
        metrics="Cut billing disputes by 80% and DSO by 15 days.",
        decision_criteria="ERP compatibility and audit trails are non-negotiable.",
        decision_process="Finance and RevOps are co-sponsoring evaluation.",
        identify_pain="Manual invoices cause recurring customer friction.",
        notes={
            "why": "Fixing billing unlocks cash faster.",
            "why_now": "Audit flagged inconsistencies for the third time.",
            "why_this_product": "Automates quote-to-cash with ERP sync."
        },
        opportunity_type="New Business",
        paper_process="IT review required before procurement step",
        competition="Zuora",
        category="Finance"
    ),
    OpportunityTheme(
        theme="Reduce sales rep ramp time",
        metrics="Cut average ramp time from 6 months to 3.",
        decision_criteria="Role-specific onboarding paths and analytics required.",
        decision_process="Enablement leader owning decision, testing in sandbox.",
        identify_pain="It takes too long for reps to become productive.",
        notes={
            "why": "Shorter ramp = more quota attainment faster.",
            "why_now": "Doubling sales headcount this year.",
            "why_this_product": "Personalized, role-based learning flows built-in."
        },
        opportunity_type="Upsell",
        paper_process="HR sign-off needed, then procurement",
        competition="Showpad",
        category="Enablement"
    ),
    OpportunityTheme(
        theme="Improve support response times",
        metrics="Cut average first response time from 8 to 2 hours.",
        decision_criteria="Slack integration and AI triage required.",
        decision_process="Support team pilot funded by CIO budget.",
        identify_pain="Customers wait too long for support responses.",
        notes={
            "why": "Speed = satisfaction in customer support.",
            "why_now": "Support NPS dropped below 30 last quarter.",
            "why_this_product": "Instant AI-based ticket prioritization."
        },
        opportunity_type="New Business",
        paper_process="One-pager and legal DPA approval",
        competition="Freshdesk",
        category="Support"
    ),
    OpportunityTheme(
        theme="Prevent revenue leakage",
        metrics="Recover $2M annually in missed renewals.",
        decision_criteria="Native renewal automation + alerting required.",
        decision_process="RevOps leading cross-functional evaluation.",
        identify_pain="Renewals are slipping through the cracks.",
        notes={
            "why": "Every missed renewal is pure loss.",
            "why_now": "Leadership introduced new retention KPIs.",
            "why_this_product": "Automates workflows around renewal dates."
        },
        opportunity_type="Renewal",
        paper_process="Standard NDA + IT security review",
        competition="Gainsight",
        category="Customer Success"
    ),
    OpportunityTheme(
        theme="Increase marketing attribution clarity",
        metrics="Tie 90% of pipeline to source campaign vs current 50%.",
        decision_criteria="Multi-touch attribution and CRM sync required.",
        decision_process="Marketing ops leading tool evaluation; CMO approval needed.",
        identify_pain="Attribution is too fragmented to justify spend.",
        notes={
            "why": "Need to double down on what works in marketing.",
            "why_now": "Budget cuts demand more efficiency.",
            "why_this_product": "True multi-touch attribution out of the box."
        },
        opportunity_type="New Business",
        paper_process="Simple vendor NDA followed by procurement review",
        competition="Marketo",
        category="Marketing"
    ),
    OpportunityTheme(
        theme="Automate compliance reporting",
        metrics="Save 500+ hours/year in compliance document prep.",
        decision_criteria="SOX, SOC 2, and GDPR support required.",
        decision_process="Security and Legal teams vetting vendors.",
        identify_pain="Manually compiling compliance reports is slow and error-prone.",
        notes={
            "why": "Avoiding non-compliance fines and reputation risk.",
            "why_now": "Audit window is approaching next quarter.",
            "why_this_product": "Auto-generates reports with audit trails."
        },
        opportunity_type="Pilot",
        paper_process="Compliance officer and legal team joint sign-off",
        competition="Vanta",
        category="Compliance"
    ),
    OpportunityTheme(
        theme="Boost product usage",
        metrics="Increase weekly active users by 40%.",
        decision_criteria="In-app nudges and usage dashboards needed.",
        decision_process="Product-led growth team piloting internally.",
        identify_pain="Low engagement despite large user base.",
        notes={
            "why": "Active users are more likely to convert or renew.",
            "why_now": "PMs now have growth targets for Q2.",
            "why_this_product": "In-app guidance and targeting is best-in-class."
        },
        opportunity_type="Upsell",
        paper_process="Product and analytics teams review jointly",
        competition="Pendo",
        category="Product"
    ),
    OpportunityTheme(
        theme="Enhance CSAT scores",
        metrics="Lift CSAT from 72% to 90% within 6 months.",
        decision_criteria="Integration with helpdesk and CS tools required.",
        decision_process="Customer success team evaluating platforms.",
        identify_pain="CSAT surveys often ignored or poorly timed.",
        notes={
            "why": "Customer loyalty is slipping.",
            "why_now": "CEO tied bonuses to customer satisfaction goals.",
            "why_this_product": "Delivers timely surveys and consolidates feedback."
        },
        opportunity_type="New Business",
        paper_process="DPA and SOC2 requirements mandatory",
        competition="Qualtrics",
        category="Customer Experience"
    ),
    OpportunityTheme(
        theme="Automate quarterly business reviews (QBRs)",
        metrics="Reduce QBR prep time from 4 hours to 30 minutes per account.",
        decision_criteria="Dynamic data pulling and templating features needed.",
        decision_process="Customer success managers requested proof-of-concept.",
        identify_pain="QBRs are time-consuming and inconsistent.",
        notes={
            "why": "Scalable QBRs = better renewals.",
            "why_now": "Team is stretched thin after layoffs.",
            "why_this_product": "Auto-populates decks with live account data."
        },
        opportunity_type="Pilot",
        paper_process="None — exec team greenlit pilot",
        competition="Gainsight",
        category="Customer Success"
    ),
    OpportunityTheme(
        theme="Consolidate sales tools",
        metrics="Cut SaaS costs by 25% through tool consolidation.",
        decision_criteria="Must replace at least 3 existing tools.",
        decision_process="Procurement-led review with Sales input.",
        identify_pain="Tech stack is bloated and expensive.",
        notes={
            "why": "Reducing costs while improving efficiency.",
            "why_now": "Budget freeze just kicked in.",
            "why_this_product": "Consolidates enablement, intelligence, and reporting."
        },
        opportunity_type="New Business",
        paper_process="Vendor onboarding + IT checklist",
        competition="Outreach",
        category="Sales Enablement"
    ),
    OpportunityTheme(
        theme="Detect churn risks early",
        metrics="Increase proactive saves by 50% per quarter.",
        decision_criteria="Health scoring and integration with CRM required.",
        decision_process="Customer Success ops team owns initiative.",
        identify_pain="Too many surprises in churned accounts.",
        notes={
            "why": "Churn prevention is cheaper than acquisition.",
            "why_now": "Q1 churn hit a 2-year high.",
            "why_this_product": "Predictive alerts let CSMs act earlier."
        },
        opportunity_type="Upsell",
        paper_process="Budget already approved, only security review left",
        competition="Totango",
        category="Customer Success"
    ),
    OpportunityTheme(
        theme="Improve product roadmap alignment",
        metrics="Capture and categorize 80% of customer feature requests.",
        decision_criteria="Must integrate with CRM and product board.",
        decision_process="Product and CS co-sponsoring trial phase.",
        identify_pain="Customer feedback isn’t reaching product team in time.",
        notes={
            "why": "Better input = more customer-driven roadmap.",
            "why_now": "New CPO wants faster iteration loops.",
            "why_this_product": "Connects feedback directly into backlog planning."
        },
        opportunity_type="Pilot",
        paper_process="No formal process, internal champions driving it",
        competition="Productboard",
        category="Product Management"
    ),
    OpportunityTheme(
        theme="Streamline customer onboarding",
        metrics="Reduce time-to-live from 45 to 15 days.",
        decision_criteria="Playbooks, milestones, and CRM sync required.",
        decision_process="Implementation team is testing with 3 accounts.",
        identify_pain="Clients delay go-lives due to confusion and misalignment.",
        notes={
            "why": "Faster onboarding means faster value.",
            "why_now": "NPS suffers when onboarding is slow.",
            "why_this_product": "Customizable playbooks and stakeholder visibility included."
        },
        opportunity_type="New Business",
        paper_process="Security and customer onboarding review",
        competition="GuideCX",
        category="Implementation"
    ),
    OpportunityTheme(
        theme="Unlock upsell opportunities",
        metrics="Grow ACV per account by 25% through data-driven expansion.",
        decision_criteria="Insights into usage and engagement required.",
        decision_process="CS and Sales jointly driving evaluation.",
        identify_pain="Missed upsell windows due to lack of account signals.",
        notes={
            "why": "Maximizing customer lifetime value.",
            "why_now": "Revenue target doubled for renewals team.",
            "why_this_product": "Signals tied directly to product usage data."
        },
        opportunity_type="Upsell",
        paper_process="Expansion MSA in place, no redlines expected",
        competition="Gainsight PX",
        category="Revenue Expansion"
    ),
    OpportunityTheme(
        theme="Centralize revenue operations data",
        metrics="Create a single source of truth for revenue teams.",
        decision_criteria="Connects CRM, billing, and marketing data sources.",
        decision_process="RevOps is piloting internally with 2 use cases.",
        identify_pain="Data is siloed across tools, leading to reporting conflicts.",
        notes={
            "why": "Everyone is building reports on different data sets.",
            "why_now": "Board requested unified view of revenue health.",
            "why_this_product": "Unifies revenue data across the full customer journey."
        },
        opportunity_type="New Business",
        paper_process="DPA and SOC2 audit needed",
        competition="RevOps.io",
        category="Revenue Ops"
    ),
    OpportunityTheme(
        theme="Improve pricing strategy",
        metrics="Optimize pricing model to increase win rate by 15%.",
        decision_criteria="Support for pricing experiments and segmentation.",
        decision_process="Finance and Product testing 3 vendors with sandbox access.",
        identify_pain="Losing deals due to rigid or outdated pricing.",
        notes={
            "why": "Pricing is a major lever for growth.",
            "why_now": "Market conditions changed rapidly in last 6 months.",
            "why_this_product": "Dynamic pricing with real-time insights."
        },
        opportunity_type="Pilot",
        paper_process="Finance compliance and sandbox sign-off required",
        competition="ProfitWell",
        category="Pricing"
    ),
    OpportunityTheme(
        theme="Enable self-service support",
        metrics="Reduce support tickets by 40% via better self-help tools.",
        decision_criteria="Search, analytics, and feedback tracking required.",
        decision_process="Support ops leading RFP process; exec champion identified.",
        identify_pain="Low usage of help center, high repetitive tickets.",
        notes={
            "why": "Support can't scale linearly with growth.",
            "why_now": "Ticket volume doubled in last 2 quarters.",
            "why_this_product": "Smart search and contextual help out of the box."
        },
        opportunity_type="New Business",
        paper_process="Security and customer trust team involved",
        competition="Zendesk Guide",
        category="Support"
    ),
    OpportunityTheme(
        theme="Improve executive visibility",
        metrics="Create live dashboards for board and C-suite.",
        decision_criteria="Connects to CRM, billing, and CS tools easily.",
        decision_process="CRO and CEO both involved in vendor selection.",
        identify_pain="Executives don't have real-time visibility into metrics.",
        notes={
            "why": "Leadership flying blind is risky.",
            "why_now": "Just missed key KPIs and want to prevent recurrence.",
            "why_this_product": "Live board-ready dashboards with no-code setup."
        },
        opportunity_type="Upsell",
        paper_process="Executive approval only; already a vendor",
        competition="Tableau",
        category="Analytics"
    )
]