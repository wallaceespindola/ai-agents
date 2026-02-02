"""
Slides Creator Utilities

Core modules for converting articles to presentations.
"""

from article_parser import ArticleParser, ArticleStructure, CodeBlock, ImageReference
from pptx_generator import PowerPointGenerator, PptxConfig, ColorScheme

__all__ = [
    'ArticleParser',
    'ArticleStructure',
    'CodeBlock',
    'ImageReference',
    'PowerPointGenerator',
    'PptxConfig',
    'ColorScheme',
]
