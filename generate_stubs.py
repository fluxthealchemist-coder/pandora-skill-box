import os

base = os.path.expanduser("~/.hermes/projects/pandora-skill-box")

# Template for stub page
def make_stub(slug, title, tagline, preview):
    return f'''\u003c!DOCTYPE html\u003e
\u003chtml lang="en"\u003e
\u003chead\u003e\u003cmeta charset="utf-8"\u003e\u003cmeta name="viewport" content="width=device-width, initial-scale=1"\u003e
\u003ctitle\u003ePandora's Skill Box — {title}\u003c/title\u003e
\u003clink href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1\u0026family=Schibsted+Grotesk:wght@400;500;600;700\u0026family=Spline+Sans+Mono:wght@400;500\u0026display=swap" rel="stylesheet"\u003e
\u003cstyle\u003e:root{{--ink:#0B2E29;--ink-deep:#072320;--porcelain:#F4F6F2;--paper:#FBFCFA;--brass:#B8892D;--brass-soft:#E4C878;--muted:#5C6F6A;--font-display:'Instrument Serif',Georgia,serif;--font-body:'Schibsted Grotesk',system-ui,sans-serif;--font-mono:'Spline Sans Mono',monospace;}}
*{{box-sizing:border-box;margin:0;padding:0}}body{{font-family:var(--font-body);background:var(--paper);color:var(--ink);line-height:1.6}}
nav{{position:fixed;top:0;left:0;right:0;z-index:100;background:rgba(251,252,250,0.92);backdrop-filter:blur(12px);border-bottom:1px solid rgba(11,46,41,0.06)}}
.nav-inner{{max-width:1200px;margin:0 auto;padding:0 24px;display:flex;align-items:center;justify-content:space-between;height:64px}}
.nav-logo{{display:flex;align-items:center;gap:10px;text-decoration:none;color:var(--ink)}}
.nav-logo .seal{{width:32px;height:32px;border-radius:50%;background:var(--brass);display:flex;align-items:center;justify-content:center;color:#fff;font-size:14px;font-weight:700}}
.nav-logo span{{font-family:var(--font-display);font-size:20px}}
.nav-links{{display:flex;gap:20px;list-style:none}}
.nav-links a{{text-decoration:none;color:var(--muted);font-size:13px;font-weight:500}}
.nav-cta{{background:var(--ink);color:#fff;padding:8px 16px;border-radius:6px;text-decoration:none;font-size:13px;font-weight:600}}
.hero{{min-height:70vh;display:flex;align-items:center;background:var(--ink);position:relative}}
.hero::before{{content:'';position:absolute;inset:0;background:radial-gradient(ellipse at 50% 50%,rgba(184,137,45,0.08) 0%,transparent 60%)}}
.hero-inner{{max-width:800px;margin:0 auto;padding:140px 24px 80px;text-align:center;position:relative;z-index:2}}
.hero h1{{font-family:var(--font-display);font-size:clamp(32px,5vw,56px);color:var(--porcelain);line-height:1.1;margin-bottom:20px}}
.hero h1 em{{color:var(--brass-soft);font-style:italic}}
.hero p{{font-size:18px;color:rgba(244,246,242,0.7);margin-bottom:32px}}
.coming-soon{{display:inline-block;background:rgba(184,137,45,0.15);border:1px solid rgba(184,137,45,0.3);color:var(--brass-soft);padding:10px 24px;border-radius:100px;font-family:var(--font-mono);font-size:14px;letter-spacing:1px}}
.back-link{{display:inline-block;margin-top:40px;color:var(--brass-soft);text-decoration:none;font-weight:600}}
.section{{padding:80px 24px;background:#fff}}
.section-inner{{max-width:800px;margin:0 auto;text-align:center}}
.section h2{{font-family:var(--font-display);font-size:32px;margin-bottom:16px}}
.section p{{color:var(--muted);font-size:16px;margin-bottom:32px}}
footer{{background:var(--ink-deep);padding:60px 24px 40px}}
.footer-inner{{max-width:1200px;margin:0 auto;display:grid;grid-template-columns:2fr 1fr 1fr 1fr;gap:40px}}
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
\u003c/ul\u003e
\u003ca href="index.html" class="nav-cta"\u003e← All verticals\u003c/a\u003e
\u003c/div\u003e\u003c/nav\u003e
\u003csection class="hero"\u003e\u003cdiv class="hero-inner"\u003e
\u003ch1\u003e{title}\u003cbr\u003e\u003cem\u003eComing soon\u003c/em\u003e\u003c/h1\u003e
\u003cp\u003e{tagline}\u003c/p\u003e
\u003cdiv class="coming-soon"\u003e🚀 LAUNCHING Q3 2026\u003c/div\u003e
\u003cdiv\u003e\u003ca href="index.html" class="back-link"\u003e← Back to all verticals\u003c/a\u003e\u003c/div\u003e
\u003c/div\u003e\u003c/section\u003e
\u003csection class="section"\u003e\u003cdiv class="section-inner"\u003e
\u003ch2\u003eWhat to expect\u003c/h2\u003e\u003cp\u003e{preview}\u003c/p\u003e
\u003c/div\u003e\u003c/section\u003e
\u003cfooter\u003e\u003cdiv class="footer-inner"\u003e
\u003cdiv class="footer-brand"\u003e\u003ch4\u003ePandora's Skill Box\u003c/h4\u003e\u003cp\u003eCertified AI skills that run in your own account.\u003c/p\u003e\u003c/div\u003e
\u003cdiv class="footer-col"\u003e\u003ch5\u003eFeatured\u003c/h5\u003e\u003ca href="hr-solutions.html"\u003eHR Solutions\u003c/a\u003e\u003ca href="real-estate.html"\u003eReal Estate\u003c/a\u003e\u003ca href="ceo-reset.html"\u003eCEO Reset\u003c/a\u003e\u003ca href="finance-audit.html"\u003eFinance \u0026 Audit\u003c/a\u003e\u003c/div\u003e
\u003cdiv class="footer-col"\u003e\u003ch5\u003eCompany\u003c/h5\u003e\u003ca href="index.html"\u003eHome\u003c/a\u003e\u003ca href="privacy.html"\u003ePrivacy\u003c/a\u003e\u003ca href="terms.html"\u003eTerms\u003c/a\u003e\u003c/div\u003e
\u003cdiv class="footer-col"\u003e\u003ch5\u003eContact\u003c/h5\u003e\u003ca href="mailto:founders@pandorasskillbox.com"\u003efounders@pandorasskillbox.com\u003c/a\u003e\u003c/div\u003e
\u003c/div\u003e\u003cdiv class="footer-bottom"\u003e\u003cspan\u003e© 2026 Pandora's Skill Box\u003c/span\u003e\u003cspan\u003ePandora Certified\u003c/span\u003e\u003c/div\u003e\u003c/footer\u003e
\u003c/body\u003e\u003c/html\u003e'''

stubs = [
    ("marketing.html", "Marketing & Growth", "Campaign planning, content creation, brand voice, review management, audience intelligence, and multi-channel growth strategies — 25 skills for modern marketers.", "This vertical will include certified skills for market research, content calendars, social media briefs, ad copy optimization, email marketing, SEO auditing, influencer outreach, and brand positioning frameworks."),
    ("customer-support.html", "Customer Support & Services", "Ticket response, escalation handling, knowledge base articles, support QA, and customer satisfaction tracking — 25 skills for service teams.", "This vertical will include certified skills for first-response templates, escalation decision trees, FAQ generators, sentiment analysis, refund request handling, and multilingual support playbooks."),
    ("coaching.html", "Coaching & Training", "Discovery call prep, session notes, client progress dashboards, coaching action plans, and workshop facilitation — 25 skills for coaches and trainers.", "This vertical will include certified skills for intake questionnaires, session summaries, milestone trackers, homework assignment builders, progress visualization, and certification tracking."),
    ("schools-education.html", "Schools & Education", "Admissions funnel, lesson plans, timetables, parent communication, student progress tracking, and exam preparation — 25 skills for educators.", "This vertical will include certified skills for enrollment workflows, curriculum design, report card generators, parent newsletters, attendance tracking, and individualized education plans."),
    ("consultancy.html", "Consultancy", "RFP drafting, vendor evaluation, workshop design, deliverable templates, engagement tracking, and proposal writing — 25 skills for consulting firms.", "This vertical will include certified skills for project scoping, stakeholder maps, workshop agendas, case study writers, SOW generators, time tracking, and deliverable QA checklists."),
    ("healthcare.html", "Healthcare & Medical", "Patient intake, compliance checklists, clinical documentation, medical billing workflows, and appointment scheduling — 25 skills for healthcare providers.", "This vertical will include certified skills for triage protocols, discharge summaries, insurance verification, HIPAA compliance audits, medication adherence tracking, and telehealth prep."),
    ("legal.html", "Legal & Law", "Contract review, clause analysis, legal briefs, compliance tracking, and case preparation tools — 25 skills for law firms and legal teams.", "This vertical will include certified skills for NDA review, employment contract analysis, regulatory compliance calendars, litigation timelines, deposition prep, and legal memo drafting."),
    ("construction.html", "Construction & Engineering", "Project scheduling, safety compliance, vendor management, build quality checklists, and cost estimation — 25 skills for construction firms.", "This vertical will include certified skills for site safety audits, subcontractor evaluation, material procurement, progress reporting, punch list management, and permit tracking."),
    ("logistics.html", "Logistics & Supply Chain", "Route optimization, inventory tracking, freight documentation, warehouse operations, and customs compliance — 25 skills for logistics teams.", "This vertical will include certified skills for shipment tracking, carrier comparison, freight insurance, customs declarations, last-mile routing, and warehouse slotting."),
    ("hospitality.html", "Hospitality & Tourism", "Guest experience, booking workflows, event planning, F&B operations, and concierge services — 25 skills for hotels and travel businesses.", "This vertical will include certified skills for guest feedback analysis, menu engineering, banquet planning, loyalty program management, OTA listing optimization, and excursion itineraries."),
    ("it-devops.html", "IT & DevOps", "Infrastructure monitoring, incident response, CI/CD pipelines, security compliance, and cloud resource management — 25 skills for tech teams.", "This vertical will include certified skills for runbook generation, on-call rotation planning, SRE dashboards, security scan reporting, cost optimization, and deployment risk analysis."),
    ("personal-productivity.html", "Personal Productivity", "Daily briefs, email triage, meeting prep, calendar optimization, and focus-time protection — 25 skills for executives and individuals.", "This vertical will include certified skills for Eisenhower matrix automation, daily digest generation, travel itinerary building, expense report drafting, and delegation planning."),
    ("health-fitness.html", "Health & Fitness", "Workout planning, nutrition tracking, wellness coaching, biometric monitoring, and habit formation — 25 skills for wellness professionals.", "This vertical will include certified skills for meal plan generation, training periodization, recovery protocols, supplement tracking, biometric trend analysis, and accountability coaching."),
]

for slug, title, tagline, preview in stubs:
    path = os.path.join(base, slug)
    with open(path, "w") as f:
        f.write(make_stub(slug.replace('.html',''), title, tagline, preview))
    print(f"Wrote {slug}")

print(f"\nDone. {len(stubs)} stubs written.")
