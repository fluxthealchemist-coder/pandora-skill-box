import os

base = os.path.dirname(os.path.abspath(__file__))

# ============================================================
# SKILL DATABASE — 25 skills per vertical
# ============================================================

verticals = {
    "sales": {
        "title": "Sales \u0026 Business Development",
        "tagline": "Lead generation, prospecting, CRM automation, cold outreach sequences, and pipeline management — 25 skills that turn any rep into a closer.",
        "skills": [
            ("Lead Scoring Framework", "PROSPECTING", "Qualify leads with weighted scoring models based on BANT, MEDDIC, and custom criteria. $19", "#"),
            ("Apollo.io Outreach Builder", "PROSPECTING", "Build targeted contact lists, sequence templates, and A/B test copy for Apollo campaigns. $19", "#"),
            ("Cold Email Chain Designer", "OUTREACH", "7-touch email sequences with subject line variants, openers, and objection handlers. $19", "#"),
            ("LinkedIn Prospecting System", "SOCIAL", "Connection request scripts, InMail templates, and content engagement playbooks for LinkedIn. $19", "#"),
            ("CRM Hygiene \u0026 Enrichment", "CRM", "Dedupe, standardize, and enrich contact records with firmographic and technographic data. $19", "#"),
            ("Discovery Call Script", "CALLS", "Structured first-call framework — pain detection, budget confirmation, timeline mapping. $19", "#"),
            ("Demo Personalization Engine", "DEMO", "Tailor product demos to industry, role, and use case with dynamic storyline builder. $19", "#"),
            ("Proposal \u0026 Quote Generator", "CLOSE", "Professional proposals with pricing tables, terms, and e-signature integration. $19", "#"),
            ("Objection Response Library", "CLOSE", "50+ proven responses to price, timing, authority, and competition objections. $19", "#"),
            ("Sales Deck Narrative Builder", "PRESENT", "Story-driven pitch decks with proof points, case studies, and CTA slides. $19", "#"),
            ("Pipeline Forecasting Model", "ANALYTICS", "Weighted pipeline stages, commit calculations, and variance analysis by rep. $19", "#"),
            ("Competitor Battle Card", "INTEL", "Head-to-head comparison grids — feature, price, and positioning for any competitor. $19", "#"),
            ("Account-Based Marketing Plan", "ABM", "Target account selection, stakeholder mapping, and personalized campaign plays. $19", "#"),
            ("Churn Risk Scoring", "RETENTION", "Early-warning indicators, intervention playbooks, and save-sequence automation. $19", "#"),
            ("Upsell \u0026 Cross-sell Detector", "EXPANSION", "Usage-pattern triggers, expansion timing, and upgrade proposal templates. $19", "#"),
            ("Referral Request System", "NETWORK", "Timing, messaging, and incentive structures for customer referral generation. $19", "#"),
            ("RFP Response Builder", "ENTERPRISE", "Standardized RFP answer library, compliance checklists, and submission formatting. $19", "#"),
            ("Territory Planning Model", "STRATEGY", "Account distribution, quota allocation, and coverage optimization by geography. $19", "#"),
            ("Sales Compensation Calculator", "COMP", "OTE splits, accelerator tiers, clawback rules, and attainment projections. $19", "#"),
            ("Win-Loss Analysis Template", "ANALYTICS", "Structured debriefs — why we won, why we lost, and pattern aggregation. $19", "#"),
            ("Sales Onboarding Playbook", "ENABLEMENT", "30-60-90 day ramp plan, certification milestones, and shadow schedule. $19", "#"),
            ("Call Recording Insight Extractor", "ENABLEMENT", "Transcript analysis, talk-ratio scoring, and coaching moment identification. $19", "#"),
            ("Pricing Negotiation Matrix", "CLOSE", "Discount authority levels, trade-off options, and margin-protected counteroffers. $19", "#"),
            ("Event Lead Capture System", "FIELD", "Badge-scan workflows, follow-up sequences, and ROI tracking for trade shows. $19", "#"),
            ("Sales Handoff to CS Brief", "HANDOFF", "Complete context transfer — stakeholders, promises, risks, and onboarding triggers. $19", "#"),
        ]
    },
    "marketing": {
        "title": "Marketing \u0026 Growth",
        "tagline": "Campaign planning, content creation, brand voice, review management, and audience intelligence — 25 skills for modern marketers.",
        "skills": [
            ("Campaign Brief Builder", "STRATEGY", "Objective, audience, message, channel, and KPI definition for any campaign. $19", "#"),
            ("Brand Voice Guide Generator", "BRAND", "Tone pillars, vocabulary rules, do/don't lists, and sample copy by channel. $19", "#"),
            ("Content Calendar Planner", "CONTENT", "Monthly editorial calendar with themes, formats, deadlines, and owner assignments. $19", "#"),
            ("SEO Audit Checklist", "SEO", "Technical, on-page, off-page, and local SEO scoring with prioritized fixes. $19", "#"),
            ("Social Media Ad Copy Pack", "PAID", "Headline-body-CTA variants for Meta, LinkedIn, X, and TikTok ads. $19", "#"),
            ("Landing Page Copy Optimizer", "CONVERSION", "Hero, social proof, benefit bullets, FAQ, and CTA sections for any offer. $19", "#"),
            ("Email Drip Sequence Writer", "EMAIL", "Welcome, nurture, re-engagement, and win-back sequences with send logic. $19", "#"),
            ("Influencer Outreach Brief", "PR", "Pitch templates, rate negotiation, deliverable specs, and tracking setup. $19", "#"),
            ("Review Response Generator", "REPUTATION", "Positive and negative review responses for Google, TripAdvisor, and industry sites. $19", "#"),
            ("Competitor Ad Intel Brief", "INTEL", "Messaging analysis, offer comparison, and gap identification from public ads. $19", "#"),
            ("Customer Persona Builder", "AUDIENCE", "Demographic, psychographic, pain-point, and journey-map profiles. $19", "#"),
            ("Video Script Template", "VIDEO", "Hook-problem-solution-CTA structure for 30, 60, and 90-second formats. $19", "#"),
            ("Press Release Draft", "PR", "Newsworthy angle, quote insertion, boilerplate, and journalist pitching list. $19", "#"),
            ("Marketing Budget Allocator", "FINANCE", "Channel mix, CAC targets, ROI projections, and reallocation triggers. $19", "#"),
            ("A/B Test Design Framework", "EXPERIMENT", "Hypothesis, variant, sample size, duration, and success criteria. $19", "#"),
            ("Webinar Promotion Kit", "EVENTS", "Registration page, reminder sequence, social posts, and follow-up nurture. $19", "#"),
            ("Product Launch Playbook", "LAUNCH", "Pre-launch, launch-day, and post-launch activities with owner and deadline. $19", "#"),
            ("UTM Tagging Generator", "ANALYTICS", "Campaign, source, medium, and content parameters with naming convention. $19", "#"),
            ("Lead Magnet Creator", "GROWTH", "Ebook, checklist, or template outline with title, hook, and delivery flow. $19", "#"),
            ("Customer Survey Designer", "RESEARCH", "NPS, CSAT, product-market fit, and churn reason questionnaires. $19", "#"),
            ("Marketing Dashboard Builder", "ANALYTICS", "KPI hierarchy, data sources, refresh schedule, and alert thresholds. $19", "#"),
            ("Referral Program Design", "GROWTH", "Incentive structure, landing page, email triggers, and reward fulfillment. $19", "#"),
            ("Podcast Guest Pitch Kit", "PR", "Angle selection, bio draft, talking points, and episode promotion plan. $19", "#"),
            ("Affiliate Program Brief", "PARTNERS", "Commission tiers, terms, tracking setup, and onboarding sequence. $19", "#"),
            ("Crisis Response Template", "REPUTATION", "Escalation protocol, holding statement, channel response, and post-mortem. $19", "#"),
        ]
    },
    "customer-support": {
        "title": "Customer Support \u0026 Services",
        "tagline": "Ticket response, escalation handling, knowledge base articles, and support QA workflows — 25 skills for service teams.",
        "skills": [
            ("First Response Template Library", "TICKETS", "Acknowledgment, expectation-setting, and empathy statements by issue type. $19", "#"),
            ("Escalation Decision Tree", "PROCESS", "When, who, and how to escalate — with criteria and handoff templates. $19", "#"),
            ("Knowledge Base Article Writer", "CONTENT", "Search-optimized help articles with structure, screenshots guide, and linking. $19", "#"),
            ("Ticket Categorization System", "OPS", "Tag taxonomy, priority matrix, and auto-routing rules by product area. $19", "#"),
            ("Customer Satisfaction Survey", "QA", "Post-resolution CSAT, CES, and qualitative feedback collection. $19", "#"),
            ("Refund \u0026 Return SOP", "POLICY", "Eligibility check, approval workflow, and processing steps with templates. $19", "#"),
            ("Onboarding Support Sequence", "SUCCESS", "Day 1, 3, 7, 30 check-in emails for new customers. $19", "#"),
            ("Complaint Resolution Playbook", "RECOVERY", "De-escalation steps, compensation framework, and closure confirmation. $19", "#"),
            ("Chatbot Conversation Flow", "AUTOMATION", "Greeting, intent detection, answer retrieval, and human handoff logic. $19", "#"),
            ("SLA Compliance Tracker", "OPS", "Response and resolution time monitoring, breach alerts, and root cause. $19", "#"),
            ("Agent QA Scorecard", "COACHING", "Tone, accuracy, empathy, and resolution scoring with calibration guide. $19", "#"),
            ("Product Feedback Aggregator", "VOICE", "Feature request triage, trend reporting, and product team handoff. $19", "#"),
            ("Outage Communication Template", "CRISIS", "Status page copy, customer email, and social update for downtime. $19", "#"),
            ("Multilingual Response Guide", "GLOBAL", "Common phrases in Arabic, Hindi, French, and Mandarin for support. $19", "#"),
            ("VIP Customer Handling SOP", "RETENTION", "White-glove response, dedicated queue, and executive escalation path. $19", "#"),
            ("Billing Dispute Resolver", "FINANCE", "Invoice review, proration calculation, and dispute documentation. $19", "#"),
            ("Proactive Health Check Script", "SUCCESS", "Usage review, risk identification, and recommendation outreach. $19", "#"),
            ("Community Forum Moderation", "ENGAGEMENT", "Reply guidelines, escalation rules, and toxic content handling. $19", "#"),
            ("Video Support Tutorial Script", "CONTENT", "Step-by-step screen recording scripts with narration and markers. $19", "#"),
            ("Seasonal Surge Planner", "OPS", "Staffing model, FAQ pre-emption, and deflection strategy for peak periods. $19", "#"),
            ("Support Knowledge Quiz", "TRAINING", "Product, policy, and procedure assessments with scoring and remediation. $19", "#"),
            ("Customer Exit Interview", "CHURN", "Departure reasons, competitive intelligence, and win-back opportunity. $19", "#"),
            ("Self-Service Deflection Audit", "EFFICIENCY", "Contact reason analysis, portal gap identification, and improvement plan. $19", "#"),
            ("Integration Troubleshooter", "TECH", "API error decoding, credential verification, and vendor coordination. $19", "#"),
            ("Support Team Dashboard", "ANALYTICS", "Volume, CSAT, SLA, backlog, and agent performance in one view. $19", "#"),
        ]
    },
    "coaching": {
        "title": "Coaching \u0026 Training",
        "tagline": "Discovery call prep, session notes, client progress dashboards, coaching action plans, and workshop facilitation — 25 skills for coaches and trainers.",
        "skills": [
            ("Discovery Call Prep", "INTAKE", "Pre-call questionnaire, goal extraction, and expectation alignment. $19", "#"),
            ("Coaching Agreement Draft", "LEGAL", "Scope, boundaries, confidentiality, cancellation, and payment terms. $19", "#"),
            ("Session Note Template", "ADMIN", "Structured post-session notes — insights, actions, and follow-ups. $19", "#"),
            ("Client Progress Dashboard", "TRACKING", "Goal milestone tracker, habit scorecard, and trend visualization. $19", "#"),
            ("Accountability Email Sequence", "ENGAGEMENT", "Weekly check-ins, milestone celebrations, and nudge triggers. $19", "#"),
            ("Workshop Design Blueprint", "FACILITATION", "Agenda, exercises, materials, timing, and debrief for half-day workshops. $19", "#"),
            ("Assessment Questionnaire Builder", "EVAL", "360-degree, personality, skills, and readiness assessments. $19", "#"),
            ("Goal Setting Framework", "PLANNING", "SMART, OKR, or GROW model goal documents with accountability hooks. $19", "#"),
            ("Homework Assignment Designer", "ACTION", "Between-session tasks with deadline, success criteria, and reflection prompts. $19", "#"),
            ("Group Coaching Session Plan", "GROUP", "Icebreakers, breakout activities, sharing protocols, and wrap structure. $19", "#"),
            ("Certification Tracking Sheet", "CREDENTIALS", "Module completion, assessment scores, and certificate issuance. $19", "#"),
            ("Client Offboarding Summary", "CLOSE", "Progress recap, resource handover, and testimonial request. $19", "#"),
            ("Testimonial Request Script", "MARKETING", "Timing, framing, and format options for powerful client testimonials. $19", "#"),
            ("Package Pricing Calculator", "FINANCE", "Session bundles, payment plans, and value-based pricing models. $19", "#"),
            ("Referral Partner Brief", "GROWTH", "Introduction email, commission structure, and ideal client profile. $19", "#"),
            ("Onboarding Welcome Sequence", "EXPERIENCE", "Pre-coaching prep, tool setup, and first-week engagement plan. $19", "#"),
            ("Conflict Resolution Script", "DIFFICULT", "Defusing tension, reframing perspectives, and mutual agreement. $19", "#"),
            ("Energy \u0026 Burnout Assessment", "WELLNESS", "Warning sign detection, recovery planning, and boundary setting. $19", "#"),
            ("Career Transition Roadmap", "CAREER", "Skills audit, market mapping, and 90-day transition action plan. $19", "#"),
            ("Leadership Competency Map", "LEADERS", "Competency definition, self-assessment, and development pathway. $19", "#"),
            ("Presentation Skills Builder", "SKILLS", "Structure, storytelling, slide design, and delivery coaching. $19", "#"),
            ("Feedback Delivery Framework", "COMMUNICATION", "SBI model, preparation checklist, and follow-through tracker. $19", "#"),
            ("Mindset Re-framing Exercise", "PSYCHOLOGY", "Limiting belief identification, evidence gathering, and new narrative. $19", "#"),
            ("Team Dynamics Diagnostic", "TEAMS", "Belbin-style role mapping, friction analysis, and collaboration plan. $19", "#"),
            ("Coaching Business Metrics", "ANALYTICS", "Revenue, utilization, retention, NPS, and pipeline tracking. $19", "#"),
        ]
    },
    "schools-education": {
        "title": "Schools \u0026 Education",
        "tagline": "Admissions funnel, lesson plans, timetables, parent communication, student progress tracking, and exam preparation — 25 skills for educators and institutions.",
        "skills": [
            ("Admissions Funnel Builder", "ENROLLMENT", "Inquiry-to-enrollment pipeline with touchpoints, events, and conversion tracking. $19", "#"),
            ("Lesson Plan Generator", "TEACHING", "Objective, activity, assessment, differentiation, and resource planning. $19", "#"),
            ("Timetable Optimizer", "SCHEDULE", "Teacher availability, room constraints, subject balance, and clash resolution. $19", "#"),
            ("Parent Communication Log", "ENGAGEMENT", "Incident reports, progress updates, and meeting summaries by student. $19", "#"),
            ("Student Progress Report", "ASSESSMENT", "Grade trends, skill mastery, behavior notes, and improvement targets. $19", "#"),
            ("Exam Paper Generator", "ASSESSMENT", "Question bank selection, difficulty balancing, answer key, and rubric. $19", "#"),
            ("Substitute Teacher Brief", "COVER", "Class profile, lesson plan, behavior notes, and emergency contacts. $19", "#"),
            ("Field Trip Risk Assessment", "SAFETY", "Hazards, mitigation, consent forms, and emergency procedures. $19", "#"),
            ("Special Needs IEP Planner", "SEN", "Goals, accommodations, progress monitoring, and stakeholder reviews. $19", "#"),
            ("Staff Appraisal Template", "HR", "Performance criteria, evidence collection, feedback, and development goals. $19", "#"),
            ("Budget Request Builder", "FINANCE", "Need justification, cost breakdown, vendor comparison, and ROI projection. $19", "#"),
            ("School Marketing Brochure", "MARKETING", "Value proposition, program highlights, testimonials, and enrollment CTA. $19", "#"),
            ("Alumni Engagement Plan", "RELATIONS", "Database segmentation, event calendar, and donation campaign strategy. $19", "#"),
            ("Library Catalog Update", "RESOURCES", "Acquisition, classification, weeding, and lending analytics. $19", "#"),
            ("Canteen Menu Planner", "OPERATIONS", "Nutritional balance, dietary restrictions, supplier rotation, and waste tracking. $19", "#"),
            ("Transport Route Optimizer", "LOGISTICS", "Stop sequencing, capacity management, and parent notification. $19", "#"),
            ("Anti-Bullying Action Plan", "SAFEGUARD", "Policy drafting, reporting mechanism, intervention steps, and monitoring. $19", "#"),
            ("Professional Development Plan", "TRAINING", "Teacher skills gap, course matching, budget, and certification tracking. $19", "#"),
            ("Open Day Event Planner", "EVENTS", "Logistics, tours, presentations, registration, and follow-up nurturing. $19", "#"),
            ("Attendance Intervention Tracker", "BEHAVIOR", "Absence pattern analysis, early-warning flags, and parent contact. $19", "#"),
            ("Curriculum Gap Analysis", "ACADEMIC", "Standard mapping, coverage audit, and resource acquisition plan. $19", "#"),
            ("Parent Teacher Meeting Prep", "MEETINGS", "Agenda, talking points, data packets, and action note templates. $19", "#"),
            ("Graduation Ceremony Script", "EVENTS", "Program flow, speaker notes, award sequences, and photography plan. $19", "#"),
            ("IT Acceptable Use Policy", "POLICY", "Device rules, internet safety, consequences, and parent consent. $19", "#"),
            ("Accreditation Readiness Pack", "COMPLIANCE", "Self-study, evidence folder, visit prep, and post-visit action. $19", "#"),
        ]
    },
    "consultancy": {
        "title": "Consultancy",
        "tagline": "RFP drafting, vendor evaluation, workshop design, deliverable templates, engagement tracking, and proposal writing — 25 skills for consulting firms and independent consultants.",
        "skills": [
            ("RFP Response Builder", "BIDS", "Executive summary, approach, team, timeline, and pricing for any RFP. $19", "#"),
            ("Vendor Evaluation Matrix", "PROCUREMENT", "Scoring criteria, weighting, comparison table, and recommendation memo. $19", "#"),
            ("Workshop Agenda Designer", "FACILITATION", "Objectives, exercises, timing, materials, and debrief for client workshops. $19", "#"),
            ("SOW \u0026 Scope Document", "CONTRACT", "Deliverables, exclusions, assumptions, timeline, and change-control clause. $19", "#"),
            ("Client Stakeholder Map", "ANALYSIS", "Power/interest grid, influence channels, and engagement strategy. $19", "#"),
            ("Deliverable QA Checklist", "QUALITY", "Structure, evidence, formatting, branding, and peer-review gates. $19", "#"),
            ("Engagement Tracking Dashboard", "OPS", "Hours, milestones, budget burn, risks, and client satisfaction by project. $19", "#"),
            ("Kickoff Meeting Runbook", "START", "Attendees, agenda, decision log, RACI, and communication protocol. $19", "#"),
            ("Change Request Template", "CONTROL", "Impact assessment, pricing, timeline, and approval workflow. $19", "#"),
            ("Risk Register Builder", "RISK", "Identification, probability, impact, mitigation, and owner assignment. $19", "#"),
            ("Executive Presentation Pack", "DECK", "Situation, complication, resolution, recommendation, and next steps. $19", "#"),
            ("Benchmarking Study Design", "RESEARCH", "Peer selection, metric definition, data collection, and gap analysis. $19", "#"),
            ("Interview Protocol Builder", "FIELD", "Questions, probing guides, note-taking template, and synthesis framework. $19", "#"),
            ("Process Mapping Guide", "ANALYSIS", "As-is, pain points, to-be, and implementation roadmap. $19", "#"),
            ("Business Case Calculator", "FINANCE", "NPV, IRR, payback, sensitivity, and scenario comparison. $19", "#"),
            ("Training Needs Analysis", "LEARNING", "Skills audit, gap prioritization, curriculum design, and delivery plan. $19", "#"),
            ("Post-Engagement Review", "CLOSE", "Objectives vs outcomes, lessons learned, and follow-up opportunities. $19", "#"),
            ("Thought Leadership Article", "CONTENT", "Angle, outline, evidence, narrative, and publication strategy. $19", "#"),
            ("Capability Maturity Assessment", "DIAGNOSTIC", "Level definitions, evidence gathering, and improvement roadmap. $19", "#"),
            ("Competitive Landscape Map", "STRATEGY", "Player profiles, positioning, strengths, weaknesses, and white space. $19", "#"),
            ("Project Closure Report", "CLOSE", "Scope delivered, variances, handover, and archive checklist. $19", "#"),
            ("Retainer Proposal Template", "SALES", "Scope, hours, response time, deliverables, and renewal terms. $19", "#"),
            ("Knowledge Transfer Plan", "HANDOFF", "Documentation, shadowing, reverse shadowing, and sign-off criteria. $19", "#"),
            ("Client NPS Pulse", "FEEDBACK", "Questionnaire, trend analysis, action planning, and close-loop process. $19", "#"),
            ("Consulting Rate Calculator", "FINANCE", "Cost-plus, value-based, and market-comparable pricing with justification. $19", "#"),
        ]
    },
    "healthcare": {
        "title": "Healthcare \u0026 Medical",
        "tagline": "Patient intake, compliance checklists, clinical documentation, medical billing workflows, and appointment scheduling — 25 skills for healthcare providers.",
        "skills": [
            ("Patient Intake Form Builder", "FRONT", "Demographics, history, consent, insurance, and emergency contact capture. $19", "#"),
            ("HIPAA Compliance Audit", "COMPLIANCE", "Privacy, security, breach response, and staff training verification. $19", "#"),
            ("Clinical Note Template", "CLINICAL", "SOAP, DAP, or BIRP formatted notes with coding guidance. $19", "#"),
            ("Medical Billing Code Checker", "BILLING", "CPT/ICD-10 lookup, modifier guidance, and denial prevention. $19", "#"),
            ("Appointment Scheduling Optimizer", "OPS", "Slot allocation, no-show prediction, and reminder sequences. $19", "#"),
            ("Informed Consent Document", "LEGAL", "Procedure explanation, risks, alternatives, and signature capture. $19", "#"),
            ("Discharge Summary Writer", "CLINICAL", "Admission reason, treatment, condition at discharge, and follow-up plan. $19", "#"),
            ("Insurance Verification Check", "FINANCE", "Eligibility, benefits, pre-auth, and referral requirement confirmation. $19", "#"),
            ("Medication Adherence Tracker", "PHARMACY", "Refill patterns, side-effect monitoring, and intervention triggers. $19", "#"),
            ("Telehealth Prep Checklist", "REMOTE", "Tech test, privacy, lighting, and documentation setup for virtual visits. $19", "#"),
            ("Infection Control Protocol", "SAFETY", "PPE, sterilization, exposure response, and reporting requirements. $19", "#"),
            ("Staff Credential Tracker", "HR", "License expiry, CEU completion, and renewal alert system. $19", "#"),
            ("Patient Satisfaction Survey", "QA", "Visit experience, communication, wait time, and recommendation scoring. $19", "#"),
            ("Medical Equipment Maintenance", "OPS", "Schedule, calibration, repair log, and replacement planning. $19", "#"),
            ("Referral Letter Generator", "CLINICAL", "History, findings, reason for referral, and urgency indication. $19", "#"),
            ("Emergency Response Drill Plan", "SAFETY", "Code blue, fire, evacuation, and mass casualty scenarios with roles. $19", "#"),
            ("Patient Education Handout", "EDUCATION", "Condition, treatment, self-care, warning signs, and follow-up in plain language. $19", "#"),
            ("Quality Indicator Dashboard", "ANALYTICS", "Readmission, infection rate, mortality, and patient safety metrics. $19", "#"),
            ("Lab Result Communication", "CLINICAL", "Normal, abnormal, and critical value notification scripts with next steps. $19", "#"),
            ("Vaccination Schedule Planner", "PREVENTION", "Adult and pediatric immunization calendars with reminder logic. $19", "#"),
            ("Surgical Pre-op Checklist", "SURGERY", "Consent, fasting, meds, allergies, and anesthesia readiness verification. $19", "#"),
            ("Chronic Care Plan", "MANAGEMENT", "Diabetes, hypertension, or asthma — monitoring, medication, and lifestyle. $19", "#"),
            ("Incident Report Form", "RISK", "Event description, witnesses, immediate action, and root cause analysis. $19", "#"),
            ("Healthcare Marketing Brief", "GROWTH", "Service launch, patient acquisition, and community outreach campaign. $19", "#"),
            ("Regulatory Filing Calendar", "COMPLIANCE", "MOH, DHA, HAAD, JCI deadlines with document prep and submission. $19", "#"),
        ]
    },
    "legal": {
        "title": "Legal \u0026 Law",
        "tagline": "Contract review, clause analysis, legal briefs, compliance tracking, and case preparation tools — 25 skills for law firms and legal teams.",
        "skills": [
            ("NDA Review Checklist", "CONTRACT", "Confidentiality scope, term, survival, and mutual vs one-way analysis. $19", "#"),
            ("Employment Contract Analyzer", "HR", "Probation, termination, non-compete, IP assignment, and dispute clause. $19", "#"),
            ("Regulatory Compliance Calendar", "COMPLIANCE", "Filing deadlines, responsible party, and document checklist by jurisdiction. $19", "#"),
            ("Litigation Timeline Builder", "LITIGATION", "Pleadings, discovery, motions, trial, and appeal milestones with dates. $19", "#"),
            ("Deposition Prep Script", "LITIGATION", "Witness background, anticipated questions, and document exhibits. $19", "#"),
            ("Legal Memo Template", "DRAFTING", "Issue, facts, analysis, conclusion, and recommendation structure. $19", "#"),
            ("Due Diligence Checklist", "TRANSACTION", "Corporate, financial, IP, employment, and litigation review items. $19", "#"),
            ("Cease \u0026 Desist Letter", "DISPUTE", "Infringement identification, demand, deadline, and consequence statement. $19", "#"),
            ("Trademark Search Brief", "IP", "Class identification, conflict assessment, and registration strategy. $19", "#"),
            ("Privacy Policy Drafter", "COMPLIANCE", "GDPR, CCPA, UAE PDPL aligned collection, use, and rights language. $19", "#"),
            ("Shareholders' Agreement Review", "CORPORATE", "Voting, drag-along, tag-along, deadlock, and exit provisions. $19", "#"),
            ("Power of Attorney Template", "DOCUMENT", "Scope, duration, revocation, and notarization requirements by jurisdiction. $19", "#"),
            ("Arbitration Clause Builder", "ADR", "Seat, rules, panel size, language, and enforcement mechanism. $19", "#"),
            ("Risk Assessment Matrix", "ADVISORY", "Legal risk identification, probability, impact, and mitigation recommendations. $19", "#"),
            ("Board Resolution Drafter", "CORPORATE", "Purpose, background, resolved clauses, and signature blocks. $19", "#"),
            ("Lease Agreement Reviewer", "REAL", "Term, rent, maintenance, subletting, termination, and renewal provisions. $19", "#"),
            ("Evidence Index Organizer", "LITIGATION", "Exhibit numbering, description, source, and admissibility notes. $19", "#"),
            ("Settlement Agreement Template", "DISPUTE", "Recitals, terms, consideration, release, and confidentiality. $19", "#"),
            ("Anti-Bribery Policy", "COMPLIANCE", "FCPA, UK Bribery Act, and local law aligned gifts, hospitality, and reporting. $19", "#"),
            ("Client Intake Form", "PRACTICE", "Matter details, conflict check, fee arrangement, and engagement letter trigger. $19", "#"),
            ("Legal Spend Tracker", "OPS", "Matter budgets, time recording, AFA comparison, and client reporting. $19", "#"),
            ("Contract Amendment Drafter", "CONTRACT", "Change description, original reference, new terms, and execution. $19", "#"),
            ("Wills \u0026 Probate Checklist", "PRIVATE", "Assets, beneficiaries, executor, guardians, and probate timeline. $19", "#"),
            ("Subpoena Response Guide", "LITIGATION", "Objection grounds, privilege review, and production protocol. $19", "#"),
            ("Legal Team KPI Dashboard", "ANALYTICS", "Matter volume, cycle time, realization rate, and client satisfaction. $19", "#"),
        ]
    },
    "construction": {
        "title": "Construction \u0026 Engineering",
        "tagline": "Project scheduling, safety compliance, vendor management, build quality checklists, and cost estimation — 25 skills for construction firms and engineering teams.",
        "skills": [
            ("Project Schedule Builder", "PLAN", "Gantt chart, critical path, milestones, and resource loading with float analysis. $19", "#"),
            ("Site Safety Audit Checklist", "HSE", "PPE, scaffolding, electrical, excavation, and fire safety inspection items. $19", "#"),
            ("Subcontractor Evaluation", "PROCUREMENT", "Pre-qualification, financial health, past performance, and reference checks. $19", "#"),
            ("Material Procurement Plan", "SUPPLY", "BOQ, vendor shortlist, lead times, and inventory buffer calculation. $19", "#"),
            ("Progress Reporting Template", "REPORT", "Percentage complete, photos, issues, risks, and next period lookahead. $19", "#"),
            ("Punch List Manager", "CLOSE", "Defect identification, responsible party, deadline, and sign-off tracking. $19", "#"),
            ("Permit Tracking System", "COMPLIANCE", "Municipal, environmental, and utility permits with expiry and renewal alerts. $19", "#"),
            ("Cost Estimation Worksheet", "FINANCE", "Labor, material, equipment, overhead, and contingency with rate justification. $19", "#"),
            ("RFI \u0026 Submittal Log", "DOCS", "Request log, response tracking, approval status, and impact on schedule. $19", "#"),
            ("Change Order Processor", "VARIANCE", "Scope change, cost impact, schedule impact, and approval workflow. $19", "#"),
            ("Daily Field Report", "OPS", "Weather, crew count, work completed, issues, and safety incidents. $19", "#"),
            ("Quality Control Plan", "QA", "Inspection points, testing frequency, acceptance criteria, and non-conformance handling. $19", "#"),
            ("Equipment Maintenance Log", "ASSETS", "Service schedule, downtime record, spare parts, and replacement forecast. $19", "#"),
            ("Environmental Compliance Plan", "HSE", "Waste, emissions, noise, and erosion controls with monitoring schedule. $19", "#"),
            ("As-Built Drawing Log", "DOCS", "Revision tracking, approval, distribution, and archive protocol. $19", "#"),
            ("Worker Induction Pack", "HR", "Site rules, hazards, emergency procedures, and PPE requirements. $19", "#"),
            ("Snag List Prioritizer", "CLOSE", "Severity scoring, trade assignment, and client inspection scheduling. $19", "#"),
            ("Value Engineering Review", "OPTIMIZE", "Alternative material, method, or design with cost-benefit analysis. $19", "#"),
            ("Warranty Handover Pack", "CLOSE", "Defect liability period, warranty certificates, and maintenance manual. $19", "#"),
            ("Subsurface Investigation Brief", "GEOTECH", "Borehole log, soil report, and foundation recommendation summary. $19", "#"),
            ("Traffic Management Plan", "SAFETY", "Diversion, signage, pedestrian access, and approval from authorities. $19", "#"),
            ("Claim \u0026 Variation Builder", "COMMERCIAL", "EOT, disruption, and prolongation claim with supporting evidence. $19", "#"),
            ("Commissioning Checklist", "MECH", "System tests, performance verification, and handover to operations. $19", "#"),
            ("Stakeholder Communication Plan", "COMMS", "Client, consultant, authority, and community update schedule. $19", "#"),
            ("Project Closeout Report", "CLOSE", "Final cost, schedule, quality, lessons, and archive index. $19", "#"),
        ]
    },
    "logistics": {
        "title": "Logistics \u0026 Supply Chain",
        "tagline": "Route optimization, inventory tracking, freight documentation, warehouse operations, and customs compliance — 25 skills for logistics teams.",
        "skills": [
            ("Route Optimization Engine", "TRANSPORT", "Multi-stop sequencing, fuel cost, time windows, and vehicle capacity. $19", "#"),
            ("Inventory Reorder Calculator", "WAREHOUSE", "EOQ, safety stock, lead time, and reorder point by SKU. $19", "#"),
            ("Freight Quote Comparator", "PROCUREMENT", "FCL, LCL, air, and road rates with transit time and reliability scoring. $19", "#"),
            ("Customs Declaration Guide", "COMPLIANCE", "HS code lookup, duty calculation, and document checklist by country. $19", "#"),
            ("Warehouse Slotting Plan", "LAYOUT", "Velocity-based location, pick-path reduction, and space utilization. $19", "#"),
            ("Shipment Tracking Dashboard", "VISIBILITY", "Carrier integration, milestone alerts, and exception escalation. $19", "#"),
            ("Packing List Generator", "DOCS", "Itemized contents, weights, dimensions, and handling instructions. $19", "#"),
            ("Last-Mile Delivery Optimizer", "DELIVERY", "Driver territory, drop density, and customer time-slot preference. $19", "#"),
            ("Freight Insurance Claim", "RISK", "Damage documentation, carrier liability, and insurer submission pack. $19", "#"),
            ("Vendor Scorecard Builder", "PROCUREMENT", "On-time, quality, cost, and responsiveness scoring with quarterly review. $19", "#"),
            ("Cross-Docking Schedule", "OPS", "Inbound-outbound matching, dock door assignment, and labor planning. $19", "#"),
            ("Reverse Logistics SOP", "RETURNS", "Return authorization, inspection, disposition, and refund trigger. $19", "#"),
            ("Cold Chain Compliance", "PHARMA", "Temperature mapping, logger placement, and excursion response. $19", "#"),
            ("3PL Contract Reviewer", "LEGAL", "SLA, KPI, liability, termination, and performance guarantee clauses. $19", "#"),
            ("Demand Forecast Model", "PLANNING", "Historical trend, seasonality, promotion lift, and safety stock. $19", "#"),
            ("Container Load Plan", "OPS", "Carton dimensions, weight distribution, and lash-free stowage optimization. $19", "#"),
            ("Delivery Proof Collector", "LAST", "Photo, signature, geotag, and timestamp for POD verification. $19", "#"),
            ("Import Duty Optimizer", "TAX", "FTA utilization, tariff engineering, and bonded warehouse strategy. $19", "#"),
            ("Fleet Maintenance Schedule", "FLEET", "Service intervals, inspection checklist, and downtime minimization. $19", "#"),
            ("Warehouse KPI Dashboard", "ANALYTICS", "Pick accuracy, inventory accuracy, dock-to-stock, and cost per unit. $19", "#"),
            ("Dangerous Goods Shipper", "HAZMAT", "Classification, packaging, labeling, and emergency response guide. $19", "#"),
            ("Supplier Audit Checklist", "QUALITY", "Facility, process, documentation, and corrective action tracking. $19", "#"),
            ("Multi-Modal Shipment Planner", "INTL", "Sea-air-land combination for cost-time optimization and carbon reduction. $19", "#"),
            ("Logistics RFP Builder", "PROCUREMENT", "Scope, volume, lanes, SLA, and evaluation criteria for 3PL tender. $19", "#"),
            ("Sustainability Reporting", "ESG", "Emissions per shipment, modal shift, and packaging waste metrics. $19", "#"),
        ]
    },
    "hospitality": {
        "title": "Hospitality \u0026 Tourism",
        "tagline": "Guest experience, booking workflows, event planning, F\u0026B operations, and concierge services — 25 skills for hotels, restaurants, and travel businesses.",
        "skills": [
            ("Guest Feedback Analyzer", "QA", "Review aggregation, sentiment scoring, and issue-to-department routing. $19", "#"),
            ("Menu Engineering Worksheet", "F\u0026B", "Popularity-profit matrix, price elasticity, and contribution margin optimization. $19", "#"),
            ("Banquet Event Order", "EVENTS", "Menu, timing, room setup, AV, and staffing requirements by event. $19", "#"),
            ("Loyalty Program Design", "RETENTION", "Tier structure, earn-burn rates, benefits, and redemption catalog. $19", "#"),
            ("OTA Listing Optimizer", "DISTRIBUTION", "Title, photos, amenities, rate parity, and review response strategy. $19", "#"),
            ("Excursion Itinerary Builder", "TOURS", "Route, timing, inclusions, exclusions, and emergency plan. $19", "#"),
            ("Front Desk SOP", "OPS", "Check-in, checkout, complaint handling, and VIP recognition procedures. $19", "#"),
            ("Housekeeping Inspection", "ROOMS", "Cleanliness, maintenance, minibar, and amenities check with scoring. $19", "#"),
            ("Revenue Management Model", "REVENUE", "ADR, occupancy, RevPAR, and dynamic pricing by segment and season. $19", "#"),
            ("Staff Roster Optimizer", "HR", "Forecast-based scheduling, break rules, and overtime control. $19", "#"),
            ("Guest Complaint Recovery", "SERVICE", "Acknowledgment, empathy, resolution, compensation, and follow-up. $19", "#"),
            ("Wine List Curator", "F\u0026B", "By-the-glass and bottle selection, pricing, pairing, and inventory turn. $19", "#"),
            ("Spa Treatment Menu", "WELLNESS", "Treatment descriptions, duration, pricing, and therapist assignment. $19", "#"),
            ("Wedding Package Builder", "EVENTS", "Ceremony, reception, catering, decor, and vendor coordination. $19", "#"),
            ("Corporate Rate Negotiator", "SALES", "Volume commitment, rate structure, and inclusion negotiation. $19", "#"),
            ("Health \u0026 Safety Audit", "COMPLIANCE", "Kitchen, pool, gym, and room safety inspection with remediation. $19", "#"),
            ("Concierge Request Log", "SERVICE", "Booking, confirmation, reminder, and satisfaction follow-up tracking. $19", "#"),
            ("Seasonal Promotion Planner", "MARKETING", "Theme, offer, channel, timing, and revenue target by season. $19", "#"),
            ("Lost \u0026 Found Process", "OPS", "Item logging, guest notification, storage, and disposal protocol. $19", "#"),
            ("Valet Parking SOP", "OPS", "Vehicle log, damage inspection, key security, and retrieval workflow. $19", "#"),
            ("Restaurant Reservation Flow", "F\u0026B", "Booking, confirmation, waitlist, seating, and no-show policy. $19", "#"),
            ("Sustainability Action Plan", "ESG", "Energy, water, waste, and community initiatives with guest communication. $19", "#"),
            ("Guest Room Upgrade Strategy", "REVENUE", "Availability-based upsell, loyalty recognition, and special occasion. $19", "#"),
            ("Night Audit Checklist", "FINANCE", "Revenue reconciliation, cashier audit, and end-of-day reports. $19", "#"),
            ("Mystery Shopper Brief", "QA", "Evaluation criteria, scenario script, and scoring rubric for secret audits. $19", "#"),
        ]
    },
    "it-devops": {
        "title": "IT \u0026 DevOps",
        "tagline": "Infrastructure monitoring, incident response, CI/CD pipelines, security compliance, and cloud resource management — 25 skills for tech teams.",
        "skills": [
            ("Runbook Generator", "SRE", "Step-by-step incident response procedures with commands, checks, and escalation. $19", "#"),
            ("On-Call Rotation Planner", "SRE", "Schedule builder, handoff notes, and escalation matrix with timezone support. $19", "#"),
            ("SRE Dashboard Blueprint", "MONITOR", "SLI, SLO, error budget, burn rate, and alert threshold design. $19", "#"),
            ("Security Scan Report", "SEC", "Vulnerability summary, CVSS scoring, remediation priority, and timeline. $19", "#"),
            ("Cost Optimization Audit", "FINANCE", "Unused resources, right-sizing, reserved instance, and savings plan analysis. $19", "#"),
            ("Deployment Risk Assessment", "DEPLOY", "Change scope, blast radius, rollback plan, and go/no-go checklist. $19", "#"),
            ("Post-Mortem Template", "INCIDENT", "Timeline, impact, root cause, action items, and follow-up tracking. $19", "#"),
            ("CI/CD Pipeline Design", "AUTOMATION", "Build, test, scan, deploy, and rollback stages with tool selection. $19", "#"),
            ("Disaster Recovery Plan", "DR", "RTO, RPO, backup verification, failover test, and communication plan. $19", "#"),
            ("Access Control Review", "SEC", "Role matrix, privilege audit, offboarding checklist, and periodic recertification. $19", "#"),
            ("Cloud Migration Planner", "MIGRATE", "Assessment, pilot, cutover, and optimization phases with risk mitigation. $19", "#"),
            ("Database Performance Tuner", "DBA", "Query analysis, index recommendation, and connection pool optimization. $19", "#"),
            ("Kubernetes Manifest Review", "K8S", "Resource limits, health checks, security context, and best practice. $19", "#"),
            ("Log Analysis Query Builder", "OBS", "Search, aggregation, anomaly detection, and correlation queries. $19", "#"),
            ("SSL Certificate Tracker", "SEC", "Expiry monitoring, renewal procedure, and SAN verification. $19", "#"),
            ("Load Testing Scenario", "PERF", "Concurrency, throughput, latency, and error rate targets with JMeter/k6 script. $19", "#"),
            ("Infrastructure-as-Code Review", "IAC", "Terraform/CloudFormation linting, state management, and module design. $19", "#"),
            ("Penetration Test Brief", "SEC", "Scope, methodology, tools, timeline, and report template. $19", "#"),
            ("API Documentation Template", "DEV", "Endpoint, method, auth, request, response, and error specification. $19", "#"),
            ("Service Dependency Map", "ARCH", "Upstream, downstream, critical path, and failure impact visualization. $19", "#"),
            ("Backup Verification Script", "OPS", "Restore test, integrity check, and retention compliance validation. $19", "#"),
            ("Network Troubleshooter", "NET", "Ping, traceroute, DNS, firewall, and routing diagnosis with resolution. $19", "#"),
            ("Change Advisory Board Pack", "GOVERN", "Change description, risk, test evidence, and approval request. $19", "#"),
            ("Tech Debt Register", "PLAN", "Item, impact, effort, priority, and quarterly reduction target. $19", "#"),
            ("Incident Communication Template", "COMMS", "Status page update, stakeholder notification, and post-resolution summary. $19", "#"),
        ]
    },
    "personal-productivity": {
        "title": "Personal Productivity",
        "tagline": "Daily briefs, email triage, meeting prep, calendar optimization, and focus-time protection — 25 skills for executives and individuals.",
        "skills": [
            ("Daily Brief Generator", "PLAN", "Priority extraction, schedule scan, and top-3 focus from calendar and tasks. $19", "#"),
            ("Eisenhower Matrix Sorter", "PRIORITY", "Urgent-important classification, delegation suggestions, and elimination. $19", "#"),
            ("Meeting Prep Dossier", "MEETINGS", "Attendees, agenda, pre-reads, decisions needed, and follow-up actions. $19", "#"),
            ("Calendar Optimization Audit", "TIME", "Meeting density analysis, focus block creation, and boundary enforcement. $19", "#"),
            ("Email Triage System", "INBOX", "2-minute rule, delegate, defer, and delete decision tree with templates. $19", "#"),
            ("Travel Itinerary Builder", "TRAVEL", "Flights, hotels, ground transport, and buffer time with contingency. $19", "#"),
            ("Expense Report Compiler", "FINANCE", "Receipt capture, categorization, policy check, and submission formatting. $19", "#"),
            ("Delegation Planner", "TEAM", "Task assessment, candidate matching, briefing, and checkpoint schedule. $19", "#"),
            ("Weekly Review Framework", "REFLECT", "Wins, misses, learnings, and next-week intention setting. $19", "#"),
            ("Focus Session Timer", "DEEP", "Pomodoro, break schedule, distraction list, and session goal. $19", "#"),
            ("Personal OKR Tracker", "GOALS", "Quarterly objective, key results, weekly initiatives, and confidence scoring. $19", "#"),
            ("Networking Follow-Up Log", "RELATIONS", "Contact recency, conversation notes, and re-engagement triggers. $19", "#"),
            ("Decision Journal Template", "THINK", "Context, options, criteria, choice, expected outcome, and later review. $19", "#"),
            ("Morning Routine Designer", "HABIT", "Energy, focus, and mood optimization with timing and buffer. $19", "#"),
            ("Note-Taking System Setup", "KNOW", "PARA, Zettelkasten, or bullet journal structure with tool selection. $19", "#"),
            ("Side Project Planner", "PROJECT", "Scope, time allocation, milestone, and resource plan for personal ventures. $19", "#"),
            ("Digital Declutter Guide", "ORG", "File structure, naming convention, archive, and backup automation. $19", "#"),
            ("Boundary Setting Script", "COMM", "Declining, deferring, and negotiating requests with respect and clarity. $19", "#"),
            ("Learning Path Designer", "GROW", "Skill gap, resource curation, practice schedule, and milestone assessment. $19", "#"),
            ("Energy Audit Tracker", "WELLNESS", "Peak hours, drain identification, and recovery protocol optimization. $19", "#"),
            ("Password Security Review", "SEC", "Manager audit, 2FA check, and breach exposure scan. $19", "#"),
            ("Subscription Optimizer", "FINANCE", "Usage review, duplicate detection, and cancellation or downgrade plan. $19", "#"),
            ("Gift \u0026 Occasion Reminder", "RELATIONS", "Birthday, anniversary, and special event calendar with gift suggestions. $19", "#"),
            ("Personal Brand Builder", "MARKET", "LinkedIn bio, content pillars, posting cadence, and engagement strategy. $19", "#"),
            ("End-of-Day Shutdown Ritual", "CLOSE", "Inbox zero, tomorrow preview, gratitude, and device boundaries. $19", "#"),
        ]
    },
    "health-fitness": {
        "title": "Health \u0026 Fitness",
        "tagline": "Workout planning, nutrition tracking, wellness coaching, biometric monitoring, and habit formation — 25 skills for wellness professionals and individuals.",
        "skills": [
            ("Periodized Training Plan", "TRAIN", "Macro, meso, micro cycles with volume, intensity, and recovery by sport. $19", "#"),
            ("Meal Plan Generator", "NUTRITION", "Calorie target, macro split, grocery list, and prep schedule by dietary preference. $19", "#"),
            ("Recovery Protocol Designer", "RECOVER", "Sleep, mobility, massage, ice, and active recovery scheduling. $19", "#"),
            ("Supplement Stack Tracker", "NUTRITION", "Dosing, timing, interactions, and blood marker correlation. $19", "#"),
            ("Biometric Trend Analyzer", "DATA", "Weight, body fat, HRV, sleep, and performance trend visualization. $19", "#"),
            ("Accountability Coaching Check-In", "COACH", "Weekly goal review, obstacle troubleshooting, and next-week commitment. $19", "#"),
            ("Injury Prevention Screening", "PREVENT", "Movement assessment, asymmetry detection, and corrective exercise plan. $19", "#"),
            ("Race Day Strategy Builder", "EVENT", "Pacing, nutrition, hydration, and mental preparation for marathon or triathlon. $19", "#"),
            ("Body Composition Planner", "AESTHETIC", "Cut, maintain, or bulk phases with calorie adjustment and progress photos. $19", "#"),
            ("Home Gym Setup Guide", "EQUIP", "Space, budget, equipment selection, and workout program for limited space. $19", "#"),
            ("Group Class Choreographer", "GROUP", "Music, sequence, intensity peaks, and modifications by fitness level. $19", "#"),
            ("Nutrition Label Decoder", "EDU", "Serving size, macro, ingredient quality, and health claim evaluation. $19", "#"),
            ("Sleep Hygiene Optimizer", "SLEEP", "Routine, environment, blue light, caffeine, and nap protocol. $19", "#"),
            ("Stress Resilience Plan", "MIND", "Breathing, meditation, nature, and social connection prescriptions. $19", "#"),
            ("Yoga Sequence Builder", "MOBILITY", "Warm-up, peak pose, counter pose, and relaxation with breath cues. $19", "#"),
            ("Strength PR Tracker", "LIFT", "1RM, 5RM, volume PR logging with attempt planning and safety. $19", "#"),
            ("Hydration Monitor", "HABIT", "Intake target, reminder schedule, and urine color self-assessment. $19", "#"),
            ("Mindful Eating Guide", "BEHAVIOR", "Hunger scale, eating speed, distraction reduction, and satiety awareness. $19", "#"),
            ("Desk Worker Mobility Plan", "CORRECT", "Neck, shoulder, hip, and wrist routines for sedentary professionals. $19", "#"),
            ("Wellness Retreat Itinerary", "EVENT", "Activities, meals, workshops, and downtime balance for group retreats. $19", "#"),
            ("Gym Newbie Orientation", "ONBOARD", "Etiquette, equipment intro, basic program, and confidence building. $19", "#"),
            ("Heart Rate Zone Calculator", "CARDIO", "Max HR, resting HR, zone definitions, and training allocation. $19", "#"),
            ("Meal Prep Sunday Planner", "NUTRITION", "Batch recipes, storage, portioning, and weekly rotation schedule. $19", "#"),
            ("Progress Photo Protocol", "TRACK", "Lighting, pose, frequency, and comparison guidelines for visual tracking. $19", "#"),
            ("Wellness Business Launch Kit", "ENTREPRENEUR", "Niche, pricing, packages, marketing, and liability for coaches. $19", "#"),
        ]
    },
}

# ============================================================
# HTML TEMPLATE
# ============================================================

def build_page(slug, data):
    title = data["title"]
    tagline = data["tagline"]
    skills = data["skills"]
    
    # Extract unique categories for filter buttons
    categories = sorted(set([s[1] for s in skills]))
    
    filters_html = ""
    for cat in categories:
        filters_html += f'\u003cbutton data-filter="{cat.lower()}"\u003e{cat}\u003c/button\u003e\n'
    
    cards_html = ""
    for name, cat, desc, href in skills:
        cards_html += f'''\u003ca href="{href}" class="skill-card" data-category="{cat.lower()}"\u003e
\u003cdiv class="skill-badge"\u003e{cat}\u003c/div\u003e
\u003ch3\u003e{name}\u003c/h3\u003e
\u003cp\u003e{desc}\u003c/p\u003e
\u003cdiv class="skill-meta"\u003e\u003cspan class="price"\u003e\u003c/span\u003e\u003cspan class="run"\u003eRun →\u003c/span\u003e\u003c/div\u003e
\u003c/a\u003e\n'''
    
    html = f'''\u003c!DOCTYPE html\u003e
\u003chtml lang="en"\u003e
\u003chead\u003e\u003cmeta charset="utf-8"\u003e\u003cmeta name="viewport" content="width=device-width, initial-scale=1"\u003e
\u003ctitle\u003ePandora's Skill Box — {title} Collection\u003c/title\u003e
\u003clink href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1\u0026family=Schibsted+Grotesk:wght@400;500;600;700\u0026family=Spline+Sans+Mono:wght@400;500\u0026display=swap" rel="stylesheet"\u003e
\u003cstyle\u003e:root{{--ink:#0B2E29;--ink-deep:#072320;--porcelain:#F4F6F2;--paper:#FBFCFA;--brass:#B8892D;--brass-soft:#E4C878;--muted:#5C6F6A;--verdict:#17A673;--flag:#D64533;--font-display:'Instrument Serif',Georgia,serif;--font-body:'Schibsted Grotesk',system-ui,sans-serif;--font-mono:'Spline Sans Mono',monospace;}}
*{{box-sizing:border-box;margin:0;padding:0}}html{{scroll-behavior:smooth}}
body{{font-family:var(--font-body);background:var(--paper);color:var(--ink);line-height:1.6}}
nav{{position:fixed;top:0;left:0;right:0;z-index:100;background:rgba(251,252,250,0.92);backdrop-filter:blur(12px);border-bottom:1px solid rgba(11,46,41,0.06)}}
.nav-inner{{max-width:1200px;margin:0 auto;padding:0 24px;display:flex;align-items:center;justify-content:space-between;height:64px}}
.nav-logo{{display:flex;align-items:center;gap:10px;text-decoration:none;color:var(--ink)}}
.nav-logo .seal{{width:32px;height:32px;border-radius:50%;background:var(--brass);display:flex;align-items:center;justify-content:center;color:#fff;font-size:14px;font-weight:700}}
.nav-logo span{{font-family:var(--font-display);font-size:20px}}
.nav-links{{display:flex;gap:16px;list-style:none;align-items:center}}
.nav-links a{{text-decoration:none;color:var(--muted);font-size:12px;font-weight:500;white-space:nowrap}}
.nav-links a:hover{{color:var(--ink)}}
.nav-cta{{background:var(--ink);color:#fff;padding:8px 14px;border-radius:6px;text-decoration:none;font-size:12px;font-weight:600;white-space:nowrap}}
.hero{{min-height:60vh;display:flex;align-items:center;background:var(--ink);position:relative}}
.hero::before{{content:'';position:absolute;inset:0;background:radial-gradient(ellipse at 50% 50%,rgba(184,137,45,0.08) 0%,transparent 60%)}}
.hero-inner{{max-width:800px;margin:0 auto;padding:140px 24px 60px;text-align:center;position:relative;z-index:2}}
.hero h1{{font-family:var(--font-display);font-size:clamp(32px,5vw,56px);color:var(--porcelain);line-height:1.1;margin-bottom:20px}}
.hero h1 em{{color:var(--brass-soft);font-style:italic}}
.hero p{{font-size:18px;color:rgba(244,246,242,0.7);margin-bottom:32px}}
.btn-primary{{background:var(--brass);color:#fff;padding:14px 32px;border-radius:8px;text-decoration:none;font-weight:600;font-size:15px;display:inline-block}}
.back-link{{display:inline-block;margin-top:40px;color:var(--brass-soft);text-decoration:none;font-weight:600}}
.filters{{max-width:1200px;margin:0 auto;padding:24px;display:flex;gap:10px;flex-wrap:wrap}}
.filters button{{background:var(--porcelain);border:none;padding:8px 16px;border-radius:100px;font-family:var(--font-mono);font-size:12px;color:var(--muted);cursor:pointer;transition:all 0.2s}}
.filters button:hover,.filters button.active{{background:var(--ink);color:#fff}}
.skills{{max-width:1200px;margin:0 auto;padding:0 24px 80px;display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:20px}}
.skill-card{{background:#fff;border-radius:12px;padding:24px;border:1px solid rgba(11,46,41,0.06);transition:all 0.2s;position:relative;text-decoration:none;color:inherit;display:block}}
.skill-card::after{{content:'';position:absolute;inset:0;z-index:10}}
.skill-card::before{{content:'';position:absolute;top:0;left:0;right:0;height:3px;background:var(--brass);opacity:0;transition:opacity 0.2s}}
.skill-card:hover::before{{opacity:1}}
.skill-card:hover{{transform:translateY(-2px);box-shadow:0 12px 40px rgba(11,46,41,0.06)}}
.skill-badge{{display:inline-block;background:var(--porcelain);color:var(--muted);font-family:var(--font-mono);font-size:11px;padding:4px 12px;border-radius:100px;margin-bottom:12px;text-transform:uppercase;letter-spacing:0.5px;position:relative;z-index:5;pointer-events:none}}
.skill-card h3{{font-family:var(--font-display);font-size:20px;margin-bottom:8px;color:var(--ink);position:relative;z-index:5;pointer-events:none}}
.skill-card p{{color:var(--muted);font-size:14px;margin-bottom:16px;min-height:60px;position:relative;z-index:5;pointer-events:none}}
.skill-meta{{display:flex;justify-content:space-between;align-items:center;position:relative;z-index:5;pointer-events:none}}
.skill-meta .price{{font-family:var(--font-mono);font-size:12px;color:var(--brass);font-weight:500}}
.skill-meta .run{{color:var(--brass);font-weight:600;font-size:13px}}
footer{{background:var(--ink-deep);padding:60px 24px 40px}}
.footer-inner{{max-width:1200px;margin:0 auto;display:grid;grid-template-columns:2fr 1fr 1fr 1fr;gap:40px}}
.footer-brand .seal{{width:40px;height:40px;border-radius:50%;background:var(--brass);display:flex;align-items:center;justify-content:center;color:#fff;font-size:16px;font-weight:700;margin-bottom:16px}}
.footer-brand h4{{font-family:var(--font-display);color:var(--porcelain);font-size:20px;margin-bottom:8px}}
.footer-brand p{{color:rgba(244,246,242,0.5);font-size:14px}}
.footer-col h5{{color:var(--porcelain);font-size:13px;text-transform:uppercase;letter-spacing:1px;margin-bottom:20px}}
.footer-col a{{display:block;color:rgba(244,246,242,0.5);text-decoration:none;font-size:14px;margin-bottom:12px}}
.footer-bottom{{max-width:1200px;margin:40px auto 0;padding-top:24px;border-top:1px solid rgba(244,246,242,0.08);display:flex;justify-content:space-between;color:rgba(244,246,242,0.4);font-size:12px}}
@media(max-width:768px){{.nav-links{{display:none}}.footer-inner{{grid-template-columns:1fr 1fr}}}}
\u003c/style\u003e\u003c/head\u003e
\u003cbody\u003e
\u003cnav\u003e\u003cdiv class="nav-inner"\u003e
\u003ca href="index.html" class="nav-logo"\u003e\u003cdiv class="seal"\u003eP\u003c/div\u003e\u003cspan\u003ePandora's Skill Box\u003c/span\u003e\u003c/a\u003e
\u003cul class="nav-links"\u003e
\u003cli\u003e\u003ca href="hr-solutions.html"\u003eHR\u003c/a\u003e\u003c/li\u003e
\u003cli\u003e\u003ca href="real-estate.html"\u003eReal Estate\u003c/a\u003e\u003c/li\u003e
\u003cli\u003e\u003ca href="ceo-reset.html"\u003eCEO Reset\u003c/a\u003e\u003c/li\u003e
\u003cli\u003e\u003ca href="finance-audit.html"\u003eFinance\u003c/a\u003e\u003c/li\u003e
\u003cli\u003e\u003ca href="sales.html"\u003eSales\u003c/a\u003e\u003c/li\u003e
\u003cli\u003e\u003ca href="marketing.html"\u003eMarketing\u003c/a\u003e\u003c/li\u003e
\u003cli\u003e\u003ca href="customer-support.html"\u003eSupport\u003c/a\u003e\u003c/li\u003e
\u003cli\u003e\u003ca href="coaching.html"\u003eCoaching\u003c/a\u003e\u003c/li\u003e
\u003cli\u003e\u003ca href="schools-education.html"\u003eEducation\u003c/a\u003e\u003c/li\u003e
\u003cli\u003e\u003ca href="consultancy.html"\u003eConsultancy\u003c/a\u003e\u003c/li\u003e
\u003cli\u003e\u003ca href="healthcare.html"\u003eHealthcare\u003c/a\u003e\u003c/li\u003e
\u003cli\u003e\u003ca href="legal.html"\u003eLegal\u003c/a\u003e\u003c/li\u003e
\u003cli\u003e\u003ca href="construction.html"\u003eConstruction\u003c/a\u003e\u003c/li\u003e
\u003cli\u003e\u003ca href="logistics.html"\u003eLogistics\u003c/a\u003e\u003c/li\u003e
\u003cli\u003e\u003ca href="hospitality.html"\u003eHospitality\u003c/a\u003e\u003c/li\u003e
\u003cli\u003e\u003ca href="it-devops.html"\u003eIT\u003c/a\u003e\u003c/li\u003e
\u003cli\u003e\u003ca href="personal-productivity.html"\u003eProductivity\u003c/a\u003e\u003c/li\u003e
\u003cli\u003e\u003ca href="health-fitness.html"\u003eFitness\u003c/a\u003e\u003c/li\u003e
\u003c/ul\u003e
\u003ca href="index.html" class="nav-cta"\u003e← All verticals\u003c/a\u003e
\u003c/div\u003e\u003c/nav\u003e
\u003csection class="hero"\u003e\u003cdiv class="hero-inner"\u003e
\u003ch1\u003e{title}\u003cbr\u003e\u003cem\u003e25 certified skills\u003c/em\u003e\u003c/h1\u003e
\u003cp\u003e{tagline}\u003c/p\u003e
\u003ca href="#skills" class="btn-primary"\u003eBrowse 25 skills\u003c/a\u003e
\u003cdiv\u003e\u003ca href="index.html" class="back-link"\u003e← Back to all verticals\u003c/a\u003e\u003c/div\u003e
\u003c/div\u003e\u003c/section\u003e
\u003cdiv class="filters" id="skills"\u003e{filters_html}\u003c/div\u003e
\u003cdiv class="skills"\u003e{cards_html}\u003c/div\u003e
\u003cfooter\u003e\u003cdiv class="footer-inner"\u003e
\u003cdiv class="footer-brand"\u003e\u003cdiv class="seal"\u003eP\u003c/div\u003e\u003ch4\u003ePandora's Skill Box\u003c/h4\u003e\u003cp\u003eCertified AI skills that run in your own account.\u003c/p\u003e\u003c/div\u003e
\u003cdiv class="footer-col"\u003e\u003ch5\u003eVerticals\u003c/h5\u003e\u003ca href="hr-solutions.html"\u003eHR Solutions\u003c/a\u003e\u003ca href="real-estate.html"\u003eReal Estate\u003c/a\u003e\u003ca href="ceo-reset.html"\u003eCEO Reset\u003c/a\u003e\u003ca href="finance-audit.html"\u003eFinance \u0026 Audit\u003c/a\u003e\u003ca href="sales.html"\u003eSales\u003c/a\u003e\u003ca href="marketing.html"\u003eMarketing\u003c/a\u003e\u003c/div\u003e
\u003cdiv class="footer-col"\u003e\u003ch5\u003eMore\u003c/h5\u003e\u003ca href="customer-support.html"\u003eSupport\u003c/a\u003e\u003ca href="coaching.html"\u003eCoaching\u003c/a\u003e\u003ca href="schools-education.html"\u003eEducation\u003c/a\u003e\u003ca href="consultancy.html"\u003eConsultancy\u003c/a\u003e\u003ca href="healthcare.html"\u003eHealthcare\u003c/a\u003e\u003ca href="legal.html"\u003eLegal\u003c/a\u003e\u003c/div\u003e
\u003cdiv class="footer-col"\u003e\u003ch5\u003eCompany\u003c/h5\u003e\u003ca href="index.html"\u003eHome\u003c/a\u003e\u003ca href="privacy.html"\u003ePrivacy\u003c/a\u003e\u003ca href="terms.html"\u003eTerms\u003c/a\u003e\u003c/div\u003e
\u003c/div\u003e\u003cdiv class="footer-bottom"\u003e\u003cspan\u003e© 2026 Pandora's Skill Box\u003c/span\u003e\u003cspan\u003ePandora Certified · 12-Point Security Scan\u003c/span\u003e\u003c/div\u003e\u003c/footer\u003e
\u003cscript\u003edocument.addEventListener('click',function(e){{var c=e.target.closest('.skill-card[href]');if(c){{window.location.href=c.getAttribute('href');}}}});\u003c/script\u003e
\u003c/body\u003e\u003c/html\u003e'''
    
    path = os.path.join(base, f"{slug}.html")
    with open(path, "w") as f:
        f.write(html)
    print(f"Built {slug}.html ({len(skills)} skills)")

# Build all verticals
for slug, data in verticals.items():
    build_page(slug, data)

print(f"\nDone. {len(verticals)} verticals built with {sum(len(v['skills']) for v in verticals.values())} total skills.")
