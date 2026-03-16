import typer
import os
from typing import Optional
from dotenv import load_dotenv

from manzh.man_fetch import fetch_man
from manzh.parser import split_sections
from manzh.translator import translate_section
from manzh.formatter import format_terminal, format_markdown

load_dotenv()

app = typer.Typer(help="manzh - Unix manual localization layer (Taiwan Traditional Chinese)")

@app.command()
def main(
    command: str = typer.Argument(..., help="The manual page to translate (e.g., grep, tar)"),
    bilingual: bool = typer.Option(False, "--bilingual", "-b", help="Display original and translated text side-by-side"),
    markdown: bool = typer.Option(False, "--markdown", "-m", help="Output as Markdown text"),
    raw: bool = typer.Option(False, "--raw", help="Output raw, untranslated man page text for debugging"),
    section: Optional[str] = typer.Option(None, "--section", "-s", help="Translate only a specific section (e.g., DESCRIPTION)")
):
    """
    Translates and displays a requested man page in Taiwan Traditional Chinese.
    """
    # 1. Fetch
    raw_text = fetch_man(command)
    if not raw_text:
        typer.echo(f"Error: No manual entry for {command}", err=True)
        raise typer.Exit(code=1)
        
    if raw:
        typer.echo(raw_text)
        raise typer.Exit()
        
    # 2. Parse
    sections = split_sections(raw_text)
    if not sections:
        typer.echo("Error: Could not parse sections from the manual page.", err=True)
        raise typer.Exit(code=1)
        
    # 3. Translate
    # Note: In a real app we'd parallelize this or use streaming.
    # For MVP, we iterate synchronously.
    translated_sections = {}
    
    if section:
        target_section = section.upper()
        if target_section not in sections:
            typer.echo(f"Error: Section '{target_section}' not found in manual.", err=True)
            raise typer.Exit(code=1)
            
        translated_sections[target_section] = translate_section(command, sections[target_section], target_section)
        # Filter sections to only the requested one for output
        sections = {target_section: sections[target_section]}
    else:
        typer.echo("Translating... (This might take a few moments depending on the API speed)")
        for sec_name, sec_text in sections.items():
            translated_sections[sec_name] = translate_section(command, sec_text, sec_name)
            
    # 4. Format & Output
    if markdown:
        md_output = format_markdown(sections, translated_sections, command)
        typer.echo(md_output)
    else:
        format_terminal(sections, translated_sections, bilingual)


if __name__ == "__main__":
    app()
