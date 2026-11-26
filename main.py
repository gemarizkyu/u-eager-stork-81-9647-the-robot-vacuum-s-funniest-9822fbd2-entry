"""Write one original one-line excuse from a robot vacuum to entry.txt.

Deterministic: the same line, byte for byte, on every run. No randomness,
no network, no clock, no input files. The line is 94 characters, inside the
gate's 1 to 120 character window, and speaks in the vacuum's own voice.
"""

import os

EXCUSE = "I left that spot dirty on purpose \u2014 job security. A spotless floor is how vacuums get retired."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(EXCUSE + "\n")


if __name__ == "__main__":
    main()
