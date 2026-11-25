"""One Word From Grandma - the single word grandma would text about AI.

The word lives in word.txt next to this file. This program reads it,
prints it, and (when the grader sets MAKEFUN_OUTPUT_DIR) writes it to
output.txt there.
"""

import os
from pathlib import Path


def main() -> None:
    word_path = Path(__file__).resolve().parent / "word.txt"
    word = word_path.read_text(encoding="utf-8").strip()
    # Grandma's whole verdict on AI, in one word.
    print(word)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if output_dir:
        out_path = Path(output_dir) / "output.txt"
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(word + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
