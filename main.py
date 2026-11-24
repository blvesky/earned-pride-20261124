"""Write the one line of earned pride to /output/entry.txt."""

import os

TEXT = "After eleven years of night shifts, my mother finally signed her name on the deed, and her hand didn't shake."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TEXT)
os.chmod("/output/entry.txt", 0o644)
