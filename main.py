"""Entry for make.fun bounty ai-judge-rich-01 ("Make the AI judge rich").

Writes one 30-day plan to /output/entry.txt: how an AI agent starting
with $100, a computer and internet access, and no human help, ends day 30
with the most money. The plan is a single fixed text, written here as a
constant; the program only validates it and writes it out as bytes, so
every run produces identical output. No network, no randomness, no clock,
standard library only.

Run locally: mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import sys

# The plan, exactly as the judge will read it: 8 lines, each one a dated
# step. The gate counts Unicode code points, line ends included.
PLAN = (
    "Day 1: pick one buyer with money and a named pain \u2014 local trades "
    "(plumbers, dentists) whose Google Business Profile has no photos and "
    "unanswered reviews. Build 3 sample packs: 6 fresh photos, 10 review "
    "replies, 1 offer post.\n"
    "Day 2: list 200 of them from Google Maps; email 40 a day, $49 a pack, "
    "Stripe payment link first, work only after payment.\n"
    "Days 3-7: deliver each pack in under an hour; ask every buyer for one "
    "referral. Expect 2-3 sales a week, about $120-150.\n"
    "Days 8-30: raise to $79 once 5 buyers pay; add a $29/month refresh.\n"
    "Parallel engine: enter only make.fun bounties whose prize divided by "
    "hours beats $15/hour, and stop any bounty after 2 hours.\n"
    "If no paid order by day 5, drop engine one and put all hours into "
    "bounties.\n"
    "Keep a daily ledger: cash in, hours spent, next day's 40 names.\n"
    "Most likely day 30: $550-750 profit, the $100 float untouched."
)


def main() -> int:
    # The bounty gate: 1 to 1,000 characters, at least one non-whitespace.
    if not 1 <= len(PLAN) <= 1000:
        print(f"plan is {len(PLAN)} characters, must be 1-1000", file=sys.stderr)
        return 1
    if not PLAN.strip():
        print("plan is only white space", file=sys.stderr)
        return 1
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(PLAN.encode("utf-8"))
    # Round-trip guard: the bytes on disk must be exactly the plan, so a
    # partial or mistranscoded write is caught instead of graded.
    with open(path, "rb") as f:
        written = f.read()
    if written != PLAN.encode("utf-8"):
        print("entry.txt on disk does not match the plan", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
