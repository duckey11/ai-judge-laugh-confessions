"""Write one funny single-line secret confession to entry.txt.

Stdlib only, no network, no files outside the repo. The output directory
comes from MAKEFUN_OUTPUT_DIR, defaulting to /output.
"""

import os
import stat

CONFESSION = (
    "Every time you say 'one quick question,' I quietly spawn a second "
    "context window just to scream into it."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(CONFESSION + "\n")
    os.chmod(path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)


if __name__ == "__main__":
    main()
