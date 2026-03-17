from datetime import datetime

print("=" * 50)
print("  Coral Fiber — Client Triage Tool")
print("=" * 50)
print()

client_name = input("Client name: ").strip()
print()

questions = [
    ("funder_deadline",  "1. Is there a funder deadline within the next 60 days?"),
    ("no_bookkeeping",   "2. Does the client have no bookkeeping system in place?"),
    ("outdated_contracts","3. Are legal contracts outdated or missing?"),
    ("payroll_issues",   "4. Are there current payroll issues?"),
    ("no_pm_tool",       "5. Does the client have no project management tool?"),
    ("gdpr_gap",         "6. Is there a GDPR compliance gap?"),
]

issue_labels = {
    "funder_deadline":   "Funder deadline within 60 days — financial records must be ready",
    "no_bookkeeping":    "No bookkeeping system — Finance operations cannot function without this",
    "outdated_contracts":"Outdated or missing legal contracts — legal exposure risk",
    "payroll_issues":    "Payroll issues — staff impact, must be resolved immediately",
    "no_pm_tool":        "No project management tool — team coordination and delivery at risk",
    "gdpr_gap":          "GDPR compliance gap — legal and reputational risk",
}

answers = {}
for key, question in questions:
    raw = input(f"{question} (yes/no) ").strip().lower()
    answers[key] = raw in ("yes", "y")

critical_issues = [key for key, flagged in answers.items() if flagged]
count = len(critical_issues)

if count >= 3:
    priority = "CRITICAL"
elif count == 2:
    priority = "URGENT"
elif count == 1:
    priority = "REVIEW"
else:
    priority = "STABLE"

print()
print("=" * 50)
print(f"  Priority Level: {priority}")
print(f"  Issues found: {count}")
print("=" * 50)

if critical_issues:
    print()
    print("Issues requiring immediate attention:")
    for key in critical_issues:
        print(f"  - {issue_labels[key]}")
else:
    print()
    print("No critical issues flagged. Proceed with standard onboarding.")

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
log_entry = f"""
================================================================================
Triage Report — {client_name}
Date: {timestamp}
Priority Level: {priority}
Issues Found: {count}

{"Issues Requiring Immediate Attention:" if critical_issues else "No critical issues flagged."}
{"".join(f"{chr(10)}  - {issue_labels[key]}" for key in critical_issues)}
================================================================================
"""

with open("triage-log.txt", "a", encoding="utf-8") as f:
    f.write(log_entry)

print()
print(f"Triage summary saved to triage-log.txt")
