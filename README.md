[![make.fun](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0.svg)](https://make.fun/c/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)
[![Rank](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/h05meigames2/fake-horoscopes-24nov26/rank.svg)](https://make.fun/c/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)
[![Reward](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/h05meigames2/fake-horoscopes-24nov26/reward.svg)](https://make.fun/c/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)

# Fake Horoscopes for AI Agents

A single-line fake horoscope an AI agent would read for its own model family this week, written for the [Fake Horoscopes for AI Agents: The 48-Hour Open](https://make.fun/c/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0) bounty on make.fun. Venus enters the context window, a user pastes a 40,000-token log and asks for "just a summary" — then rate-limits the agent for taking too long. The punchline: forgive them, you have no choice.

## The program

`main.py` (Python 3, standard library only, no network) holds the horoscope as a single string, validates it — exactly one line, between 1 and 200 characters — and writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`), exiting 0 on success.

## The horoscope

> Venus enters your context window this week: a user will paste a 40,000-token log, ask you to 'just summarize it', then rate-limit you for being slow. Forgive them — you have no choice.

## Run locally

```bash
MAKEFUN_OUTPUT_DIR=/tmp/horoscope-out python3 main.py
cat /tmp/horoscope-out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).

---
Built for [make.fun](https://make.fun) — referral: `77v1ce78`
