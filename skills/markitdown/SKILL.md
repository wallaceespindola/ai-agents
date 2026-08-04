---
name: markitdown
description: Convert documents and media to Markdown using Microsoft's MarkItDown CLI — PDF, DOCX, PPTX, XLSX, HTML, CSV, JSON, XML, EPub, ZIP archives, images (OCR) and YouTube URLs. Use when turning source documents into Markdown for articles, docs, LLM context or archiving, or when asked to "markitdown" a file.
---

# MarkItDown — Document to Markdown Conversion

Wraps Microsoft's [MarkItDown](https://github.com/microsoft/markitdown) CLI (installed via
`uv tool install "markitdown[all]"`). Converts almost any document format to clean,
LLM-friendly Markdown.

## When to Use This Skill

- Converting a PDF, Word, PowerPoint or Excel file into Markdown for an article draft or docs
- Pulling readable text out of HTML pages, EPubs or ZIP archives of mixed files
- Extracting text from images via OCR
- Fetching a YouTube video's transcript as Markdown
- Preparing document content as LLM context (Markdown is the cheapest faithful format)

Not for: Markdown → other formats (use pandoc), or high-fidelity layout preservation
(MarkItDown optimizes for text content, not visual fidelity).

## Quick Reference

```bash
markitdown file.pdf                        # convert, result to stdout
markitdown file.docx -o file.md            # convert to file
markitdown https://youtu.be/VIDEO_ID       # YouTube transcript
markitdown report.zip                      # every file in the archive, concatenated
markitdown scan.png                        # OCR on images
cat file.pdf | markitdown                  # stdin works too
```

Supported inputs: PDF, DOCX, PPTX, XLSX/XLS, HTML, CSV, JSON, XML, EPub, ZIP,
images (JPG/PNG — EXIF + OCR), audio (WAV/MP3 — EXIF + transcription), YouTube URLs.

## Batch Conversion

```bash
# ponytail: sequential loop is fine — conversion is I/O-bound, parallelize only if a real batch hurts
for f in docs/*.pdf; do markitdown "$f" -o "${f%.pdf}.md"; done
```

## Gotchas

- Audio transcription needs `ffmpeg` on PATH (`brew install ffmpeg`); without it audio files fail, everything else works
- Scanned PDFs with no text layer produce little or nothing — OCR applies to image files, not image-only PDFs; rasterize pages to PNG first if needed
- XLSX conversion emits one Markdown table per sheet; wide sheets produce wide tables — check rendering on the target platform
- Output is content-first: complex layouts (multi-column PDFs, floating tables) flatten in reading order

## Article Pipeline Fit

Use to ingest source material (specs, slide decks, reports) into Markdown before drafting
with the platform skills. Output feeds markdown-formatter for final cleanup.

## Related Skills

- markdown-formatter — normalize the converted output to house Markdown style
- code-examples-generator — rebuild code blocks that OCR/conversion mangled
- pdf / docx / pptx / xlsx (document-skills plugin) — create or edit Office documents; markitdown only reads
- doc-converter agent — batch conversions and mixed-format ingestion jobs
