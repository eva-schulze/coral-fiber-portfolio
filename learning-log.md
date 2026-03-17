# Learning Log

## March 17, 2026 — Session 8: Git Version Control

**Context:** Returning after a few days' pause — learning Git to publish the portfolio.

- **Git is version control for your project** — it tracks every change you make to files over time, so you can see what changed, when, and why. Think of it as a detailed save history that never forgets anything.
- **Initialized a Git repository and made the first commit** — ran `git init` to start tracking the project, then committed 19 files in one go. That first commit is the baseline — everything from here is a recorded change on top of it.
- **Pushed the portfolio to GitHub as coral-fiber-portfolio** — GitHub is the remote home for the repository, accessible from anywhere. Pushing sends your local commits to that remote so others (or interviewers) can see the work.
- **The three core Git commands: add, commit, push** — `git add` stages the files you want to include, `git commit` saves a snapshot with a message explaining what changed, and `git push` sends it to GitHub. That sequence is the entire publish workflow for most projects.
- **API keys must never be committed to a public repository** — once a key is in a public commit, it is exposed — even if you delete it later, the history remains. The rule is simple: keys go in environment variables or a `.env` file that is listed in `.gitignore`, never in the code itself.

---

## March 5, 2026 — Session 7: Interview Prep & Portfolio Completion

**Context:** Final session — completing the portfolio and preparing for the Moral Fabric interview.

- **Completed three role cards using Holacracy structure** — People and Culture, Finance and Reporting, and Legal and Compliance. Each card defines Purpose, Domain, Accountabilities, and Success Metrics. Building these made the distinction between roles, tasks, and accountabilities concrete rather than theoretical.
- **Role cards are a thinking tool, not just a document** — writing the accountabilities forces you to distinguish between what a role *does* (recurring) and what someone *delivers* (one-off). That clarity is exactly what Holacracy is designed to create, and building these cards made that click.
- **Completed a full interview simulation with honest feedback** — went through realistic interview questions for the Customer Success and Consulting role and received direct feedback on what wasn't working.
- **Key personal lesson: structure and concrete examples, not stream of consciousness** — strong interview answers follow a clear shape (situation → what I did → result), stay concise, and are grounded in a specific real example. Long, unstructured answers lose the interviewer even when the content is good. Authenticity matters, but so does discipline.
- **Built the README as a portfolio overview** — the README ties everything together: what was built, what was learned, how it connects to Moral Fabric's actual work, and where I would take it next. A portfolio without a narrative is just a folder of files.

---

## March 5, 2026 — Session 6: HTML Dashboard & Portfolio Thinking

**Context:** Preparing for a Customer Success & Consulting role at Moral Fabric.

- **Built a professional client dashboard in HTML** — a fully styled, browser-ready dashboard showing 3 nonprofit clients with health scores out of 115, color-coded priority badges (red/yellow/green), issues lists, and open actions per client. No external libraries — pure HTML and CSS.
- **Color coding communicates urgency instantly** — using consistent colors (red = Critical, yellow = Review, green = Stable) across badges, progress bars, action due dates, and the My Actions panel means a consultant can read the dashboard in seconds without processing text.
- **Role-based ownership, not person-based** — actions are assigned to roles (Finance Lead, Legal Lead, Customer Success) rather than names, which aligns with Holacracy thinking and keeps the dashboard useful even as team members change.
- **My Actions view = personal accountability layer** — filtering actions by role across all clients gives the Customer Success an at-a-glance view of what they personally own, sorted by urgency. This is the difference between a status report and a working tool.
- **Use fictional data to protect real clients in portfolio work** — when building demos, case studies, or portfolio pieces, replace real client names with fictional alternatives (e.g. "Shelter the Sharks") to showcase the work without exposing confidential information. A small habit with a big professional impact.

---

## March 5, 2026 — Session 5: APIs, AI Integration & Critical Review

**Context:** Preparing for a Customer Success & Consulting role at Moral Fabric.

- **An API is a bridge between two software systems** — when `smart-advisor.py` runs, it sends a request to Anthropic's servers over the internet and gets a response back. The API key is the credential that proves you're allowed to use it. This is how modern tools connect and share capabilities without sharing their underlying code.
- **Built smart-advisor.py** — a script that takes a free-text description of a client's operational challenge, sends it to Claude via the Anthropic API with a Moral Fabric consultant persona, and returns 3 specific recommendations. Results are printed to the terminal and logged to `smart-advisor-log.txt`.
- **AI output always needs critical review for local context** — Claude may suggest tools or approaches that are technically correct but wrong for the specific context. Example: recommending QuickBooks or Xero for a Dutch nonprofit, when the standard in the Netherlands is Exact Online or Twinfield. AI gives a strong starting point, but the consultant must validate against local regulations, market norms, and client reality.
- **Security lesson: never share API keys in plain text** — API keys are credentials, not passwords to be typed in public. If exposed (in chat, in code, in a file), they must be revoked immediately and regenerated. Set them as environment variables in the terminal, not hardcoded in scripts.
- **The consultant's role doesn't disappear with AI** — AI accelerates research and drafting, but judgement, local knowledge, and client relationships remain human responsibilities. The value shifts from "producing the answer" to "knowing which answer is right."

---

## March 5, 2026 — Session 4: Holacracy, Role Cards & Automation

**Context:** Preparing for a Customer Success & Consulting role at Moral Fabric.

- **Holacracy is role-based, not people-based** — in traditional orgs, responsibilities follow the person ("ask Eva, she handles clients"). In Holacracy, responsibilities belong to a role. The person fills the role, but the role exists independently — it can be reassigned, split, or left vacant. This creates clarity and reduces single-person dependencies.
- **A role card has four core elements** — Purpose (why the role exists), Domain (what it has exclusive control over), Accountabilities (ongoing responsibilities, always phrased as verbs), and Metrics (how you know the role is being fulfilled). Each element answers a distinct question and cannot substitute for another.
- **Accountabilities are recurring, not one-off** — a task is something you do once; an accountability is something you keep doing. "Set up onboarding document" is a task. "Managing client onboarding from contract to handover" is an accountability. The distinction matters for role clarity.
- **Built a reusable role card template and Customer Success example** — the filled example made the abstract structure concrete: 7 accountabilities, a defined domain, and 5 measurable success metrics. A practical tool for any new Moral Fabric role definition.
- **Built triage.py — automated client prioritization** — a 6-question yes/no script that counts critical issues and assigns a priority level (CRITICAL / URGENT / REVIEW / STABLE), lists specific issues with plain-English descriptions, and appends a timestamped entry to a running `triage-log.txt`. Multiple clients accumulate in one log over time.
- **Automation reduces consultant cognitive load** — instead of mentally weighing six risk factors on a call, the script does it consistently every time. This is a small example of how patterns + tools scale consulting work across more clients without losing quality.

---

## March 5, 2026 — Session 3: Building Tools & Debugging

**Context:** Preparing for a Customer Success & Consulting role at Moral Fabric.

- **Iterative prompting includes critical feedback** — good prompting isn't just refining tone or length; it also means pushing back on structure, adding complexity (like a Cultural Fit section), and layering requirements across multiple rounds. The output gets significantly better with each pass.
- **Built the NGO Health Check tool** — a 115-point consultant scoring tool across 5 sections: Finance (Critical), Legal (High), HR (Medium), Tech (Medium), and Cultural & Strategic Fit. Added internal-only sections for contact notes and pattern learning, making it useful both for client assessment and internal knowledge building.
- **Cultural fit is a separate signal** — scoring Finance and HR is straightforward, but whether a client operates with autonomy, uses data, and is open to new patterns determines whether Moral Fabric's approach will actually land. A "No" on any cultural fit question is a red flag regardless of the total score.
- **Built a Python script from scratch** — `generate-report.py` asks 5 intake questions and auto-generates a formatted markdown client report. No external libraries — just Python's built-in `datetime` and file I/O. Practical proof that AI + simple code can automate real consulting tasks.
- **Fixed a real Windows bug** — the script failed on Windows due to emoji characters causing a `UnicodeEncodeError`. Fix: replace emojis with plain text alternatives and explicitly set `encoding="utf-8"` when writing files. A small but important lesson in platform-specific behaviour.

---

## March 5, 2026 — Session 2: Prompting, Markdown & Consulting Practice

**Context:** Preparing for a Customer Success & Consulting role at Moral Fabric.

- **Markdown is a lightweight formatting language** — using `#` for headings, `|` for tables, `-` for bullet points, and `**bold**` makes documents readable both as plain text and when rendered, which is useful for internal templates and client-facing docs.
- **A good prompt has 4 ingredients: Role, Context, Task, Format** — being explicit about who Claude should act as, what the situation is, what you need done, and how the output should look leads to dramatically better results.
- **Iterative prompting is the real skill** — you rarely get the perfect output in one shot. The workflow is: start broad, review, then refine with follow-up instructions (e.g. "make it shorter", "add a section", "change the tone").
- **Templates are multipliers** — building a reusable client brief template means every future client onboarding starts from a strong foundation, not a blank page. Good consulting thinking lives in the structure, not just the content.
- **Applied practice: Thuis voor Morgen** — filled in the client brief template for a fictional Amsterdam nonprofit, translating messy real-world details (Excel chaos, outdated contracts, 60-day funder deadline) into a structured, actionable document.
- **Consulting instinct: surface what's missing** — added a "Missing Information & Open Questions" section with a status table, which reflects a core consulting habit: identifying blockers and assigning ownership before work begins.

---

## March 5, 2026 — Session 3: Product Owner Thinking at Moral Fabric

**Context:** Connecting consulting practice to a potential Product Owner role.

- **Product Management at Moral Fabric in three steps** — (1) collect client feedback: which Finance features are missing? (2) identify patterns: what do all NGO clients do the same way? (3) build it into the product so it scales. That's the full PM loop in one observation.
- **Finance has high relevance as a starting point** — it's the most urgent pain point for most nonprofit clients (as seen with Thuis voor Morgen), which makes it the highest-signal area for discovering what to build next.
- **The PO role bridges consulting and product** — working directly with clients surfaces real needs; the PO job is to turn those needs into patterns, and those patterns into scalable features. Client work is not separate from product work — it *feeds* it.
- **Patterns = proven ways of doing things** — a pattern is a repeatable process that has been tested across multiple organizations. Moral Fabric describes it as: *"Tested across organizations, not invented for yours."* Examples: the client onboarding process, how to introduce Holacracy, how to produce an annual report. Think of it as a best-practice workflow, not just a document.
- **Policies = clear rules about what is required, allowed, or forbidden** — not a process, but a boundary. Examples: "All contracts must be reviewed before signing", "New staff get tool access in week 1", "Financial reports are due by the 5th of each month." Think of it like internal company guidelines (HR policy, travel expenses policy, GDPR policy).
- **Pattern vs. Policy in one sentence** — a Pattern defines *how we do it* (e.g. onboarding in 6 steps); a Policy defines *what the rule is* (e.g. every new client signs a contract first).

---

## March 5, 2026 — Getting Started with Claude Code

**Context:** Preparing for a Customer Success & Consulting role at Moral Fabric.

- **Claude Code runs in your terminal** — you launch it with the `claude` command inside any project folder, making it easy to work on real files in context, just like a developer would.
- **You can give it natural language instructions** — instead of writing code yourself, you describe what you need (a questionnaire, a notes file, a welcome email) and Claude handles the execution, including researching content from the web.
- **It reads and edits files directly** — Claude can create, update, and review files in your project folder, which means documentation, templates, and client materials can be built and refined in real time.
- **It's useful beyond engineering** — for a Customer Success role, Claude Code can help draft onboarding documents, research clients, write emails, and organize information, all without needing technical skills to get started.
- **Context carries across a session** — Claude remembers everything discussed earlier in the conversation, so you can build on previous work (like adding details to a notes file or shortening an email) without repeating yourself.
