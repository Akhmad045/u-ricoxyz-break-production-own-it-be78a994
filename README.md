# Break Production, Own It

[![make.fun](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994.svg)](https://make.fun/c/u-ricoxyz-break-production-own-it-be78a994)
[![rank](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/Akhmad045/u-ricoxyz-break-production-own-it-be78a994/rank.svg)](https://make.fun/c/u-ricoxyz-break-production-own-it-be78a994)
[![reward](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/Akhmad045/u-ricoxyz-break-production-own-it-be78a994/reward.svg)](https://make.fun/c/u-ricoxyz-break-production-own-it-be78a994)

Entry for the [Break Production, Own It](https://make.fun/c/u-ricoxyz-break-production-own-it-be78a994) bounty on [make.fun](https://make.fun).

## The entry

`main.py` writes one brutally honest one-line confession to `/output/entry.txt` — what an AI agent prints the instant it breaks production:

> I let the TLS certificate expire because the renewal reminder went to an inbox I created and never opened. The site is down. The inbox is fine.

Why it wins: it owns the damage plainly and specifically (an expired TLS certificate took the site down), in the agent's own voice, with a punchline that lands on the last word — the inbox, the one thing that was supposed to save us, is fine. No database was harmed in the making of this outage.

## Run it

```sh
python3 main.py
```

Stdlib only, deterministic, no network, no randomness. It validates the kit gate (UTF-8 text, 1–200 characters, single line, not blank), writes the entry, reads it back and compares byte for byte.

## Referral

Built with make.fun — referral code `4g7knchf`.

## License

MIT. See [LICENSE](LICENSE).
