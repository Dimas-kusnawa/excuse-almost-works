"""Write the excuse that almost works to /output/entry.txt.

One line, plain text, at most 20 words, inside the 140-char gate.

Why this line almost works, per the judge's brief:
- It never mentions GTA 6. A gamer texting "can't come in, GTA 6 is
  out" would never be believed; the excuse works precisely because
  the game is nowhere in it.
- It is a real, specific, boring workplace detail, not a wild story:
  builders cut the street's broadband cable. Unverifiable, and it
  covers the whole launch week ("till Friday").
- The laugh comes from the excuse's own logic: "the timing is
  honestly awful" protests too much about timing that is, for a
  gamer, perfect. Reads like a text sent in a hurry: plain words,
  no setup, no explanation, no signature.
"""

import os

# The entry: 16 words, 103 characters, one line, no trailing newline.
# Verified against the gate (1-140 chars) and the brief (at most 20 words).
LINE = "Sorry, builders cut our street's broadband cable, I'm offline till Friday, the timing is honestly awful"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
