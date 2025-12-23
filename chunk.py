from pathlib import Path
import re


PARSED_FILE = Path("parsed/rn-performance-optimization.full.md")
CHUNKS_DIR = Path("chunks")


PART_RE = re.compile(r"^PART\s+\d+", re.IGNORECASE)
CHAPTER_RE = re.compile(r"^CHAPTER\s+\d+", re.IGNORECASE)
ISSUE_RE = re.compile(r"^ISSUE:", re.IGNORECASE)
SOLUTION_RE = re.compile(r"^SOLUTION:", re.IGNORECASE)
ALL_CAPS_RE = re.compile(r"^[A-Z0-9 ,.'\":;()\-\–&]{6,300}$")


def normalize_heading(line: str) -> str:
    stripped = line.strip()

    if not stripped.startswith("#"):
        return line.rstrip()

    raw = stripped.lstrip("#").strip()

    if PART_RE.match(raw):
        return f"# {raw}"

    if CHAPTER_RE.match(raw):
        return f"## {raw}"

    if ISSUE_RE.match(raw):
        return f"#### {raw}"

    if SOLUTION_RE.match(raw):
        return f"#### {raw}"

    if ALL_CAPS_RE.match(raw):
        return f"### {raw}"

    return line.rstrip()


def chapter_filename(chapter_title: str) -> str:
    match = re.search(r"CHAPTER\s+(\d+)", chapter_title, re.IGNORECASE)
    number = match.group(1).zfill(2) if match else "unknown"
    return f"chapter-{number}.md"


def chunk_by_chapter():
    CHUNKS_DIR.mkdir(parents=True, exist_ok=True)

    current_chapter_title = None
    current_lines = []

    with open(PARSED_FILE, "r", encoding="utf-8") as f:
        for line in f:
            normalized = normalize_heading(line)

            # IMPORTANT: detect chapters from NORMALIZED line
            if normalized.startswith("## CHAPTER"):
                if current_chapter_title and current_lines:
                    out = CHUNKS_DIR / chapter_filename(current_chapter_title)
                    out.write_text("\n".join(current_lines).strip() + "\n", encoding="utf-8")

                current_chapter_title = normalized.replace("## ", "")
                current_lines = [normalized]
            else:
                if current_chapter_title:
                    current_lines.append(normalized)

    if current_chapter_title and current_lines:
        out = CHUNKS_DIR / chapter_filename(current_chapter_title)
        out.write_text("\n".join(current_lines).strip() + "\n", encoding="utf-8")

    print("Chapter chunks regenerated successfully")


if __name__ == "__main__":
    chunk_by_chapter()
