"""One short joke about office life, 200 characters at most.

The program writes exactly that line and nothing else to /output/entry.txt.
"""

import os

TEXT = "My calendar invited me to a meeting about why I never have time for meetings, and I had to decline because of a meeting."


def main():
    assert 1 <= len(TEXT) <= 200, len(TEXT)
    assert TEXT == TEXT.strip()
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
