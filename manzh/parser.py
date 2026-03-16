import re
from typing import Dict, List, Tuple

def split_sections(text: str) -> Dict[str, str]:
    """Splits a man page text into its main sections (NAME, SYNOPSIS, etc.)."""
    sections = {}
    current_section = None
    current_content = []

    for line in text.splitlines():
        # A section header is typically uppercase, starts at the beginning of the line, 
        # and has no leading spaces. Some man pages have formatting so we strip trailing whitespace.
        if line and not line[0].isspace() and line.isupper() and len(line.strip()) < 40:
            if current_section:
                sections[current_section] = "\n".join(current_content)
            current_section = line.strip()
            current_content = []
        elif current_section:
            current_content.append(line)

    # Add the last section
    if current_section and current_content:
        sections[current_section] = "\n".join(current_content)

    return sections

def detect_untranslatable_blocks(text: str) -> Tuple[List[str], str]:
    """
    Identifies and extracts blocks that shouldn't be translated (e.g., code blocks).
    Returns a tuple of (extracted_blocks, text_with_placeholders).
    This process is complex and will be refined; for MVP, we'll try a basic approach
    or rely mostly on LLM prompt instructions to not touch code lines.
    
    For now, this is a placeholder function returning the original text.
    We will rely heavily on the LLM Prompt to parse this.
    """
    return [], text
