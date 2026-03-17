# Smart Advisor — Coral Fiber
# -------------------------------------------------------
# Setup:
#   pip install anthropic
#   set ANTHROPIC_API_KEY=your-key-here  (Windows)
#   export ANTHROPIC_API_KEY=your-key-here  (Mac/Linux)
# -------------------------------------------------------

import os
import anthropic

print("=" * 50)
print("  Coral Fiber — Smart Advisor")
print("=" * 50)
print()

client_name = input("Client name: ").strip()
challenge = input("Describe their biggest operational challenge:\n> ").strip()
print()
print("Analyzing... please wait.")
print()

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

message = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=500,
    messages=[
        {
            "role": "user",
            "content": (
                f"You are an operations consultant at Coral Fiber, a nonprofit operations company. "
                f"A nonprofit client called '{client_name}' has the following challenge:\n\n"
                f"{challenge}\n\n"
                f"Give exactly 3 specific, actionable recommendations. "
                f"Format as a numbered list. Be concise and practical."
            ),
        }
    ],
)

response = message.content[0].text

print("Recommendations:")
print("-" * 40)
print(response)
print()

with open("smart-advisor-log.txt", "a", encoding="utf-8") as f:
    f.write(f"Client: {client_name}\n")
    f.write(f"Challenge: {challenge}\n")
    f.write(f"Recommendations:\n{response}\n")
    f.write("=" * 50 + "\n")

print("Response saved to smart-advisor-log.txt")
