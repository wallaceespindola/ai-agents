"""
Article Parser - Extract structured content from markdown articles

Parses technical articles following the ARTICLE_TEMPLATE.md format and
extracts metadata, sections, code blocks, and images for slide generation.
"""

import re
from dataclasses import dataclass
from typing import List, Optional, Dict, Any
from pathlib import Path
import yaml


@dataclass
class CodeBlock:
    """Represents a code block from an article"""
    language: str
    code: str
    context_before: str = ""
    context_after: str = ""
    line_count: int = 0

    def __post_init__(self):
        self.line_count = len(self.code.strip().split('\n'))


@dataclass
class ImageReference:
    """Represents an image/diagram reference from an article"""
    alt_text: str
    file_path: str
    caption: str = ""
    is_diagram: bool = False  # True for Mermaid/PlantUML diagrams


@dataclass
class Section:
    """Represents an article section (heading + content)"""
    heading: str
    level: int  # 1 for H1, 2 for H2, 3 for H3
    content: str
    subsections: List['Section'] = None
    code_blocks: List[CodeBlock] = None
    images: List[ImageReference] = None

    def __post_init__(self):
        if self.subsections is None:
            self.subsections = []
        if self.code_blocks is None:
            self.code_blocks = []
        if self.images is None:
            self.images = []


@dataclass
class ArticleStructure:
    """Complete article structure with all extracted content"""
    title: str
    author: str
    date: str
    tags: List[str]
    sections: List[Section]
    code_blocks: List[CodeBlock]
    images: List[ImageReference]
    raw_content: str

    def get_estimated_slide_count(self) -> int:
        """Estimate number of slides needed"""
        # 1 title slide
        slides = 1

        # ~2-3 slides per H2 section (depends on content density)
        h2_sections = [s for s in self.sections if s.level == 2]
        slides += len(h2_sections) * 2

        # 1 slide per code block
        slides += len(self.code_blocks)

        # 1 slide per image/diagram
        slides += len(self.images)

        # 1 conclusion slide
        slides += 1

        return slides


class ArticleParser:
    """Parse markdown articles into structured format"""

    def __init__(self):
        self.frontmatter_pattern = re.compile(r'^---\n(.*?)\n---', re.DOTALL)
        self.heading_pattern = re.compile(r'^(#{1,6})\s+(.+)$', re.MULTILINE)
        self.code_block_pattern = re.compile(
            r'```(\w*)\n(.*?)```',
            re.DOTALL
        )
        self.image_pattern = re.compile(r'!\[([^\]]*)\]\(([^\)]+)\)')
        self.list_pattern = re.compile(r'^[\*\-\+]\s+(.+)$', re.MULTILINE)

    def parse_file(self, file_path: str) -> ArticleStructure:
        """Parse a markdown article file"""
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"Article not found: {file_path}")

        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()

        return self.parse_content(content)

    def parse_content(self, content: str) -> ArticleStructure:
        """Parse markdown content and extract article structure"""

        # Extract frontmatter
        metadata = self._extract_frontmatter(content)

        # Remove frontmatter from content for further processing
        content_without_fm = self.frontmatter_pattern.sub('', content)

        # Extract code blocks
        code_blocks = self._extract_code_blocks(content_without_fm)

        # Extract images
        images = self._extract_images(content_without_fm)

        # Extract sections
        sections = self._extract_sections(content_without_fm)

        return ArticleStructure(
            title=metadata.get('title', 'Untitled'),
            author=metadata.get('author', 'Unknown'),
            date=metadata.get('date', ''),
            tags=metadata.get('tags', []),
            sections=sections,
            code_blocks=code_blocks,
            images=images,
            raw_content=content
        )

    def _extract_frontmatter(self, content: str) -> Dict[str, Any]:
        """Extract YAML frontmatter from article"""
        match = self.frontmatter_pattern.search(content)
        if not match:
            return {}

        try:
            fm = yaml.safe_load(match.group(1))
            return fm if fm else {}
        except yaml.YAMLError:
            return {}

    def _extract_code_blocks(self, content: str) -> List[CodeBlock]:
        """Extract all code blocks from content"""
        blocks = []

        for match in self.code_block_pattern.finditer(content):
            language = match.group(1) or 'text'
            code = match.group(2).strip()

            # Find context (text before and after code block)
            start = match.start()
            end = match.end()

            # Get context before (last 2 sentences)
            before_text = content[:start]
            context_before = self._get_context(before_text, 2)

            # Get context after (first 2 sentences)
            after_text = content[end:]
            context_after = self._get_context(after_text, 2)

            blocks.append(CodeBlock(
                language=language,
                code=code,
                context_before=context_before,
                context_after=context_after
            ))

        return blocks

    def _extract_images(self, content: str) -> List[ImageReference]:
        """Extract image references from content"""
        images = []

        for match in self.image_pattern.finditer(content):
            alt_text = match.group(1)
            file_path = match.group(2)

            # Determine if it's a diagram (Mermaid/PlantUML syntax in file path)
            is_diagram = 'mermaid' in file_path.lower() or 'plantuml' in file_path.lower()

            images.append(ImageReference(
                alt_text=alt_text,
                file_path=file_path,
                is_diagram=is_diagram
            ))

        return images

    def _extract_sections(self, content: str) -> List[Section]:
        """Extract document sections by heading hierarchy"""
        sections = []
        current_section = None

        lines = content.split('\n')

        for line in lines:
            match = self.heading_pattern.match(line)
            if match:
                level = len(match.group(1))
                heading = match.group(2)

                if level == 2:  # H2 - main section
                    if current_section:
                        sections.append(current_section)
                    current_section = Section(
                        heading=heading,
                        level=level,
                        content=""
                    )
                elif level == 3 and current_section:  # H3 - subsection
                    subsection = Section(
                        heading=heading,
                        level=level,
                        content=""
                    )
                    current_section.subsections.append(subsection)
            elif current_section:
                current_section.content += line + '\n'

        if current_section:
            sections.append(current_section)

        return sections

    def _get_context(self, text: str, num_sentences: int = 2) -> str:
        """Extract last N sentences from text"""
        sentences = re.split(r'[.!?]+', text.strip())
        sentences = [s.strip() for s in sentences if s.strip()]

        if not sentences:
            return ""

        context = '. '.join(sentences[-num_sentences:])
        return context.strip()[:200]  # Limit to 200 chars

    def calculate_slide_count(self, article: ArticleStructure) -> int:
        """Calculate estimated number of slides for article"""
        return article.get_estimated_slide_count()

    def create_slide_plan(self, article: ArticleStructure) -> List[Dict[str, Any]]:
        """Create detailed slide-by-slide plan from article"""
        slides = []

        # Slide 1: Title slide
        slides.append({
            'type': 'title',
            'content': {
                'title': article.title,
                'author': article.author,
                'date': article.date,
                'tags': article.tags
            },
            'speaker_notes': f"Presenting: {article.title}\nAuthor: {article.author}"
        })

        # Content slides from sections
        for section in article.sections:
            if section.level != 2:
                continue

            # Section title slide
            slides.append({
                'type': 'content',
                'content': {
                    'heading': section.heading,
                    'body': self._condense_text(section.content, 100),
                    'bullet_points': self._extract_bullet_points(section.content)
                },
                'speaker_notes': section.content[:500]
            })

            # Add code blocks for this section
            for code_block in section.code_blocks:
                slides.append({
                    'type': 'code',
                    'content': {
                        'language': code_block.language,
                        'code': code_block.code,
                        'context': code_block.context_before
                    },
                    'speaker_notes': f"{code_block.context_before}\n\n{code_block.context_after}"
                })

            # Add images for this section
            for image in section.images:
                slides.append({
                    'type': 'visual',
                    'content': {
                        'alt_text': image.alt_text,
                        'file_path': image.file_path,
                        'caption': image.caption
                    },
                    'speaker_notes': image.caption
                })

        # Conclusion slide
        conclusion = self._extract_conclusion(article)
        slides.append({
            'type': 'conclusion',
            'content': {
                'heading': 'Key Takeaways',
                'takeaways': conclusion['takeaways'],
                'cta': conclusion['cta']
            },
            'speaker_notes': conclusion['notes']
        })

        return slides

    def _condense_text(self, text: str, max_words: int = 100) -> str:
        """Reduce text to essential points"""
        sentences = re.split(r'[.!?]+', text.strip())
        sentences = [s.strip() for s in sentences if s.strip()]

        condensed = ""
        word_count = 0

        for sentence in sentences:
            words = len(sentence.split())
            if word_count + words <= max_words:
                condensed += sentence + ". "
                word_count += words
            else:
                break

        if word_count > max_words:
            condensed += "..."

        return condensed.strip()

    def _extract_bullet_points(self, text: str, max_bullets: int = 5) -> List[str]:
        """Extract bullet points from text"""
        bullets = []

        for match in self.list_pattern.finditer(text):
            if len(bullets) < max_bullets:
                bullets.append(match.group(1).strip())

        return bullets

    def _extract_conclusion(self, article: ArticleStructure) -> Dict[str, Any]:
        """Extract conclusion section and generate takeaways"""

        # Look for conclusion section
        conclusion_content = ""
        for section in article.sections:
            if 'conclusion' in section.heading.lower():
                conclusion_content = section.content
                break

        # Extract takeaways
        takeaways = self._extract_bullet_points(conclusion_content, 5)
        if not takeaways:
            # Generate from first section
            takeaways = self._extract_bullet_points(
                article.sections[0].content if article.sections else "", 5
            )

        return {
            'takeaways': takeaways,
            'cta': 'Check out the full article and code examples',
            'notes': conclusion_content[:500]
        }


# Example usage
if __name__ == "__main__":
    parser = ArticleParser()

    # Example: Parse a file
    # article = parser.parse_file("docs/articles/example.md")
    # print(f"Title: {article.title}")
    # print(f"Estimated slides: {parser.calculate_slide_count(article)}")
    # slide_plan = parser.create_slide_plan(article)
    # for i, slide in enumerate(slide_plan):
    #     print(f"\nSlide {i+1}: {slide['type']}")
