# Coral Fiber Portfolio

> A hands-on consulting toolkit built to demonstrate operational thinking for nonprofit organizations.

![Built with Claude Code](https://img.shields.io/badge/Built%20with-Claude%20Code-5C4EFA?style=flat-square)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![HTML](https://img.shields.io/badge/HTML-E34F26?style=flat-square&logo=html5&logoColor=white)

---

## About

**Coral Fiber** is a fictional nonprofit operations consultancy used as a learning context. The premise: Coral Fiber helps small nonprofits fix their operational foundations — finance, legal, HR, tooling — so they can focus on their mission.

This portfolio was built in a series of sessions using Claude Code to create real consulting tools from scratch: intake forms, scoring systems, dashboards, AI advisors, and automated reports. Everything was built through natural language prompting, iterative feedback, and critical review.

---

## What's Inside

### Consulting Tools

| File | Description |
|---|---|
| `ngo-health-check.md` | 115-point operational health check across Finance, Legal, HR, Tech, and Cultural Fit |
| `client-brief-template.md` | Reusable client brief template covering ops status, risks, 30-day plan, and open questions |
| `client-brief-shelter-the-sharks.md` | Filled client brief for fictional nonprofit "Shelter the Sharks" |
| `client-onboarding.txt` | 7-section intake questionnaire for new nonprofit clients |
| `coral-fiber-notes.txt` | Research notes on Coral Fiber's services and approach |

### Role Cards (Holacracy)

| File | Description |
|---|---|
| `role-card-template.md` | Holacracy role card template: Purpose, Domain, Accountabilities, Metrics |
| `role-card-customer-success.md` | Filled role card for Customer Success |
| `role-card-people-and-culture.md` | Filled role card for People and Culture |
| `role-card-finance-and-reporting.md` | Filled role card for Finance and Reporting |
| `role-card-legal-and-compliance.md` | Filled role card for Legal and Compliance |

### Python Scripts

| File | Description |
|---|---|
| `generate-report.py` | Asks 5 intake questions and auto-generates a markdown client summary report |
| `triage.py` | 6 yes/no questions → priority level (Critical / Urgent / Review / Stable) + timestamped log |
| `smart-advisor.py` | Connects to the Anthropic API to generate AI-powered consulting recommendations |
| `cf-advisor.py` | Conversational AI advisor with Dutch nonprofit system prompt and full conversation loop |
| `daily-briefing.py` | Reads `clients.json` and auto-generates a dated markdown briefing with urgency tiers |

### Dashboard & Data

| File | Description |
|---|---|
| `client-dashboard.html` | Browser-based client dashboard with health scores, color-coded priorities, and My Actions view |
| `clients.json` | Structured client data powering the dashboard and briefing script |
| `briefing-2026-03-17.md` | Example output from `daily-briefing.py` — critical alerts, this week, full client status |

### Logs & Reports

| File | Description |
|---|---|
| `triage-log.txt` | Auto-generated log from `triage.py` runs |
| `smart-advisor-log.txt` | Auto-generated log from `smart-advisor.py` runs |
| `cf-advisor-log.txt` | Session log from `cf-advisor.py` |
| `report-shelter-the-sharks.md` | Auto-generated client report for Shelter the Sharks |
| `learning-log.md` | Session-by-session log of concepts and insights built up over 11 sessions |

---

## Skills Demonstrated

| Skill | Applied in |
|---|---|
| **Claude Code** | All tools — built entirely through AI-assisted development |
| **Python** | `generate-report.py`, `triage.py`, `smart-advisor.py`, `cf-advisor.py`, `daily-briefing.py` |
| **APIs** | `smart-advisor.py` and `cf-advisor.py` via the Anthropic API |
| **JSON** | `clients.json` as a live data source for dashboard and briefing |
| **HTML** | `client-dashboard.html` — styled, dynamic, data-driven |
| **Git** | Version-controlled from session 8 onwards; pushed to GitHub |
| **Prompting** | System prompts, iterative refinement, role + context + task + format structuring |

---

## Built By

**Eva Schulze**
Applying for Customer Success, Consulting & Product Management at Coral Fiber

*Built across 11 sessions in March 2026 using Claude Code.*
