from pathlib import Path

Path("data/output.txt").write_text("hello")

print("File written")
