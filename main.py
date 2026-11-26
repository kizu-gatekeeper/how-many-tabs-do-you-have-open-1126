"""Entry for make.fun: How Many Tabs Do You Have Open?

One honest number, digits only: a count high enough to be a confession,
specific enough to be true.
"""
import os

LINE = "347"
MAX_CHARS = 5


def write_entry(out_dir):
    assert LINE.isdigit(), "entry must be digits only"
    assert LINE.strip() and "\n" not in LINE and len(LINE) <= MAX_CHARS
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


def main():
    write_entry(os.environ.get("MAKEFUN_OUTPUT_DIR", "."))


if __name__ == "__main__":
    main()
