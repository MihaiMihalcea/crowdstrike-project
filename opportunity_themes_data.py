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
    ),
    OpportunityTheme(
        theme="Expand into EMEA market",
        metrics="Increase EMEA revenue by 20% within 12 months.",
        decision_criteria="Needs multi-currency, multilingual support and strong local compliance.",
        decision_process="Working with international consultants, final decision in 45 days.",
        identify_pain="Limited market share in Europe due to lack of localized presence.",
        notes={
            "why": "Global expansion is part of the annual growth strategy.",
            "why_now": "Just opened new EMEA HQ and hired regional leadership.",
            "why_this_product": "We offer region-specific compliance and localization out of the box."
        },
        opportunity_type="New Business",
        paper_process="International procurement team and legal review required.",
        competition="Evaluating a German competitor with limited integrations.",
        category="International Expansion"
    ),
    OpportunityTheme(
        theme="Automate financial reporting",
        metrics="Cut manual reporting hours by 60%.",
        decision_criteria="Must integrate with existing ERP and support GAAP compliance.",
        decision_process="Finance team piloting two platforms; exec sponsor signs off next month.",
        identify_pain="Quarter-end closing takes too long due to manual data pulls.",
        notes={
            "why": "Manual processes are delaying strategic analysis.",
            "why_now": "New CFO is driving automation initiatives.",
            "why_this_product": "Our automation engine pulls real-time data from ERPs seamlessly."
        },
        opportunity_type="Upsell",
        paper_process="Finance-led vendor onboarding and security review.",
        competition="Oracle module and one FinTech startup.",
        category="Finance Automation"
    ),
    OpportunityTheme(
        theme="Replace legacy support system",
        metrics="Improve CSAT by 15% and reduce ticket resolution time by 30%.",
        decision_criteria="Needs omnichannel support, AI-powered routing, and SLA tracking.",
        decision_process="IT and CX teams reviewing RFP responses, shortlist in 3 weeks.",
        identify_pain="Current system lacks automation and analytics.",
        notes={
            "why": "Customer satisfaction is flatlining despite growing headcount.",
            "why_now": "Recent leadership shift in CX department.",
            "why_this_product": "Only vendor offering native AI routing and full audit trails."
        },
        opportunity_type="Rip and Replace",
        paper_process="Procurement and InfoSec involved.",
        competition="Zendesk, Salesforce Service Cloud.",
        category="Customer Experience"
    ),
    OpportunityTheme(
        theme="Consolidate martech stack",
        metrics="Cut martech costs by 25% and increase campaign efficiency.",
        decision_criteria="Must replace 3 tools and offer advanced segmentation.",
        decision_process="Marketing and RevOps running a proof of concept.",
        identify_pain="Tool fragmentation leads to inconsistent customer journeys.",
        notes={
            "why": "Stack is bloated and slowing campaigns down.",
            "why_now": "New VP of Marketing initiated consolidation.",
            "why_this_product": "We combine 4 tools into one, with better data integrity."
        },
        opportunity_type="Consolidation",
        paper_process="CMO sign-off with IT data audit.",
        competition="HubSpot, Iterable.",
        category="Marketing Ops"
    ),
    OpportunityTheme(
        theme="Prepare for IPO compliance",
        metrics="Achieve SOX readiness and close audits in <30 days.",
        decision_criteria="Needs full audit trails, role-based access, and secure archiving.",
        decision_process="Internal compliance team is building shortlist from Big 4 guidance.",
        identify_pain="Current systems don't support detailed tracking or retention.",
        notes={
            "why": "Company targets IPO by Q2 next year.",
            "why_now": "Board requested internal readiness audit.",
            "why_this_product": "Our solution is SOC2 + SOX compliant with rapid deployment."
        },
        opportunity_type="Compliance",
        paper_process="Legal, compliance, and external counsel involved.",
        competition="Workiva, proprietary solutions.",
        category="Risk & Compliance"
    ),
    OpportunityTheme(
        theme="Launch embedded payments",
        metrics="Add new revenue stream by enabling payments within platform.",
        decision_criteria="PCI compliance, white-label support, and low transaction fees required.",
        decision_process="Product and Finance teams are doing feasibility assessment.",
        identify_pain="Current offering lacks monetization beyond subscriptions.",
        notes={
            "why": "Leadership wants to diversify revenue with financial services.",
            "why_now": "Market pressure and investor interest in fintech integrations.",
            "why_this_product": "We offer ready-to-integrate APIs with compliance and fraud detection."
        },
        opportunity_type="New Revenue Line",
        paper_process="Finance, product, and legal to approve jointly.",
        competition="Stripe Connect, Adyen.",
        category="Product-Led Growth"
    ),
    OpportunityTheme(
        theme="Implement ESG reporting",
        metrics="Enable quarterly ESG disclosures with 100% audit readiness.",
        decision_criteria="Must support GRI and SASB standards with data ingestion.",
        decision_process="ESG team is piloting with Sustainability Ops and third-party auditor.",
        identify_pain="Manual ESG tracking is inconsistent and not auditable.",
        notes={
            "why": "Investors are asking for transparent ESG metrics.",
            "why_now": "ESG audit coming up in Q4.",
            "why_this_product": "Only vendor with native SASB/GRI templates and verification APIs."
        },
        opportunity_type="Compliance",
        paper_process="Board-level approval and 3rd-party audit review.",
        competition="Workiva ESG, Microsoft Sustainability Manager.",
        category="Sustainability"
    ),
    OpportunityTheme(
        theme="Streamline channel sales operations",
        metrics="Reduce partner onboarding time by 40%.",
        decision_criteria="Partner portal, co-selling workflows, and approval flows required.",
        decision_process="Channel Ops team issuing RFI to 3 vendors.",
        identify_pain="Manual partner management delays revenue collection.",
        notes={
            "why": "New VP of Channels is restructuring partner tiers.",
            "why_now": "Q2 partner pipeline is blocked by onboarding delays.",
            "why_this_product": "Purpose-built for channel workflows and deal registration."
        },
        opportunity_type="Channel Expansion",
        paper_process="Channel leadership and deal desk.",
        competition="Salesforce PRM, Channeltivity.",
        category="Sales Ops"
    ),
    OpportunityTheme(
        theme="Enhance product analytics",
        metrics="Increase product engagement by 25% in 6 months.",
        decision_criteria="Granular event tracking, retention cohorting, and funnel visualization.",
        decision_process="Product managers evaluating 3 vendors via sandbox environments.",
        identify_pain="Current tool lacks visibility into feature-level adoption.",
        notes={
            "why": "Product roadmap tied to usage-based growth KPIs.",
            "why_now": "Launching new features and want instant feedback loops.",
            "why_this_product": "Best-in-class cohorting and product-led insight engine."
        },
        opportunity_type="Upsell",
        paper_process="Product and analytics heads approve together.",
        competition="Heap, Amplitude.",
        category="Product Analytics"
    ),
    OpportunityTheme(
        theme="Reduce billing disputes",
        metrics="Reduce invoice dispute rates from 12% to 2%.",
        decision_criteria="Automated billing rules, preview invoicing, and audit logs.",
        decision_process="Finance automation initiative led by RevOps and billing team.",
        identify_pain="Frequent errors in contract-to-invoice mapping.",
        notes={
            "why": "Billing disputes delay cash flow and impact trust.",
            "why_now": "Recent customer churn attributed to billing issues.",
            "why_this_product": "We integrate directly with CRM and CPQ to avoid mismatch."
        },
        opportunity_type="Customer Retention",
        paper_process="RevOps and finance sign-off required.",
        competition="Zuora, in-house scripts.",
        category="Revenue Ops"
    ),
    OpportunityTheme(
        theme="Monitor SaaS usage for cost control",
        metrics="Cut unused SaaS spend by 20% across departments.",
        decision_criteria="SSO integrations, usage visibility, and renewal alerting.",
        decision_process="Procurement and IT evaluating vendors with finance overlay.",
        identify_pain="Shadow IT causing overspend and redundancy.",
        notes={
            "why": "CFO aims to rein in uncontrolled SaaS growth.",
            "why_now": "Renewal calendar spiked this quarter.",
            "why_this_product": "Deep integrations with Okta and license reconciliation tools."
        },
        opportunity_type="Cost Optimization",
        paper_process="Procurement and budget owner alignment.",
        competition="Zluri, Torii, spreadsheets.",
        category="IT Finance"
    ),
    OpportunityTheme(
        theme="Prevent insider threats",
        metrics="Detect and mitigate insider incidents in <24 hours.",
        decision_criteria="User behavior monitoring, data exfiltration alerts, and role-based rules.",
        decision_process="Security team conducting internal red-team exercises.",
        identify_pain="Recent data leak traced to privileged access misuse.",
        notes={
            "why": "Leadership is concerned about internal risk surface.",
            "why_now": "Regulators flagged insider monitoring as weak.",
            "why_this_product": "Proactive user behavior analytics with SOC integration."
        },
        opportunity_type="Security Upgrade",
        paper_process="CISO and legal alignment required.",
        competition="ObserveIT, Varonis.",
        category="Cybersecurity"
    ),
    OpportunityTheme(
        theme="Launch virtual onboarding for remote hires",
        metrics="Reduce new hire time-to-productivity from 40 to 20 days.",
        decision_criteria="Workflow automation, LMS integration, and HRIS sync.",
        decision_process="HR and IT co-sponsoring pilot with two platforms.",
        identify_pain="Remote hires are underperforming vs. on-site cohort.",
        notes={
            "why": "Workforce is now 70% remote.",
            "why_now": "Q2 hiring spike requires scalable onboarding.",
            "why_this_product": "Smooth remote onboarding with built-in analytics."
        },
        opportunity_type="HR Transformation",
        paper_process="HR tech committee and CIO approval.",
        competition="Rippling, Workday LMS module.",
        category="People Ops"
    ),
    OpportunityTheme(
        theme="Improve mobile user retention",
        metrics="Lift D30 retention from 10% to 20%.",
        decision_criteria="Push notification optimization, A/B testing, and deep linking.",
        decision_process="Growth team running experiments across tools.",
        identify_pain="Mobile retention lags despite feature parity.",
        notes={
            "why": "Mobile segment is the company’s fastest-growing user base.",
            "why_now": "Churn is limiting LTV for mobile customers.",
            "why_this_product": "Best-in-class mobile engagement orchestration."
        },
        opportunity_type="User Growth",
        paper_process="Growth and mobile leads to approve.",
        competition="Leanplum, OneSignal.",
        category="Growth Marketing"
    ),
    OpportunityTheme(
        theme="Establish unified customer view",
        metrics="90% identity resolution rate across platforms.",
        decision_criteria="Cross-channel ID stitching, CDP integrations, privacy compliance.",
        decision_process="Data team leading architecture design with marketing input.",
        identify_pain="Customer data lives in silos with no single view.",
        notes={
            "why": "Without unified data, personalization is impossible.",
            "why_now": "Personalization mandates added to H2 OKRs.",
            "why_this_product": "Real-time CDP with flexible schema mapping."
        },
        opportunity_type="Data Unification",
        paper_process="Data governance and security approval flow.",
        competition="Segment, BlueConic.",
        category="Data Strategy"
    ),
    OpportunityTheme(
        theme="Automate SOC 2 readiness",
        metrics="Complete SOC 2 audit prep in under 6 weeks.",
        decision_criteria="Evidence collection automation, risk scoring, and pre-built controls.",
        decision_process="Security team evaluating vendors against auditor checklist.",
        identify_pain="Manual readiness takes too long and risks missed evidence.",
        notes={
            "why": "Customer asks for SOC 2 during procurement.",
            "why_now": "New enterprise contracts blocked until SOC 2 is ready.",
            "why_this_product": "Out-of-the-box SOC 2 policy engine and integrations."
        },
        opportunity_type="Security Certification",
        paper_process="Audit team, CISO, and external auditor approval.",
        competition="Vanta, Drata.",
        category="Information Security"
    ),
    OpportunityTheme(
        theme="Automate compliance reporting",
        metrics="Reduce time spent on compliance reporting by 75%.",
        decision_criteria="Must integrate with existing data warehouse and generate export-ready reports.",
        decision_process="CFO and Risk Manager reviewing automation tools. Decision expected by end of quarter.",
        identify_pain="Manual compliance reports take weeks and are prone to human error.",
        notes={
            "why": "Compliance audits are increasing in frequency and complexity.",
            "why_now": "A recent audit highlighted inconsistencies in manual reporting.",
            "why_this_product": "Our solution auto-generates reports directly from verified data sources."
        },
        opportunity_type="New Business",
        paper_process="Legal review and data security assessment required.",
        competition="Facing competition from a niche RegTech vendor.",
        category="Compliance Automation"
    ),
    OpportunityTheme(
        theme="Improve employee engagement",
        metrics="Increase employee eNPS score by 20 points within a year.",
        decision_criteria="Needs pulse surveys, engagement analytics, and real-time dashboards.",
        decision_process="HR and IT teams are conducting joint evaluations with demos.",
        identify_pain="Low morale and high turnover in key departments.",
        notes={
            "why": "Engagement directly impacts retention and productivity.",
            "why_now": "Recent employee survey showed a sharp drop in satisfaction.",
            "why_this_product": "Our platform offers targeted feedback loops and engagement playbooks."
        },
        opportunity_type="Expansion",
        paper_process="Needs HR, Legal, and IT sign-off.",
        competition="Competing against incumbent HCM solution.",
        category="People Operations"
    ),
    OpportunityTheme(
        theme="Streamline vendor onboarding",
        metrics="Reduce vendor onboarding time from 6 weeks to 2 weeks.",
        decision_criteria="Requires document collection automation and workflow routing.",
        decision_process="Procurement lead is championing the initiative; board approval needed.",
        identify_pain="Delays in onboarding impact project timelines and budget.",
        notes={
            "why": "Current vendor onboarding is manual and error-prone.",
            "why_now": "Company scaling partnerships rapidly and process can't keep up.",
            "why_this_product": "Our workflow engine automates compliance checks and document collection."
        },
        opportunity_type="New Business",
        paper_process="Standard procurement process with risk review.",
        competition="Custom-built internal tools.",
        category="Procurement & Ops"
    ),
    OpportunityTheme(
        theme="Forecast revenue more accurately",
        metrics="Improve forecast accuracy from 70% to 95%.",
        decision_criteria="Must integrate with CRM and support scenario modeling.",
        decision_process="RevOps and Finance collaborating; vendor shortlist created.",
        identify_pain="Frequent misses on quarterly projections.",
        notes={
            "why": "Better forecasting drives better strategic decisions.",
            "why_now": "New CFO pushing for precision and accountability.",
            "why_this_product": "We offer AI-powered forecast modeling with CRM sync."
        },
        opportunity_type="New Business",
        paper_process="Legal review and compliance with SOX standards.",
        competition="Spreadsheets and legacy forecasting tools.",
        category="Revenue Operations"
    ),
    OpportunityTheme(
        theme="Increase product adoption",
        metrics="Grow active user base by 40% in the next 6 months.",
        decision_criteria="Needs in-app nudges, analytics, and segmentation tools.",
        decision_process="Product team evaluating tools in parallel with user research.",
        identify_pain="Users sign up but don’t engage beyond the first week.",
        notes={
            "why": "Adoption is lagging despite marketing efforts.",
            "why_now": "Product-led growth strategy just launched.",
            "why_this_product": "Our in-app guidance and analytics improve activation rates."
        },
        opportunity_type="Expansion",
        paper_process="Fast-track pilot with Product team approval.",
        competition="Lightweight no-code competitors.",
        category="Product Growth"
    ),
    OpportunityTheme(
        theme="Strengthen data privacy controls",
        metrics="Achieve full GDPR/CCPA compliance across all user data.",
        decision_criteria="Must provide automated data subject request handling.",
        decision_process="Legal and Engineering teams collaborating on selection.",
        identify_pain="Risk of non-compliance penalties and brand damage.",
        notes={
            "why": "Data privacy regulations are tightening globally.",
            "why_now": "A recent breach incident triggered internal review.",
            "why_this_product": "Built-in workflows for deletion, access, and consent."
        },
        opportunity_type="New Business",
        paper_process="Mandatory review by InfoSec and legal.",
        competition="Legacy data governance solutions.",
        category="Security & Compliance"
    ),
    OpportunityTheme(
        theme="Accelerate invoice processing",
        metrics="Reduce average invoice processing time by 80%.",
        decision_criteria="Needs OCR, approval routing, and ERP integration.",
        decision_process="Finance and AP departments reviewing solutions jointly.",
        identify_pain="Manual invoicing leads to delayed payments and missed discounts.",
        notes={
            "why": "Late payments hurt supplier relationships and incur fees.",
            "why_now": "High invoice volume expected with upcoming expansion.",
            "why_this_product": "We provide intelligent capture and automated workflows."
        },
        opportunity_type="New Business",
        paper_process="Standard Finance-led procurement flow.",
        competition="Manual processes and basic AP tools.",
        category="Finance Automation"
    ),
    OpportunityTheme(
        theme="Reduce cloud costs",
        metrics="Cut monthly cloud spend by 30% without impacting performance.",
        decision_criteria="Must support real-time monitoring and automated scaling.",
        decision_process="DevOps and Finance teams jointly reviewing solutions.",
        identify_pain="Unpredictable costs due to underutilized resources.",
        notes={
            "why": "Cloud costs are outpacing revenue growth.",
            "why_now": "Leadership launched a cost-efficiency mandate.",
            "why_this_product": "Our platform offers optimization insights and automation."
        },
        opportunity_type="Expansion",
        paper_process="Cloud cost center approval only.",
        competition="Cloud-native billing tools.",
        category="IT & Infrastructure"
    ),
    OpportunityTheme(
        theme="Modernize IT ticketing system",
        metrics="Reduce internal ticket resolution time by 50%.",
        decision_criteria="Requires AI routing, SLAs, and integration with Slack.",
        decision_process="IT Director running pilot with two vendors.",
        identify_pain="Tickets pile up and support quality suffers.",
        notes={
            "why": "IT team is understaffed and overwhelmed.",
            "why_now": "Employee satisfaction score dropped due to IT response delays.",
            "why_this_product": "We use ML to route and resolve IT issues quickly."
        },
        opportunity_type="Replacement",
        paper_process="IT and procurement review process.",
        competition="Jira Service Management and Freshdesk.",
        category="IT Operations"
    ),
    OpportunityTheme(
        theme="Unify marketing analytics",
        metrics="Achieve a 360° view of campaign performance across all channels.",
        decision_criteria="Requires multi-touch attribution and real-time dashboards.",
        decision_process="Marketing and BI teams evaluating via trial access.",
        identify_pain="Siloed data prevents meaningful attribution.",
        notes={
            "why": "They need to prove marketing ROI to secure budget.",
            "why_now": "New VP of Marketing demanding unified visibility.",
            "why_this_product": "We connect all platforms and offer deep cross-channel insights."
        },
        opportunity_type="New Business",
        paper_process="Marketing ops review and IT sign-off.",
        competition="Existing BI dashboards and spreadsheets.",
        category="Marketing Analytics"
    )
]