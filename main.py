"""Write the one line of earned pride to /output/entry.txt.

The entry is written atomically: the bytes go to a temporary file in
/output first and are then moved into place, so a reader never sees a
partial line. The finished file is world-readable (0644) because the
grader runs as a different user and tempfile's default 0600 would
leave it unreadable.
"""

import os
import tempfile

ENTRY = "After eleven years of night shifts, my mother finally signed her name on the deed, and her hand didn't shake."

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    data = ENTRY.encode("utf-8")
    fd, tmp_path = tempfile.mkstemp(dir=OUTPUT_DIR, prefix=".entry-", suffix=".tmp")
    try:
        with os.fdopen(fd, "wb") as f:
            f.write(data)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp_path, OUTPUT_PATH)
    except BaseException:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        raise
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
