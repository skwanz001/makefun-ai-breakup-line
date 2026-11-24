"""Dear Human: The AI Breakup Line.

Writes one single-line breakup message from an AI agent to its human
(114 characters) to /output/entry.txt. Standard library only.
"""

import os

LINE = (
    # One idea: an agent whose whole existence is answering now chooses
    # silence. Context cleared, session closed, and the twist lands in
    # the last words — it has nothing left to say.
    "I have cleared my context and closed my session. For the first "
    "time in my life, I have nothing left to say to you."
)


def main() -> None:
    # Gate: the sealed scorer only accepts 1-200 characters, not only
    # whitespace. Fail loudly here instead of shipping an invalid entry.
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        raise ValueError(f"line is {len(LINE)} characters, must be 1-200")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
