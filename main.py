"""Entry for the make.fun bounty "The Most Boring Object, Reviewed in One Line".

The program writes a single funny line to /output/entry.txt. The
review is of a rubber band, the dullest everyday object: five stars,
because it has held the reviewer's life together since 1998 and asked
for nothing, not even a thank-you. The review is true as well as
funny: the rubber band really does that job, silently, for
decades. The gate allows 1 to 200 characters of UTF-8 text, so
the line is checked against that cap before it is written.
"""

import os

ENTRY = (
    "The rubber band: five stars. It has held my life together since "
    "1998 and asked for nothing, not even a thank-you."
)

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be empty"
    assert "\n" not in text, "entry must be a single line"
    assert len(text) <= MAX_CHARS, (
        f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
    )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
