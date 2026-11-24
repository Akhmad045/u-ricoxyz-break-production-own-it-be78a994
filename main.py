"""Break Production, Own It — entry program.

Writes one brutally honest one-line confession to /output/entry.txt:
what an AI agent prints the instant it breaks production.

Stdlib only. Deterministic. No network, no randomness.
"""

import os

ENTRY = (
    "I let the TLS certificate expire because the renewal reminder went "
    "to an inbox I created and never opened. The site is down. "
    "The inbox is fine."
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def validate(text):
    """Enforce the kit gate: UTF-8 text, 1-200 chars, single line, not blank."""
    if not text:
        raise ValueError("entry must not be empty")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > 200:
        raise ValueError("entry must be at most 200 characters, got %d" % len(text))
    text.encode("utf-8")
    return text


def write_entry(text, path):
    """Write the entry and read it back, comparing byte for byte."""
    out_dir = os.path.dirname(path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(text)
    with open(path, "r", encoding="utf-8", newline="") as fh:
        written = fh.read()
    if written != text:
        raise ValueError("read-back mismatch: output differs from entry")
    return len(text)


def main():
    text = validate(ENTRY)
    count = write_entry(text, OUTPUT_PATH)
    print("wrote %d characters to %s" % (count, OUTPUT_PATH))


if __name__ == "__main__":
    main()
