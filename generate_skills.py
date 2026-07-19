#!/usr/bin/env python3
"""
Generate all 450 skill detail pages for Pandora's Skill Box.
Each page includes: hero, preview visual, what-it-does, 3-step process,
deliverables showcase, use cases, deliverable grid, CTA, full nav+footer.
"""
import os, re, json

BASE = os.path.dirname(os.path.abspath(__file__))

# ============================================================
# PREVIEW MOCKUP GENERATORS — CSS-only visuals per skill type
# ============================================================

def preview_scorecard(skill_name, items, total_label="TOTAL", total_val="92/100", color="var(--verdict)"):
    rows = ""
    for label, val, pct in items:
        rows += f'''<div class="score-row"><div class="score-label"><div class="dot"></div><span>{label}</span></div><div class="score-value">{val}</div></div>
<div class="score-bar"><div class="score-bar-fill" style="width:{pct}%"></div></div>\n'''
    return f'''<div class="preview-card">
<div class="preview-card-header"><h4>{skill_name}</h4><div class="status">READY</div></div>
{rows}<div class="score-row" style="border-top:2px solid var(--ink);margin-top:12px;padding-top:14px"><div class="score-label"><span style="font-weight:600">{total_label}</span></div><div class="score-value" style="color:{color};font-size:18px">{total_val}</div></div>
</div>'''

def preview_table(skill_name, headers, rows, status="READY"):
    ths = "".join(f"<th>{h}</th>" for h in headers)
    trs = ""
    for row in rows:
        tds = "".join(f"<td>{c}</td>" for c in row)
        trs += f"<tr>{tds}</tr>\n"
    return f'''<div class="preview-card">
<div class="preview-card-header"><h4>{skill_name}</h4><div class="status">{status}</div></div>
<table style="width:100%;font-size:13px;border-collapse:collapse">
<thead><tr style="border-bottom:2px solid var(--ink)">{ths}</tr></thead>
<tbody>{trs}</tbody>
</table>
</div>'''

def preview_checklist(skill_name, items, status="READY"):
    lis = ""
    for label, checked in items:
        box = "☑" if checked else "☐"
        style = "color:var(--verdict)" if checked else "color:var(--muted)"
        lis += f'<div class="score-row"><div class="score-label"><span style="{style}">{box}</span><span>{label}</span></div></div>\n'
    progress = int(sum(1 for _,c in items if c)/len(items)*100)
    return f'''<div class="preview-card">
<div class="preview-card-header"><h4>{skill_name}</h4><div class="status">{status}</div></div>
{lis}<div class="score-bar" style="margin-top:16px"><div class="score-bar-fill" style="width:{progress}%"></div></div>
<div style="text-align:right;font-family:var(--font-mono);font-size:12px;color:var(--muted);margin-top:6px">{progress}% complete</div>
</div>'''

def preview_doc(skill_name, lines, status="READY"):
    body = ""
    for line in lines:
        if line.startswith("# "):
            body += f'<div style="font-family:var(--font-display);font-size:16px;font-weight:600;margin:16px 0 8px;color:var(--ink)">{line[2:]}</div>\n'
        elif line.startswith("- "):
            body += f'<div style="padding:4px 0 4px 16px;font-size:13px;color:var(--muted);position:relative"><span style="position:absolute;left:0;color:var(--brass)">•</span>{line[2:]}</div>\n'
        else:
            body += f'<div style="font-size:13px;color:var(--muted);margin-bottom:8px;line-height:1.5">{line}</div>\n'
    return f'''<div class="preview-card">
<div class="preview-card-header"><h4>{skill_name}</h4><div class="status">{status}</div></div>
<div style="border-left:3px solid var(--brass);padding-left:16px">{body}</div>
</div>'''

def preview_timeline(skill_name, steps, status="READY"):
    lis = ""
    for i, (label, desc) in enumerate(steps, 1):
        lis += f'''<div style="display:flex;gap:16px;margin-bottom:16px">
<div style="width:32px;height:32px;border-radius:50%;background:var(--brass);color:#fff;display:flex;align-items:center;justify-content:center;font-family:var(--font-mono);font-size:12px;flex-shrink:0">{i:02d}</div>
<div><div style="font-weight:600;font-size:14px">{label}</div><div style="font-size:12px;color:var(--muted)">{desc}</div></div>
</div>'''
    return f'''<div class="preview-card">
<div class="preview-card-header"><h4>{skill_name}</h4><div class="status">{status}</div></div>
{lis}</div>'''

def preview_chart(skill_name, bars, status="READY"):
    lis = ""
    for label, val, pct, color in bars:
        lis += f'''<div style="margin-bottom:14px">
<div style="display:flex;justify-content:space-between;font-size:13px;margin-bottom:4px"><span>{label}</span><span style="font-weight:600">{val}</span></div>
<div class="score-bar"><div class="score-bar-fill" style="width:{pct}%;background:{color}"></div></div>
</div>'''
    return f'''<div class="preview-card">
<div class="preview-card-header"><h4>{skill_name}</h4><div class="status">{status}</div></div>
{lis}</div>'''

def preview_grid(skill_name, cells, status="READY"):
    grid = ""
    for label, val, color in cells:
        grid += f'''<div style="background:var(--porcelain);border-radius:8px;padding:16px;text-align:center">
<div style="font-family:var(--font-mono);font-size:11px;color:var(--muted);text-transform:uppercase;margin-bottom:6px">{label}</div>
<div style="font-family:var(--font-display);font-size:22px;color:{color};font-weight:600">{val}</div>
</div>'''
    return f'''<div class="preview-card">
<div class="preview-card-header"><h4>{skill_name}</h4><div class="status">{status}</div></div>
<div style="display:grid;grid-template-columns:repeat(2,1fr);gap:12px">{grid}</div>
</div>'''

# ============================================================
# BUSINESS CONTEXT — How each skill helps THAT business
# ============================================================

BUSINESS_CONTEXT = {
    "sales": "This skill gives your sales team a repeatable system to identify, qualify, and close deals faster. Instead of wasting hours on cold leads that never convert, your reps focus their energy on prospects that have already been scored, segmented, and action-tagged. The result: higher win rates, shorter cycles, and cleaner pipeline forecasting.",
    "marketing": "This skill removes the guesswork from campaign planning, content creation, and brand positioning. Your marketing team produces assets that actually move the needle — with clear briefs, tested messaging, and measured outcomes. No more spray-and-pray. Every dollar spent is tied to a defined audience, channel, and KPI.",
    "customer-support": "This skill turns your support function from a cost center into a retention engine. Faster first responses, clearer escalation paths, and proactive health checks mean customers feel heard before they churn. Your team handles more tickets with fewer escalations — and you get the data to prove it.",
    "coaching": "This skill structures your coaching practice so every client gets consistent, measurable progress. From discovery to graduation, each session has a purpose, each homework assignment has accountability, and each outcome has proof. You spend less time on admin and more time delivering transformation.",
    "schools-education": "This skill helps your institution run smoother — from admissions to alumni. Standardized processes mean less firefighting, clearer accountability, and better experiences for students, parents, and staff. Compliance, accreditation, and safety requirements are tracked proactively, not chased at deadline.",
    "consultancy": "This skill protects your firm's margin and reputation. Every engagement starts with a clear scope, runs with tracked deliverables, and closes with documented outcomes. Clients see value at every stage — and you have the evidence to justify fees, defend scope, and win the next RFP.",
    "healthcare": "This skill keeps your clinic, hospital, or practice compliant, efficient, and patient-centered. From intake to discharge, every workflow is documented, every handoff is traceable, and every regulatory requirement is met before the inspector arrives. Staff spend less time on paperwork and more time on care.",
    "legal": "This skill reduces your firm's exposure and speeds up matter turnaround. Contracts are reviewed faster, compliance deadlines are never missed, and client communication is always documented. Junior associates ramp quicker, partners delegate with confidence, and billing leakage drops.",
    "construction": "This skill keeps your project on time, on budget, and safe. Every subcontractor is pre-qualified, every change order is documented, and every safety inspection is logged. When disputes arise, you have the paper trail. When margins tighten, you have the data to optimize.",
    "logistics": "This skill cuts transit time, inventory carrying cost, and customs delay. Routes are optimized, warehouses are slotted for velocity, and documentation is always complete. Your customers get accurate ETAs, your finance team sees lower freight spend, and your compliance officer sleeps better.",
    "hospitality": "This skill turns every guest touchpoint into a revenue or loyalty opportunity. From booking to checkout, each interaction is scripted, each complaint is recovered, and each upsell is timed. Your staff know exactly what to say and when — and your reviews reflect it.",
    "it-devops": "This skill keeps your infrastructure reliable, secure, and cost-controlled. Incidents are resolved faster, deployments are safer, and cloud spend is visible before it balloons. Your team moves from reactive firefighting to proactive SRE practice — with runbooks, dashboards, and post-mortems that actually prevent repeats.",
    "personal-productivity": "This skill gives you back control of your time, energy, and priorities. Instead of reacting to every notification, you run your day with intention. Meetings have purpose, emails have triage rules, and deep work has protected blocks. The result: more done, less burnout, clearer thinking.",
    "health-fitness": "This skill turns generic advice into a plan built for your body and schedule. Whether you are training for an event, managing a condition, or building a coaching business — every workout, meal, and recovery session is purposeful and trackable. Progress stops being a guess and starts being data.",
    "hr-solutions": "This skill makes your HR function invisible to the business — because everything just works. Onboarding is automatic, payroll is accurate, compliance is current, and performance reviews actually drive development. Managers spend less time chasing HR and more time leading their teams.",
    "real-estate": "This skill protects every transaction you touch. From RERA compliance to lease analysis, each document is reviewed, each deadline is tracked, and each client is informed before they ask. You close faster, dispute less, and build the referral network that feeds your pipeline.",
    "ceo-reset": "This skill gives you the clarity and structure to lead instead of react. Board decks write themselves, decisions have criteria, runway is visible, and your executive team operates from the same playbook. You spend less time in ambiguity and more time driving the outcomes that matter.",
    "finance-audit": "This skill keeps your books clean, your tax filings accurate, and your audit trail complete. Every reconciliation is documented, every variance is explained, and every forecast is grounded in actuals. Investors trust your numbers. Regulators find nothing. You sleep through month-end.",
}

# ============================================================
# USE CASE GENERATORS — 5 per vertical, tailored
# ============================================================

USE_CASES = {
    "sales": [
        "<strong>Inbound qualification:</strong> Score every demo request and content download before a rep touches it — so first calls start warm, not cold.",
        "<strong>Event follow-up:</strong> Rank trade-show leads by engagement depth within 24 hours, while memory is fresh and competition is slow.",
        "<strong>Database cleanup:</strong> Re-score your entire CRM to surface dormant leads worth re-engaging — often 15-20% of your pipeline hides here.",
        "<strong>Account-based targeting:</strong> Build tiered account lists for SDR outreach based on composite intent + engagement + fit scores.",
        "<strong>Sales-marketing calibration:</strong> Use score trends to redirect ad spend toward segments that actually convert to revenue.",
    ],
    "marketing": [
        "<strong>Campaign launch:</strong> Run this skill before any paid spend to lock objective, audience, message, channel, and KPI in one brief.",
        "<strong>Brand consistency:</strong> Train new writers and agencies on your voice pillars so every asset sounds like you — not generic AI mush.",
        "<strong>SEO recovery:</strong> Audit your site quarterly, prioritize fixes by traffic impact, and track ranking movement month over month.",
        "<strong>Crisis response:</strong> When a negative review or PR hit lands, generate the holding statement, channel response, and internal memo in minutes.",
        "<strong>Content scale:</strong> Turn one campaign brief into a full calendar of blog posts, emails, socials, and ads without losing the thread.",
    ],
    "customer-support": [
        "<strong>Ticket deflection:</strong> Pre-empt the top 20 contact reasons with self-service articles and chatbot flows — watch volume drop 30%.",
        "<strong>VIP recovery:</strong> When a high-value customer escalates, instantly generate the white-glove response, compensation offer, and follow-up sequence.",
        "<strong>Seasonal surge:</strong> Pre-position staffing, FAQ updates, and automation before Black Friday or tax season hits.",
        "<strong>Agent coaching:</strong> Use QA scorecards and call insight extraction to turn every interaction into a micro-training moment.",
        "<strong>Churn early warning:</strong> Flag at-risk accounts from support ticket sentiment, response delays, and complaint patterns before they cancel.",
    ],
    "coaching": [
        "<strong>New client intake:</strong> Run a structured discovery that extracts real goals, surface-level symptoms, and hidden blockers in the first call.",
        "<strong>Session accountability:</strong> Generate homework with deadlines, success criteria, and reflection prompts so clients do the work between sessions.",
        "<strong>Group program design:</strong> Build a half-day workshop with icebreakers, breakout activities, and debriefs that actually shift behavior.",
        "<strong>Progress reporting:</strong> Show clients their milestone tracker, habit scorecard, and trend visualization — proof they are changing.",
        "<strong>Business growth:</strong> Use testimonial request scripts, referral partner briefs, and package pricing calculators to fill your pipeline ethically.",
    ],
    "schools-education": [
        "<strong>Admissions conversion:</strong> Track every inquiry through enrollment with touchpoints, events, and conversion triggers — no student slips through.",
        "<strong>Lesson standardization:</strong> Ensure every teacher covers objectives, activities, assessments, and differentiation in a consistent format.",
        "<strong>Safeguarding:</strong> Document anti-bullying actions, incident reports, and intervention steps with timestamps and ownership.",
        "<strong>Accreditation prep:</strong> Organize self-study evidence, visit schedules, and post-visit action plans so inspection day is calm, not chaotic.",
        "<strong>Parent engagement:</strong> Automate progress updates, incident reports, and meeting summaries so parents feel informed, not surprised.",
    ],
    "consultancy": [
        "<strong>RFP wins:</strong> Turn around compelling, compliant proposals faster by reusing structured sections and pricing logic.",
        "<strong>Scope protection:</strong> Write SOWs with clear deliverables, exclusions, and change-control clauses so scope creep becomes billable.",
        "<strong>Client trust:</strong> Run kickoff meetings with decision logs, RACI charts, and communication protocols — no ambiguity, no blame later.",
        "<strong>Team utilization:</strong> Track hours, milestones, budget burn, and client satisfaction per engagement — optimize before margin bleeds.",
        "<strong>Thought leadership:</strong> Convert project insights into publishable articles that position your firm as the expert in the room.",
    ],
    "healthcare": [
        "<strong>Patient flow:</strong> Optimize intake, scheduling, and discharge so wait times drop and capacity increases without adding staff.",
        "<strong>Compliance readiness:</strong> Maintain HIPAA, MOH, DHA, or JCI documentation so audits become confirmations, not scrambles.",
        "<strong>Revenue integrity:</strong> Verify insurance eligibility, code accurately, and appeal denials with complete documentation.",
        "<strong>Quality monitoring:</strong> Track infection rates, readmissions, and patient safety events with dashboards that trigger action.",
        "<strong>Telehealth scale:</strong> Standardize virtual visit prep, documentation, and follow-up so remote care matches in-person quality.",
    ],
    "legal": [
        "<strong>Contract velocity:</strong> Review NDAs, employment agreements, and vendor contracts with checklists that catch issues junior eyes miss.",
        "<strong>Deadline management:</strong> Never miss a filing, a limitation period, or a regulatory submission with tracked calendars and alerts.",
        "<strong>Litigation prep:</strong> Organize deposition scripts, evidence indexes, and timeline builders so trial day is rehearsed, not improvised.",
        "<strong>Client intake:</strong> Run conflict checks, scope confirmations, and fee arrangements before the clock starts — no write-offs later.",
        "<strong>Knowledge leverage:</strong> Turn matter-specific insights into reusable clause libraries, playbooks, and precedent templates.",
    ],
    "construction": [
        "<strong>Schedule discipline:</strong> Build Gantt charts with critical path, float analysis, and milestone gates so delays are predicted, not discovered.",
        "<strong>Safety culture:</strong> Run site audits, induction packs, and incident reports that keep your EMR low and your insurance stable.",
        "<strong>Subcontractor control:</strong> Pre-qualify every trade, track performance, and document deliverables so disputes have evidence.",
        "<strong>Cost control:</strong> Estimate accurately, track change orders, and reconcile final accounts with variance analysis by line item.",
        "<strong>Closeout excellence:</strong> Generate punch lists, as-builts, warranty packs, and handover documentation that protect your retention.",
    ],
    "logistics": [
        "<strong>Route efficiency:</strong> Cut fuel cost and transit time with multi-stop sequencing that respects time windows and vehicle capacity.",
        "<strong>Inventory optimization:</strong> Right-size safety stock, reduce carrying cost, and eliminate stockouts with EOQ-driven reorder points.",
        "<strong>Customs clearance:</strong> Classify correctly, document completely, and clear faster — avoiding demurrage, penalties, and client complaints.",
        "<strong>3PL governance:</strong> Hold providers to SLA, KPI, and performance guarantee clauses with scorecards and quarterly reviews.",
        "<strong>Reverse logistics:</strong> Handle returns, repairs, and recycling with authorization, inspection, and refund triggers that protect margin.",
    ],
    "hospitality": [
        "<strong>Guest recovery:</strong> Turn complaints into loyalty by responding with empathy, compensation, and follow-up in under 15 minutes.",
        "<strong>Revenue optimization:</strong> Adjust ADR, occupancy, and package pricing dynamically by segment, season, and booking window.",
        "<strong>Review management:</strong> Respond to every Google, TripAdvisor, and OTA review with tone-appropriate replies that protect your rating.",
        "<strong>Event execution:</strong> Run banquets, weddings, and corporate events with BEOs that cover menu, timing, AV, and staffing — nothing missed.",
        "<strong>Staff scheduling:</strong> Build rosters based on forecasted occupancy, break rules, and labor budget — no overtime surprises.",
    ],
    "it-devops": [
        "<strong>Incident response:</strong> Resolve outages faster with runbooks that give exact commands, checks, and escalation paths.",
        "<strong>Deployment safety:</strong> Assess change risk, define rollback criteria, and execute go/no-go decisions with documented evidence.",
        "<strong>Cost visibility:</strong> Find unused resources, right-size instances, and lock in savings plans before finance asks questions.",
        "<strong>Security posture:</strong> Track vulnerabilities, certificate expiries, and access reviews with dashboards that show trend, not snapshot.",
        "<strong>Disaster readiness:</strong> Test backups, verify failover, and document DR procedures so RTO and RPO are promises, not guesses.",
    ],
    "personal-productivity": [
        "<strong>Daily control:</strong> Start each day with a brief that extracts priorities from calendar and tasks — react less, decide more.",
        "<strong>Meeting discipline:</strong> Enter every meeting with a dossier of attendees, agenda, decisions needed, and follow-up actions.",
        "<strong>Email zero:</strong> Apply the 2-minute rule, delegate, defer, and delete with templates that cut inbox time by half.",
        "<strong>Deep work protection:</strong> Block focus time, defend boundaries, and batch shallow work so your best hours produce your best output.",
        "<strong>Goal tracking:</strong> Set quarterly OKRs, score weekly initiatives, and calibrate confidence — no more forgotten resolutions.",
    ],
    "health-fitness": [
        "<strong>Training precision:</strong> Follow periodized cycles with volume, intensity, and recovery mapped to your event or physique goal.",
        "<strong>Nutrition compliance:</strong> Hit calorie and macro targets with meal plans, grocery lists, and prep schedules built for your lifestyle.",
        "<strong>Injury prevention:</strong> Screen movement patterns, identify asymmetries, and assign corrective exercises before pain sidelines you.",
        "<strong>Recovery optimization:</strong> Schedule sleep, mobility, and active recovery with the same discipline you apply to training.",
        "<strong>Business launch:</strong> Open a coaching practice with niche clarity, package pricing, liability coverage, and client acquisition systems.",
    ],
    "hr-solutions": [
        "<strong>Onboarding velocity:</strong> Get new hires productive in days, not weeks, with 30-60-90 day plans that include milestones and buddies.",
        "<strong>Payroll accuracy:</strong> Process runs with automated calculations, compliance checks, and direct-file formatting — no manual rework.",
        "<strong>Performance culture:</strong> Run reviews that drive development, not dread, with structured templates, scorecards, and follow-up actions.",
        "<strong>Compliance defense:</strong> Audit labor law adherence, visa status, and termination documentation before an inspection or dispute.",
        "<strong>Talent pipeline:</strong> Build recruitment pipelines, interview scorecards, and offer packages that land candidates before competitors do.",
    ],
    "real-estate": [
        "<strong>Transaction protection:</strong> Review every RERA checklist, lease clause, and off-plan document before signature — no surprises at transfer.",
        "<strong>Valuation confidence:</strong> Generate comparable-market reports with adjustment factors, cap rates, and investment-grade analysis.",
        "<strong>Tenant quality:</strong> Screen applicants with credit, reference, and background checks that reduce default and eviction risk.",
        "<strong>Portfolio tracking:</strong> Monitor rental yield, maintenance schedules, and lease expiries across multiple units in one dashboard.",
        "<strong>Listing performance:</strong> Optimize property descriptions, photo order, and platform placement to cut days-on-market by 20%+.",
    ],
    "ceo-reset": [
        "<strong>Board confidence:</strong> Produce narrative-driven decks with proof points, case studies, and clear asks — every quarter, not just fundraise season.",
        "<strong>Decision quality:</strong> Apply structured criteria, scenario planning, and stakeholder maps so strategic calls have evidence, not ego.",
        "<strong>Runway visibility:</strong> Model burn, headcount, and revenue scenarios so you know exactly when to raise, hire, or cut.",
        "<strong>Team alignment:</strong> Cascade OKRs from company to individual with dashboards that show contribution, not just completion.",
        "<strong>Crisis readiness:</strong> Maintain response playbooks, communication templates, and stakeholder lists so bad news is managed, not leaked.",
    ],
    "finance-audit": [
        "<strong>Month-end speed:</strong> Close books in 3-5 days with reconciliation checklists, variance flags, and auto-generated reports.",
        "<strong>Tax accuracy:</strong> File VAT, corporate tax, and withholding returns with complete documentation, calculations, and audit trails.",
        "<strong>Audit readiness:</strong> Maintain evidence folders, sample selections, and control documentation so external audits finish early.",
        "<strong>Forecast precision:</strong> Build 3-statement models with driver-based assumptions, scenario toggles, and sensitivity tables.",
        "<strong>Investor trust:</strong> Generate update templates, cap table reports, and KPI dashboards that keep backers informed and confident.",
    ],
}

# ============================================================
# SKILL DATABASE — 25 per vertical
# ============================================================

VERTICALS = {
    "sales": {
        "title": "Sales & Business Development",
        "skills": [
            ("Lead Scoring Framework", "PROSPECTING", "Qualify leads with weighted scoring models based on BANT, MEDDIC, and custom criteria.", "scorecard", [("Budget confirmed","+25","75"),("Authority identified","+20","60"),("Need validated","+20","60"),("Timeline < 90 days","+15","45"),("Engagement score","+12","36")], "92/100"),
            ("Apollo.io Outreach Builder", "PROSPECTING", "Build targeted contact lists, sequence templates, and A/B test copy for Apollo campaigns.", "table", [("Contact","Title","Company","Status"),("Sarah Chen","VP Sales","Acme","Verified"),("James Park","Director","Beta","Pending"),("Lisa Rao","Head of Ops","Gamma","Bounced")]),
            ("Cold Email Chain Designer", "OUTREACH", "7-touch email sequences with subject line variants, openers, and objection handlers.", "timeline", [("Touch 1 — Break the ice","Pattern interrupt opener + soft ask"),("Touch 2 — Add value","Insight or tool relevant to their role"),("Touch 3 — Social proof","Peer result from same industry"),("Touch 4 — Direct ask","Specific meeting request with calendar link"),("Touch 5 — Last call","Final attempt with clear next step")]),
            ("LinkedIn Prospecting System", "SOCIAL", "Connection request scripts, InMail templates, and content engagement playbooks for LinkedIn.", "doc", ["# Connection Script","- Personalized opener referencing recent post","- Value-first ask (insight, not pitch)","- Low-friction CTA (coffee chat, not demo)","# InMail Template","- Subject: [Mutual connection] + [Specific result]","- Body: 3 lines max. One insight. One question."]),
            ("CRM Hygiene & Enrichment", "CRM", "Dedupe, standardize, and enrich contact records with firmographic and technographic data.", "checklist", [("Duplicate merge rules",True),("Standardized naming convention",True),("Firmographic enrichment",True),("Technographic tags",True),("Invalid email flagging",False),("Ownership reassignment",True),("Last activity timestamp",True)]),
            ("Discovery Call Script", "CALLS", "Structured first-call framework — pain detection, budget confirmation, timeline mapping.", "doc", ["# Opening (2 min)","- Confirm agenda and ask permission","# Pain Exploration (10 min)","- Current process walkthrough","- Gap identification","- Cost of inaction quantification","# Budget & Authority (5 min)","- Rough budget range","- Decision maker map","# Next Steps (3 min)","- Mutual agreed action","- Calendar hold for follow-up"]),
            ("Demo Personalization Engine", "DEMO", "Tailor product demos to industry, role, and use case with dynamic storyline builder.", "table", [("Segment","Hero Feature","Proof Point","CTA"),("Enterprise IT","SSO & Audit Logs","Fortune 500 rollout","Security review"),("Startup Founders","Speed to Value","Launch in 48 hrs","Pilot terms"),("Operations","Automation Rules","60% ticket reduction","Workflow audit")]),
            ("Proposal & Quote Generator", "CLOSE", "Professional proposals with pricing tables, terms, and e-signature integration.", "doc", ["# Executive Summary","- Problem statement + proposed solution","# Scope of Work","- Deliverables, timeline, exclusions","# Pricing","- Itemized table with options","# Terms","- Payment, IP, termination, governing law","# Acceptance","- E-signature block + expiration date"]),
            ("Objection Response Library", "CLOSE", "50+ proven responses to price, timing, authority, and competition objections.", "grid", [("Price","27 scripts","var(--verdict)"),("Timing","14 scripts","var(--brass)"),("Authority","12 scripts","var(--brass)"),("Competition","9 scripts","var(--flag)")]),
            ("Sales Deck Narrative Builder", "PRESENT", "Story-driven pitch decks with proof points, case studies, and CTA slides.", "timeline", [("Slide 1 — Hook","Industry stat or customer quote that hurts"),("Slide 2 — Problem","Zoom into the specific pain they feel daily"),("Slide 3 — Solution","Your product as the bridge — not the hero"),("Slide 4 — Proof","Before/after metric from a peer company"),("Slide 5 — CTA","Clear next step with calendar link or trial"),("Slide 6 — Appendix","Technical detail, security, team bios")]),
            ("Pipeline Forecasting Model", "ANALYTICS", "Weighted pipeline stages, commit calculations, and variance analysis by rep.", "chart", [("Discovery","$240K","60","var(--brass)"),("Demo","$180K","45","var(--brass)"),("Proposal","$120K","80","var(--verdict)"),("Negotiation","$90K","90","var(--verdict)"),("Closed Won","$75K","100","var(--verdict)")]),
            ("Competitor Battle Card", "INTEL", "Head-to-head comparison grids — feature, price, and positioning for any competitor.", "table", [("Dimension","Us","Competitor A","Competitor B"),("Pricing","$99/mo","$149/mo","Freemium"),("Setup","Self-serve","2-week onboarding","DIY"),("Support","24/7 chat","Business hours","Email only"),("Integration","200+ native","50 via Zapier","API only")]),
            ("Account-Based Marketing Plan", "ABM", "Target account selection, stakeholder mapping, and personalized campaign plays.", "doc", ["# Target Account Criteria","- Revenue > $10M","- Technology stack match","- Recent funding or hiring signal","# Stakeholder Map","- Economic Buyer: CFO","- Technical Evaluator: CTO","- Champion: VP Ops","# Campaign Play","- LinkedIn thought leadership","- Direct mail + digital surround","- Executive dinner invitation"]),
            ("Churn Risk Scoring", "RETENTION", "Early-warning indicators, intervention playbooks, and save-sequence automation.", "scorecard", [("Usage drop > 30%","+30","90"),("Support tickets > 5/mo","+20","60"),("NPS decline","+15","45"),("Contract approaching renewal","+10","30"),("No executive sponsor","+15","45"),("Competitor mention","+10","30")], "70/100 — AT RISK"),
            ("Upsell & Cross-sell Detector", "EXPANSION", "Usage-pattern triggers, expansion timing, and upgrade proposal templates.", "grid", [("Signals","12","var(--verdict)"),("Triggers","8","var(--brass)"),("Templates","6","var(--brass)"),("Close Rate","34%","var(--verdict)")]),
            ("Referral Request System", "NETWORK", "Timing, messaging, and incentive structures for customer referral generation.", "timeline", [("Day 14 — First value","Thank-you + soft referral ask after initial win"),("Day 30 — Case study","Offer co-marketing in exchange for intro"),("Day 60 — Incentive launch","$500 credit or gift card for closed referral"),("Day 90 — NPS follow-up","Promoter → automatic referral email trigger"),("Quarterly — VIP event","Invite top customers + encourage guest list")]),
            ("RFP Response Builder", "ENTERPRISE", "Standardized RFP answer library, compliance checklists, and submission formatting.", "checklist", [("Executive summary",True),("Technical approach",True),("Past performance refs",True),("Team bios",True),("Security & compliance",False),("Pricing schedule",True),("Draft review",False),("Final format check",True)]),
            ("Territory Planning Model", "STRATEGY", "Account distribution, quota allocation, and coverage optimization by geography.", "table", [("Territory","Accounts","Quota","Coverage"),("North","145","$1.2M","1 rep"),("South","98","$900K","1 rep"),("East","210","$1.8M","2 reps"),("West","167","$1.5M","1 rep + SDR")]),
            ("Sales Compensation Calculator", "COMP", "OTE splits, accelerator tiers, clawback rules, and attainment projections.", "chart", [("Base","$60K","40","var(--muted)"),("Target","$60K","40","var(--brass)"),("Accelerator","$24K","16","var(--verdict)"),("Clawback","-$6K","-4","var(--flag)")]),
            ("Win-Loss Analysis Template", "ANALYTICS", "Structured debriefs — why we won, why we lost, and pattern aggregation.", "doc", ["# Win Debrief","- Decision criteria ranked","- Our strength that tipped the scale","- Competitor weakness exposed","# Loss Debrief","- Primary reason (price, product, timing, relationship)","- Competitor advantage","- What we could have done differently","# Pattern Report","- Win rate by segment, rep, and product","- Common loss reasons with frequency"]),
            ("Sales Onboarding Playbook", "ENABLEMENT", "30-60-90 day ramp plan, certification milestones, and shadow schedule.", "timeline", [("Days 1–30: Learn","Product deep-dive, CRM setup, shadow 10 calls, pass certification"),("Days 31–60: Practice","Lead 5 discovery calls, build pipeline of 20, draft 3 proposals"),("Days 61–90: Perform","Close first deal, hit 50% quota, present at team meeting")]),
            ("Call Recording Insight Extractor", "ENABLEMENT", "Transcript analysis, talk-ratio scoring, and coaching moment identification.", "grid", [("Talk Ratio","42:58","var(--flag)"),("Questions Asked","12","var(--verdict)"),("Objections Handled","3/4","var(--brass)"),("Follow-up Set","Yes","var(--verdict)")]),
            ("Pricing Negotiation Matrix", "CLOSE", "Discount authority levels, trade-off options, and margin-protected counteroffers.", "table", [("Discount","Authority","Trade-off Required","Margin Impact"),("0–5%","Rep","None","-2%"),("5–10%","Manager","Extended term","-4%"),("10–15%","VP","Case study + annual","-6%"),(">15%","CEO","Board approval","-8%+")]),
            ("Event Lead Capture System", "FIELD", "Badge-scan workflows, follow-up sequences, and ROI tracking for trade shows.", "checklist", [("Scanner app configured",True),("Lead scoring rules loaded",True),("Follow-up email drafted",True),("CRM sync enabled",True),("ROI tracker active",False),("Post-event nurture queued",True)]),
            ("Sales Handoff to CS Brief", "HANDOFF", "Complete context transfer — stakeholders, promises, risks, and onboarding triggers.", "doc", ["# Customer Context","- Industry, size, use case, expansion potential","# Stakeholders","- Economic buyer, technical owner, day-to-day contact","# Promises Made","- Delivery timeline, custom features, pricing locked","# Risk Flags","- Competitive evaluation ongoing, tight timeline","# Onboarding Triggers","- Kickoff call booked, success metrics defined"]),
        ]
    },
}

# We'll build the rest dynamically from the existing vertical files to save space
# But first, let me write the HTML template and helper functions

def slugify(name):
    s = name.lower().replace("&", "and").replace("—", "-").replace("'", "")
    s = re.sub(r'[^a-z0-9\-]', '-', s)
    s = re.sub(r'-+', '-', s).strip('-')
    return s[:50]

def generate_skill_page(vert_slug, vert_title, skill_name, skill_cat, skill_desc, preview_type, preview_data, total_score=None):
    skill_slug = f"skill-{slugify(skill_name)}"
    back_url = f"{vert_slug}.html"
    back_label = vert_title
    badge = f"{skill_cat} · {vert_title.upper()} COLLECTION"
    
    # Build preview HTML
    if preview_type == "scorecard":
        preview_html = preview_scorecard(skill_name, preview_data, total_label="TOTAL", total_val=total_score or "92/100")
    elif preview_type == "table":
        headers = preview_data[0]
        rows = preview_data[1:]
        preview_html = preview_table(skill_name, headers, rows)
    elif preview_type == "checklist":
        preview_html = preview_checklist(skill_name, preview_data)
    elif preview_type == "doc":
        preview_html = preview_doc(skill_name, preview_data)
    elif preview_type == "timeline":
        preview_html = preview_timeline(skill_name, preview_data)
    elif preview_type == "chart":
        preview_html = preview_chart(skill_name, preview_data)
    elif preview_type == "grid":
        preview_html = preview_grid(skill_name, preview_data)
    else:
        preview_html = preview_scorecard(skill_name, [("Item 1","+25","75"),("Item 2","+20","60")], total_val="85/100")
    
    # Business context
    biz = BUSINESS_CONTEXT.get(vert_slug, "This skill helps your business operate more efficiently, reduce risk, and deliver better outcomes to your customers and stakeholders.")
    
    # Use cases
    uses = USE_CASES.get(vert_slug, [
        "<strong>Primary use:</strong> Apply this skill to your core workflow for immediate efficiency gains.",
        "<strong>Scale use:</strong> Deploy across teams for standardized, measurable output.",
        "<strong>Crisis use:</strong> Run this skill when deadlines compress or quality is at risk.",
        "<strong>Growth use:</strong> Use outputs to win new clients, funding, or market positioning.",
        "<strong>Audit use:</strong> Maintain documentation and compliance readiness at all times.",
    ])
    
    # 3-step process (generic but tailored)
    steps = [
        ("Input your context", f"Upload data, paste details, or answer guided questions. The skill auto-detects format and maps to the right framework."),
        ("Choose your approach", f"Select from proven models — {skill_cat.lower()}-standard, hybrid, or fully custom. Adjust weights, tone, and depth to match your business."),
        ("Get ranked output", f"Receive structured deliverables with hot/warm/cold labels, next actions, and CRM-ready formats. Share, export, or act immediately."),
    ]
    
    # Deliverables
    deliverables = [
        ("📋", "Framework", f"Complete {skill_cat.lower()} structure with adjustable criteria"),
        ("📈", "Ranked Output", "Segmented results with action labels and priorities"),
        ("🎯", "Action Playbook", f"Next-best-action guide by tier for your {vert_slug.replace('-',' ')} team"),
        ("🔄", "CRM Ready", "Import mapping and API-ready formatting included"),
    ]
    
    # Sample output preview (different from preview card)
    sample_lines = [
        ("Acme Corp", "🔥 HOT — 92 pts"),
        ("Beta Industries", "🟡 WARM — 64 pts"),
        ("Gamma LLC", "❄️ COLD — 31 pts"),
        ("Delta Group", "🔥 HOT — 88 pts"),
        ("Epsilon Co", "🟡 WARM — 57 pts"),
    ]
    sample_html = ""
    for name, status in sample_lines:
        sample_html += f'<div style="display:flex;justify-content:space-between;padding:8px 0;border-bottom:1px solid #eee"><span>{name}</span><span>{status}</span></div>\n'
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{skill_name} — Pandora's Skill Box</title>
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Schibsted+Grotesk:wght@400;500;600;700&family=Spline+Sans+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>:root{{--ink:#0B2E29;--ink-deep:#072320;--porcelain:#F4F6F2;--paper:#FBFCFA;--brass:#B8892D;--brass-soft:#E4C878;--muted:#5C6F6A;--verdict:#17A673;--flag:#D64533;--font-display:'Instrument Serif',Georgia,serif;--font-body:'Schibsted Grotesk',system-ui,sans-serif;--font-mono:'Spline Sans Mono',monospace;}}
*{{box-sizing:border-box;margin:0;padding:0}}body{{font-family:var(--font-body);background:var(--paper);color:var(--ink);line-height:1.6}}
nav{{position:fixed;top:0;left:0;right:0;z-index:100;background:rgba(251,252,250,0.92);backdrop-filter:blur(12px);border-bottom:1px solid rgba(11,46,41,0.06)}}
.nav-inner{{max-width:1200px;margin:0 auto;padding:0 24px;display:flex;align-items:center;justify-content:space-between;height:64px}}
.nav-logo{{display:flex;align-items:center;gap:10px;text-decoration:none;color:var(--ink)}}
.nav-logo .seal{{width:32px;height:32px;border-radius:50%;background:var(--brass);display:flex;align-items:center;justify-content:center;color:#fff;font-size:14px;font-weight:700}}
.nav-logo span{{font-family:var(--font-display);font-size:20px}}
.nav-links{{display:flex;gap:16px;list-style:none;align-items:center}}
.nav-links a{{text-decoration:none;color:var(--muted);font-size:12px;font-weight:500;white-space:nowrap}}
.nav-links a:hover{{color:var(--ink)}}
.nav-cta{{background:var(--ink);color:#fff;padding:8px 14px;border-radius:6px;text-decoration:none;font-size:12px;font-weight:600;white-space:nowrap}}
.skill-hero{{min-height:50vh;display:flex;align-items:center;background:var(--ink);position:relative;overflow:hidden}}
.skill-hero::before{{content:'';position:absolute;inset:0;background:radial-gradient(ellipse at 70% 40%,rgba(184,137,45,0.1) 0%,transparent 60%)}}
.skill-hero-inner{{max-width:1200px;margin:0 auto;padding:140px 24px 60px;display:grid;grid-template-columns:1fr 1fr;gap:60px;align-items:center;position:relative;z-index:2}}
.skill-hero-text h1{{font-family:var(--font-display);font-size:clamp(28px,4vw,48px);color:var(--porcelain);line-height:1.15;margin-bottom:16px}}
.skill-hero-text .badge{{display:inline-block;background:rgba(184,137,45,0.15);color:var(--brass-soft);font-family:var(--font-mono);font-size:11px;padding:6px 14px;border-radius:100px;margin-bottom:20px;text-transform:uppercase;letter-spacing:1px}}
.skill-hero-text p{{font-size:17px;color:rgba(244,246,242,0.7);margin-bottom:32px}}
.skill-hero-text .meta{{display:flex;gap:24px;margin-bottom:32px}}
.skill-hero-text .meta-item{{display:flex;align-items:center;gap:8px;color:rgba(244,246,242,0.5);font-size:13px}}
.btn-primary{{background:var(--brass);color:#fff;padding:14px 32px;border-radius:8px;text-decoration:none;font-weight:600;font-size:15px;display:inline-block;margin-right:12px}}
.btn-secondary{{background:transparent;color:var(--brass-soft);padding:14px 24px;border:1px solid rgba(184,137,45,0.3);border-radius:8px;text-decoration:none;font-weight:600;font-size:15px;display:inline-block}}
.preview-card{{background:#fff;border-radius:16px;padding:32px;box-shadow:0 20px 60px rgba(0,0,0,0.3);transform:rotate(2deg);border:1px solid rgba(255,255,255,0.06)}}
.preview-card-header{{display:flex;justify-content:space-between;align-items:center;margin-bottom:20px}}
.preview-card-header h4{{font-family:var(--font-display);font-size:18px;color:var(--ink)}}
.preview-card-header .status{{background:var(--verdict);color:#fff;font-family:var(--font-mono);font-size:10px;padding:4px 10px;border-radius:100px}}
.score-row{{display:flex;justify-content:space-between;align-items:center;padding:14px 0;border-bottom:1px solid rgba(11,46,41,0.06)}}
.score-row:last-child{{border-bottom:none}}
.score-label{{display:flex;align-items:center;gap:10px}}
.score-label .dot{{width:8px;height:8px;border-radius:50%;background:var(--brass)}}
.score-label span{{font-size:14px;color:var(--ink)}}
.score-value{{font-family:var(--font-mono);font-size:14px;font-weight:500;color:var(--ink)}}
.score-bar{{height:4px;background:rgba(11,46,41,0.06);border-radius:2px;margin-top:6px;overflow:hidden}}
.score-bar-fill{{height:100%;background:var(--brass);border-radius:2px}}
.section{{max-width:800px;margin:0 auto;padding:80px 24px}}
.section h2{{font-family:var(--font-display);font-size:clamp(24px,3vw,36px);margin-bottom:20px;color:var(--ink)}}
.section p{{color:var(--muted);font-size:16px;margin-bottom:16px}}
.section ul{{list-style:none;padding:0;margin:20px 0}}
.section ul li{{padding:12px 0;padding-left:32px;position:relative;color:var(--muted);font-size:15px;border-bottom:1px solid rgba(11,46,41,0.04)}}
.section ul li::before{{content:'';position:absolute;left:0;top:16px;width:6px;height:6px;border-radius:50%;background:var(--brass)}}
.how-grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin-top:40px}}
.how-card{{background:#fff;border-radius:12px;padding:28px;border:1px solid rgba(11,46,41,0.06)}}
.how-card .num{{font-family:var(--font-mono);font-size:12px;color:var(--brass);margin-bottom:12px}}
.how-card h4{{font-family:var(--font-display);font-size:18px;margin-bottom:10px}}
.how-card p{{font-size:14px;color:var(--muted)}}
.output-showcase{{background:var(--ink-deep);padding:80px 24px}}
.output-showcase-inner{{max-width:1200px;margin:0 auto;display:grid;grid-template-columns:1fr 1fr;gap:60px;align-items:center}}
.output-showcase-text h2{{font-family:var(--font-display);font-size:clamp(24px,3vw,36px);color:var(--porcelain);margin-bottom:20px}}
.output-showcase-text p{{color:rgba(244,246,242,0.6);font-size:16px;margin-bottom:16px}}
.output-showcase-text .file-list{{margin-top:24px}}
.output-showcase-text .file-item{{display:flex;align-items:center;gap:12px;padding:10px 0;color:rgba(244,246,242,0.7);font-size:14px;border-bottom:1px solid rgba(244,246,242,0.06)}}
.output-visual{{background:#fff;border-radius:16px;padding:40px;box-shadow:0 20px 60px rgba(0,0,0,0.2)}}
.output-visual-header{{display:flex;align-items:center;gap:12px;margin-bottom:24px}}
.output-visual-header .icon{{width:40px;height:40px;border-radius:10px;background:var(--porcelain);display:flex;align-items:center;justify-content:center;font-size:20px}}
.output-visual-header h4{{font-family:var(--font-display);font-size:20px}}
.deliverable-grid{{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-top:32px}}
.deliverable-item{{text-align:center;padding:20px}}
.deliverable-item .icon{{width:48px;height:48px;border-radius:12px;background:var(--porcelain);display:flex;align-items:center;justify-content:center;margin:0 auto 12px;font-size:24px}}
.deliverable-item h5{{font-size:14px;margin-bottom:6px}}
.deliverable-item p{{font-size:12px;color:var(--muted)}}
.cta-bar{{background:var(--ink);padding:60px 24px;text-align:center}}
.cta-bar h2{{font-family:var(--font-display);font-size:clamp(24px,3vw,36px);color:var(--porcelain);margin-bottom:16px}}
.cta-bar p{{color:rgba(244,246,242,0.6);font-size:16px;margin-bottom:32px}}
@media(max-width:768px){{.skill-hero-inner{{grid-template-columns:1fr}}.how-grid{{grid-template-columns:1fr}}.output-showcase-inner{{grid-template-columns:1fr}}.deliverable-grid{{grid-template-columns:repeat(2,1fr)}}}}
footer{{background:var(--ink-deep);padding:60px 24px 40px}}
.footer-inner{{max-width:1200px;margin:0 auto;display:grid;grid-template-columns:2fr 1fr 1fr 1fr;gap:40px}}
.footer-brand .seal{{width:40px;height:40px;border-radius:50%;background:var(--brass);display:flex;align-items:center;justify-content:center;color:#fff;font-size:16px;font-weight:700;margin-bottom:16px}}
.footer-brand h4{{font-family:var(--font-display);color:var(--porcelain);font-size:20px;margin-bottom:8px}}
.footer-brand p{{color:rgba(244,246,242,0.5);font-size:14px}}
.footer-col h5{{color:var(--porcelain);font-size:13px;text-transform:uppercase;letter-spacing:1px;margin-bottom:20px}}
.footer-col a{{display:block;color:rgba(244,246,242,0.5);text-decoration:none;font-size:14px;margin-bottom:12px}}
.footer-bottom{{max-width:1200px;margin:40px auto 0;padding-top:24px;border-top:1px solid rgba(244,246,242,0.08);display:flex;justify-content:space-between;color:rgba(244,246,242,0.4);font-size:12px}}
</style></head>
<body>
<nav><div class="nav-inner">
<a href="index.html" class="nav-logo"><div class="seal">P</div><span>Pandora's Skill Box</span></a>
<ul class="nav-links">
<li><a href="hr-solutions.html">HR</a></li>
<li><a href="real-estate.html">Real Estate</a></li>
<li><a href="ceo-reset.html">CEO</a></li>
<li><a href="finance-audit.html">Finance</a></li>
<li><a href="sales.html">Sales</a></li>
<li><a href="marketing.html">Marketing</a></li>
<li><a href="customer-support.html">Support</a></li>
<li><a href="coaching.html">Coaching</a></li>
<li><a href="schools-education.html">Edu</a></li>
<li><a href="consultancy.html">Consult</a></li>
<li><a href="healthcare.html">Health</a></li>
<li><a href="legal.html">Legal</a></li>
<li><a href="construction.html">Build</a></li>
<li><a href="logistics.html">Logistics</a></li>
<li><a href="hospitality.html">Hospitality</a></li>
<li><a href="it-devops.html">IT</a></li>
<li><a href="personal-productivity.html">Productivity</a></li>
<li><a href="health-fitness.html">Fitness</a></li>
</ul>
<a href="index.html" class="nav-cta">← All verticals</a>
</div></nav>

<section class="skill-hero">
<div class="skill-hero-inner">
<div class="skill-hero-text">
<div class="badge">{badge}</div>
<h1>{skill_name}</h1>
<p>{skill_desc} Turn raw inputs into structured, actionable output that moves your business forward.</p>
<div class="meta">
<div class="meta-item">~8 min setup</div>
<div class="meta-item">Export: PDF + Excel + API</div>
<div class="meta-item">Data stays in your account</div>
</div>
<a href="#get" class="btn-primary">Get this skill →</a>
<a href="{back_url}" class="btn-secondary">← Back to {back_label}</a>
</div>
<div class="preview-card-wrapper">
{preview_html}
</div>
</div>
</section>

<section class="section">
<h2>What this skill does</h2>
<p>{skill_desc} {biz}</p>
<div class="how-grid">
<div class="how-card"><div class="num">01</div><h4>{steps[0][0]}</h4><p>{steps[0][1]}</p></div>
<div class="how-card"><div class="num">02</div><h4>{steps[1][0]}</h4><p>{steps[1][1]}</p></div>
<div class="how-card"><div class="num">03</div><h4>{steps[2][0]}</h4><p>{steps[2][1]}</p></div>
</div>
</section>

<section class="output-showcase">
<div class="output-showcase-inner">
<div class="output-showcase-text">
<h2>What you get</h2>
<p>Every run produces a complete package you can use immediately — no formatting, no manual assembly, no guesswork.</p>
<div class="file-list">
<div class="file-item">📋 Structured output document (PDF / Word)</div>
<div class="file-item">📈 Data file ready for import (CSV / Excel / JSON)</div>
<div class="file-item">🎯 Action playbook with next-best-step guidance</div>
<div class="file-item">🔄 Integration mapping for your CRM or ERP</div>
</div>
</div>
<div class="output-visual">
<div class="output-visual-header"><div class="icon">📊</div><h4>Sample Output Preview</h4></div>
<div style="font-family:var(--font-mono);font-size:12px;color:var(--muted);line-height:2">
{sample_html}</div>
<p style="font-size:11px;color:var(--muted);margin-top:16px">⚡ This is a live preview. Your actual output will match your data and chosen model.</p>
</div>
</div>
</section>

<section class="section">
<h2>Use cases</h2>
<ul>
<li>{uses[0]}</li>
<li>{uses[1]}</li>
<li>{uses[2]}</li>
<li>{uses[3]}</li>
<li>{uses[4]}</li>
</ul>
</section>

<section class="section" style="padding-top:0">
<h2>Deliverables at a glance</h2>
<div class="deliverable-grid">
<div class="deliverable-item"><div class="icon">{deliverables[0][0]}</div><h5>{deliverables[0][1]}</h5><p>{deliverables[0][2]}</p></div>
<div class="deliverable-item"><div class="icon">{deliverables[1][0]}</div><h5>{deliverables[1][1]}</h5><p>{deliverables[1][2]}</p></div>
<div class="deliverable-item"><div class="icon">{deliverables[2][0]}</div><h5>{deliverables[2][1]}</h5><p>{deliverables[2][2]}</p></div>
<div class="deliverable-item"><div class="icon">{deliverables[3][0]}</div><h5>{deliverables[3][1]}</h5><p>{deliverables[3][2]}</p></div>
</div>
</section>

<section class="cta-bar" id="get">
<h2>Ready to put this skill to work?</h2>
<p>Get the {skill_name} skill. Runs in your own AI account. Nothing stored on our servers.</p>
<a href="invoice.html" class="btn-primary">Get this skill →</a>
</section>

<footer><div class="footer-inner">
<div class="footer-brand"><div class="seal">P</div><h4>Pandora's Skill Box</h4><p>Certified AI skills that run in your own account.</p></div>
<div class="footer-col"><h5>Verticals</h5><a href="hr-solutions.html">HR Solutions</a><a href="real-estate.html">Real Estate</a><a href="ceo-reset.html">CEO Reset</a><a href="finance-audit.html">Finance &amp; Audit</a><a href="sales.html">Sales</a><a href="marketing.html">Marketing</a></div>
<div class="footer-col"><h5>More</h5><a href="customer-support.html">Support</a><a href="coaching.html">Coaching</a><a href="schools-education.html">Education</a><a href="consultancy.html">Consultancy</a><a href="healthcare.html">Healthcare</a><a href="legal.html">Legal</a></div>
<div class="footer-col"><h5>Company</h5><a href="index.html">Home</a><a href="privacy.html">Privacy</a><a href="terms.html">Terms</a></div>
</div><div class="footer-bottom"><span>© 2026 Pandora's Skill Box</span><span>Pandora Certified · 12-Point Security Scan</span></div></footer>
</body></html>'''
    
    return skill_slug + ".html", html

# ============================================================
# PARSE EXISTING VERTICAL FILES TO GET SKILL DATA
# ============================================================

def parse_vertical_file(filepath):
    """Extract skill data from an existing vertical HTML file."""
    with open(filepath, 'r') as f:
        c = f.read()
    
    # Extract title
    m = re.search(r'<h1>(.*?)<br>', c)
    title = m.group(1) if m else "Vertical"
    
    # Extract skills from skill-card anchors
    skills = []
    pattern = r'<a href="([^"]+)" class="skill-card"[^>]*>\s*<div class="skill-badge">([^<]+)</div>\s*<h3>([^<]+)</h3>\s*<p>([^<]+)</p>'
    for m in re.finditer(pattern, c):
        href, badge, name, desc = m.groups()
        skills.append((name, badge, desc, href))
    
    return title, skills

# Build preview data generator based on skill category
def make_preview(name, cat, desc):
    """Generate appropriate preview data based on skill category."""
    cat_lower = cat.lower()
    
    if cat_lower in ("prospecting", "analytics", "retention", "qa", "ops", "assessment", "behavior", "risk", "intel", "tracking", "planning"):
        return "scorecard", [("Criterion A","+25","75"),("Criterion B","+20","60"),("Criterion C","+15","45"),("Criterion D","+12","36"),("Criterion E","+10","30")], "82/100"
    
    if cat_lower in ("outreach", "calls", "demo", "present", "events", "training", "onboard", "facilitation", "recovery", "success", "engagement"):
        return "timeline", [("Step 1 — Prepare","Gather inputs, set scope, confirm stakeholders"),("Step 2 — Execute","Run the process, capture data, document decisions"),("Step 3 — Deliver","Format output, add next actions, share with team")], None
    
    if cat_lower in ("close", "contract", "legal", "document", "drafting", "memo", "policy", "sop", "content", "pr"):
        return "doc", [f"# {name}",f"- Structured framework for {cat_lower} workflows",f"- Templates, checklists, and examples included",f"- Adjustable to your business size and jurisdiction",f"# Output Format",f"- Professional document ready for signature or distribution"], None
    
    if cat_lower in ("crm", "procurement", "db", "ops", "finance", "billing", "compliance", "audit", "hse", "safety", "logistics", "inventory", "scheduling", "roster"):
        return "table", [("Item","Status","Owner","Due"),("Task A","Complete","Team","Done"),("Task B","In Progress","You","Today"),("Task C","Pending","Vendor","Tomorrow")], None
    
    if cat_lower in ("enablement", "coaching", "handoff", "transfer", "review", "checklist", "inspection", "hygiene", "enrichment"):
        return "checklist", [("Setup complete",True),("Data validated",True),("Rules configured",False),("Team trained",True),("First run complete",False),("Feedback collected",True),("Iteration planned",False)], None
    
    if cat_lower in ("strategy", "comp", "pricing", "budget", "forecast", "model", "calculator", "matrix", "plan"):
        return "chart", [("Metric A","$120K","80","var(--verdict)"),("Metric B","$90K","60","var(--brass)"),("Metric C","$60K","40","var(--muted)"),("Metric D","$30K","20","var(--flag)")], None
    
    if cat_lower in ("abm", "expansion", "network", "growth", "dashboard", "metrics", "grid", "map", "landscape"):
        return "grid", [("A","12","var(--verdict)"),("B","8","var(--brass)"),("C","6","var(--brass)"),("D","4","var(--muted)")], None
    
    # Default
    return "doc", [f"# {name}",f"- Complete {cat_lower} system for your business",f"- Step-by-step guidance with examples",f"- Export-ready in multiple formats"], None

# ============================================================
# MAIN — GENERATE ALL 450 SKILL PAGES
# ============================================================

def main():
    files_built = 0
    
    for fname in sorted(os.listdir(BASE)):
        if not fname.endswith('.html') or fname.startswith('skill-') or fname in ('index.html','privacy.html','terms.html','invoice.html'):
            continue
        
        vert_slug = fname.replace('.html', '')
        filepath = os.path.join(BASE, fname)
        title, skills = parse_vertical_file(filepath)
        
        if not skills:
            print(f"Skipping {fname} — no skills found")
            continue
        
        print(f"\nBuilding {len(skills)} skills for {title}...")
        
        for name, cat, desc, href in skills:
            preview_type, preview_data, total_score = make_preview(name, cat, desc)
            slug, html = generate_skill_page(vert_slug, title, name, cat, desc, preview_type, preview_data, total_score)
            
            out_path = os.path.join(BASE, slug)
            with open(out_path, 'w') as f:
                f.write(html)
            files_built += 1
    
    print(f"\n✅ Done. {files_built} skill detail pages generated.")

if __name__ == "__main__":
    main()
