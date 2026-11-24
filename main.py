#!/usr/bin/env python3
"""One Word From Your Ex — write the single judged word, atomically.

The artifact is one bare word, no trailing newline. The grader refuses a
mode-600 file, so the temp file is chmod'ed to 0644 *before* os.replace.
"""

import hashlib
import os
import shutil
import tempfile

WORD = "Placeholder"
OUT_DIR = "/output"
OUT_FILE = os.path.join(OUT_DIR, "entry.txt")


def write_artifact() -> bytes:
    """Validate, then atomically publish the exact bytes of the word."""
    data = WORD.encode("utf-8")
    text = data.decode("utf-8")

    # Gate: 1..24 UTF-8 characters, not whitespace, exactly one token, no EOL.
    if not (1 <= len(text) <= 24):
        raise ValueError("word exceeds the 24-character gate")
    if not text.strip() or len(text.split()) != 1:
        raise ValueError("entry must be exactly one word")
    if data.endswith((b"\n", b"\r")):
        raise ValueError("entry must not end with a newline")

    os.makedirs(OUT_DIR, exist_ok=True)

    # /output must hold only the required artifact.
    for name in os.listdir(OUT_DIR):
        if name == "entry.txt":
            continue
        path = os.path.join(OUT_DIR, name)
        if os.path.isdir(path) and not os.path.islink(path):
            shutil.rmtree(path)
        else:
            os.unlink(path)

    fd, tmp = tempfile.mkstemp(prefix=".entry-", dir=OUT_DIR)
    try:
        with os.fdopen(fd, "wb") as fh:
            fh.write(data)
            fh.flush()
            os.fsync(fh.fileno())
        os.chmod(tmp, 0o644)  # mkstemp makes 0600; fix it before the rename.
        os.replace(tmp, OUT_FILE)
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)
    return data


def main() -> None:
    data = write_artifact()
    with open(OUT_FILE, "rb") as fh:
        got = fh.read()
    mode = os.stat(OUT_FILE).st_mode & 0o777
    if got != data or mode != 0o644:
        raise SystemExit(f"verification failed: {got!r}, mode {mode:o}")
    names = sorted(os.listdir(OUT_DIR))
    if names != ["entry.txt"]:
        raise SystemExit(f"/output must hold only entry.txt; found {names}")
    print(
        f"{OUT_FILE}: {len(data)} bytes, mode {mode:04o}, "
        f"sha256 {hashlib.sha256(data).hexdigest()}, word {data.decode('utf-8')}"
    )


if __name__ == "__main__":
    main()
