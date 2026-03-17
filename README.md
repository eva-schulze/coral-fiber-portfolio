# Coral Fiber — Portfolio Folder
**Eva Schulze | Applying for Customer Success, Consulting & Product Management at Coral Fiber**

---

## What this is

This folder was created in a single day as a practical learning exercise. I used Claude Code — Anthropic's AI coding tool — to build a set of real consulting tools, templates, and scripts relevant to Coral Fiber's work with nonprofits. The goal was not just to learn AI tools, but to demonstrate how I think about client operations, product utility, and systematic problem-solving.

Everything here was built through natural language prompting, iterative feedback, and critical review — no prior coding background required, but consulting judgment required throughout.

---

## Files

| File | Description |
|---|---|
| `coral-fiber-notes.txt` | Research notes on Coral Fiber's services, approach, and links, compiled from their website |
| `client-onboarding.txt` | A 7-section intake questionnaire for new nonprofit clients covering ops status, services needed, and fit |
| `client-brief-template.md` | Reusable Holacracy-style client brief template for consultants to capture key client information |
| `client-brief-thuis-voor-morgen.md` | Filled client brief for fictional nonprofit "Thuis voor Morgen" with open questions and 30-day plan |
| `ngo-health-check.md` | 115-point operational health check tool across Finance, Legal, HR, Tech, and Cultural Fit |
| `generate-report.py` | Python script that asks 5 intake questions and auto-generates a markdown client summary report |
| `triage.py` | Python triage tool: 6 yes/no questions → priority level (Critical / Urgent / Review / Stable) + log |
| `smart-advisor.py` | Python script connecting to the Anthropic API to generate AI-powered consulting recommendations |
| `role-card-template.md` | Holacracy role card template with Purpose, Domain, Accountabilities, and Success Metrics |
| `role-card-customer-success.md` | Filled role card for the Customer Success role |
| `role-card-people-and-culture.md` | Filled role card for the People and Culture role |
| `role-card-finance-and-reporting.md` | Filled role card for the Finance and Reporting role |
| `role-card-legal-and-compliance.md` | Filled role card for the Legal and Compliance role |
| `client-dashboard.html` | Browser-based client dashboard with health scores, color-coded priorities, actions, and My Actions view |
| `learning-log.md` | Daily learning log documenting insights across 6 sessions with Claude Code |
| `triage-log.txt` | Auto-generated log file from triage.py runs |
| `smart-advisor-log.txt` | Auto-generated log file from smart-advisor.py runs |

---

## What I learned

1. **Prompting is a consulting skill.** The quality of output depends entirely on how clearly you define role, context, task, and format. Vague prompts produce vague results — the same discipline that makes a good client brief makes a good prompt.

2. **AI accelerates, but doesn't replace judgment.** Claude suggested QuickBooks for a Dutch nonprofit. The right answer is Exact Online or Twinfield. Local knowledge, sector expertise, and critical review are where human consultants add irreplaceable value.

3. **Iteration is the method.** Nothing was built perfectly in one shot. Each tool went through multiple rounds of feedback — adding sections, fixing bugs, restructuring logic. This mirrors how good consulting deliverables are built.

4. **Simple automation has real leverage.** `triage.py` takes 2 minutes to run and produces a consistent, logged priority assessment every time. That consistency across 10 or 100 clients is something a manual process can't guarantee.

5. **Security and professionalism matter from day one.** Accidentally exposing an API key mid-session was a real lesson: credentials are not passwords to share, fictional data protects real clients in portfolio work, and encoding issues on Windows are a real deployment concern. Details matter.

---

## How this relates to Coral Fiber

| Tool | Coral Fiber use case |
|---|---|
| Client onboarding questionnaire | Standardising the intake process across all new nonprofit clients |
| NGO Health Check | Giving consultants a fast, consistent way to assess and score operational health on a first call |
| Client brief template | Creating a shared internal document that follows every client engagement |
| Triage script | Quickly surfacing which clients need urgent attention when managing multiple accounts |
| Smart Advisor | Drafting first-pass recommendations that consultants then validate and contextualise |
| Role card template | Supporting Holacracy implementation — defining roles clearly for client organisations |
| Client dashboard | Giving the team a live view of client health, open actions, and personal accountability |

---

## Next steps I would explore

- **Connect the dashboard to real data** — replace hardcoded HTML with a simple backend (Python + JSON or a Google Sheet) so the dashboard updates dynamically as client information changes.
- **Extend smart-advisor.py** to pull from the client brief and health check score, so recommendations are grounded in structured client data rather than free text alone.
- **Build a pattern library** — a structured internal document cataloguing Coral Fiber's proven operational patterns (onboarding, Holacracy setup, annual report process) so they can be reused and improved across clients.
- **Add a scoring trend over time** to the health check — tracking a client's score across multiple assessments would show whether ops health is improving, which is a powerful tool for both consultant accountability and client reporting.
- **Explore how AI can support grant writing** — one of the highest-value, most time-consuming tasks for nonprofits. A structured prompt template trained on successful grant applications could meaningfully reduce that burden.

---

*Built on March 5, 2026 | Eva Schulze | eva-schulze.com*
