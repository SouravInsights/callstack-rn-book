from pathlib import Path
from llama_parse import LlamaParse


# Configuration

PDF_DIR = Path("pdf")
PARSED_DIR = Path("parsed")

PDF_FILE = PDF_DIR / "rn-performance-optimization.pdf"
OUTPUT_FILE = PARSED_DIR / "rn-performance-optimization.full.md"

# Remove headers / footers
BBOX_TOP = 0.08     # top 8% of page
BBOX_BOTTOM = 0.06  # bottom 6% of page


# Parse PDF to Markdown

def parse_pdf_to_markdown():
    if not PDF_FILE.exists():
        raise FileNotFoundError(f"PDF not found: {PDF_FILE}")

    PARSED_DIR.mkdir(parents=True, exist_ok=True)

    parser = LlamaParse(
        result_type="markdown",
        bbox_top=BBOX_TOP,
        bbox_bottom=BBOX_BOTTOM,
        verbose=True,
    )

    with open(PDF_FILE, "rb") as f:
        documents = parser.load_data(
            f,
            extra_info={"file_name": PDF_FILE.name}
        )

    if not documents:
        raise RuntimeError("LlamaParse returned no documents")

    with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
        for doc in documents:
            out.write(doc.text.strip())
            out.write("\n\n")

    print(f"✅ Parsed markdown written to: {OUTPUT_FILE}")


# Entry point

if __name__ == "__main__":
    parse_pdf_to_markdown()
