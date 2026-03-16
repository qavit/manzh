from typing import Dict
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel

console = Console()

def format_terminal(sections: Dict[str, str], translated_sections: Dict[str, str], bilingual: bool = False) -> None:
    """Formats and prints the translated man page to the terminal using rich."""
    for section_name, original_text in sections.items():
        translated_text = translated_sections.get(section_name, original_text)
        
        # Print Section Header
        console.print(f"\n[bold green]{section_name}[/bold green]")
        
        if bilingual and section_name in translated_sections and translated_text != original_text:
            # Print both original and translated text
            console.print(original_text, style="dim")
            console.print(translated_text)
        else:
            console.print(translated_text)
            
    console.print("\n")

def format_markdown(sections: Dict[str, str], translated_sections: Dict[str, str], command: str) -> str:
    """Formats the translated man page as a Markdown string."""
    md_lines = [f"# {command}\n"]
    
    for section_name, original_text in sections.items():
        translated_text = translated_sections.get(section_name, original_text)
        
        md_lines.append(f"## {section_name}")
        md_lines.append(translated_text)
        md_lines.append("")
        
    return "\n".join(md_lines)
