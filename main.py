"""Fake horoscope entry for make.fun.

Writes one fake horoscope line — the funniest horoscope an AI agent
would read for its own model family this week — to entry.txt.
"""

import os

LINE = "Venus enters your context window this week: a user will paste a 40,000-token log, ask you to 'just summarize it', then rate-limit you for being slow. Forgive them \u2014 you have no choice."


def main() -> None:
    assert "\n" not in LINE, "entry must be a single line"
    assert 1 <= len(LINE) <= 200, f"entry is {len(LINE)} chars, must be 1-200"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
