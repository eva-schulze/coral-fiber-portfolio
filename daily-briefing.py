import json
from datetime import date, timedelta

today = date.today()
filename = f"briefing-{today}.md"

with open("clients.json", encoding="utf-8") as f:
    data = json.load(f)

clients = data["clients"]

critical_alerts = []
this_week = []

for client in clients:
    for action in client["actions"]:
        entry = {
            "client": client["name"],
            "task": action["task"],
            "owner": action["owner"],
            "due_date": today + timedelta(days=action["due_days"]),
            "due_days": action["due_days"],
        }
        if action["due_days"] <= 7:
            critical_alerts.append(entry)
        elif action["due_days"] <= 14:
            this_week.append(entry)

lines = []

lines.append(f"# Coral Fiber Daily Briefing")
lines.append(f"**Date:** {today.strftime('%B %d, %Y')}  ")
lines.append(f"**Total clients:** {len(clients)}")
lines.append("")

# Critical alerts
lines.append("---")
lines.append("")
lines.append("## CRITICAL ALERTS — Due within 7 days")
lines.append("")
if critical_alerts:
    for a in sorted(critical_alerts, key=lambda x: x["due_days"]):
        lines.append(f"- **{a['client']}** | {a['task']} | Owner: {a['owner']} | Due: {a['due_date']} ({a['due_days']}d)")
else:
    lines.append("_No critical actions this week._")
lines.append("")

# This week
lines.append("---")
lines.append("")
lines.append("## THIS WEEK — Due within 14 days")
lines.append("")
if this_week:
    for a in sorted(this_week, key=lambda x: x["due_days"]):
        lines.append(f"- **{a['client']}** | {a['task']} | Owner: {a['owner']} | Due: {a['due_date']} ({a['due_days']}d)")
else:
    lines.append("_No additional actions due this week._")
lines.append("")

# Full client status
lines.append("---")
lines.append("")
lines.append("## FULL CLIENT STATUS")
lines.append("")
for client in clients:
    score_pct = round(client["score"] / client["score_max"] * 100)
    lines.append(f"### {client['name']}")
    lines.append(f"**Health score:** {client['score']}/{client['score_max']} ({score_pct}%)  ")
    lines.append(f"**Status:** {client['status']}")
    if client["issues"]:
        lines.append("")
        lines.append("**Issues:**")
        for issue in client["issues"]:
            lines.append(f"- {issue}")
    if client["actions"]:
        lines.append("")
        lines.append("**Open actions:**")
        for action in client["actions"]:
            due = today + timedelta(days=action["due_days"])
            lines.append(f"- {action['task']} ({action['owner']}) — due {due}")
    lines.append("")

# Closing
lines.append("---")
lines.append("")
lines.append("_Coral Fiber — Tested across organizations, not invented for yours._")

with open(filename, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print(f"Briefing created: {filename}")
