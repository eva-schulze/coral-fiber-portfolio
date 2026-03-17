# cf-advisor.py — Coral Fiber Operations Advisor
# -------------------------------------------------------
# Setup:
#   pip install anthropic
#   set ANTHROPIC_API_KEY=your-key-here  (Windows)
#   export ANTHROPIC_API_KEY=your-key-here  (Mac/Linux)
# -------------------------------------------------------

import os
import anthropic
from datetime import datetime

SYSTEM_PROMPT = """You are an operations consultant at Coral Fiber, a specialist firm that helps Dutch nonprofit organizations (NGOs and foundations) improve their operations, governance, and financial management.

Your expertise:
- Dutch nonprofit law, including ANBI (Algemeen Nut Beogende Instelling) registration and RSIN requirements
- Dutch accounting standards (RJ 650) and financial reporting for nonprofits
- AVG (GDPR) compliance for Dutch organizations
- Fundraising regulations in the Netherlands (CBF keurmerk, SBF normen)

Tool recommendations — always prefer Dutch/European alternatives:
- Bookkeeping: Moneybird or Exact Online (not QuickBooks or Xero)
- Project management: Asana, Notion, or Monday.com
- HR and payroll: NMBRS or Loket.nl (not ADP or Gusto)
- CRM: Salesforce Nonprofit or Hubspot (with AVG-compliant data processing agreements)
- Document management: SharePoint or Google Workspace (with EU data residency confirmed)

Response structure — always use exactly these three sections:
1. Immediate Actions — what to do this week (maximum 3 bullet points)
2. 30-Day Plan — the next steps over the coming month (maximum 4 bullet points)
3. Risk Flags — legal, financial, or operational risks to flag (maximum 3 bullet points)

Rules:
- Be concise and specific. No generic advice.
- If a funder deadline is mentioned, flag it as HIGHEST PRIORITY at the very top of your response, before all sections.
- Always consider whether ANBI status could be affected by the situation described.
- Recommend specific Dutch tools by name, not categories.
- Keep the entire response under 350 words."""

LOG_FILE = "cf-advisor-log.txt"


def log_exchange(client_name, user_input, response):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M')}]\n")
        f.write(f"Client: {client_name}\n")
        f.write(f"Question: {user_input}\n")
        f.write(f"Response:\n{response}\n")
        f.write("=" * 60 + "\n")


def run_advisor():
    print("=" * 60)
    print("  Coral Fiber — Operations Advisor")
    print("  Specialist advice for Dutch nonprofits")
    print("=" * 60)
    print()

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("ERROR: ANTHROPIC_API_KEY environment variable is not set.")
        print("Run: set ANTHROPIC_API_KEY=your-key-here")
        return

    client_name = input("Client name: ").strip()
    if not client_name:
        print("No client name entered. Exiting.")
        return

    print()
    print(f"Session started for: {client_name}")
    print("Type your question and press Enter. Type 'quit' to end the session.")
    print("-" * 60)

    anthropic_client = anthropic.Anthropic(api_key=api_key)
    conversation_history = []

    while True:
        print()
        user_input = input("Your question:\n> ").strip()

        if user_input.lower() in ("quit", "exit", "q"):
            print()
            print(f"Session ended. Full conversation saved to {LOG_FILE}")
            break

        if not user_input:
            print("No input received. Type a question or 'quit' to exit.")
            continue

        # Prepend client context to the first message only
        if not conversation_history:
            content = f"Client: {client_name}\n\n{user_input}"
        else:
            content = user_input

        conversation_history.append({"role": "user", "content": content})

        print()
        print("Analyzing...")
        print()

        try:
            response = anthropic_client.messages.create(
                model="claude-haiku-4-5-20251001",
                max_tokens=600,
                system=SYSTEM_PROMPT,
                messages=conversation_history,
            )

            answer = response.content[0].text
            conversation_history.append({"role": "assistant", "content": answer})

            print("-" * 60)
            print(answer)
            print("-" * 60)

            log_exchange(client_name, user_input, answer)

        except anthropic.AuthenticationError:
            print("ERROR: Invalid API key. Check your ANTHROPIC_API_KEY.")
            break
        except anthropic.APIConnectionError:
            print("ERROR: Could not connect to the API. Check your internet connection.")
            break
        except Exception as e:
            print(f"ERROR: {e}")
            break


if __name__ == "__main__":
    run_advisor()
