import os
import json
import hashlib
from pathlib import Path

# Cache directory: local ./cache for development
CACHE_DIR = Path("cache")

def _get_cache_dir() -> Path:
    if not CACHE_DIR.exists():
        CACHE_DIR.mkdir(parents=True, exist_ok=True)
    return CACHE_DIR

def _get_cache_filepath(command: str, section_name: str, original_text: str) -> Path:
    """Generate a unique filename based on the command, section, and text hash."""
    # Hash the original content to ensure we invalidate cache if the English man page changes
    text_hash = hashlib.md5(original_text.encode("utf-8")).hexdigest()
    # Sanitize section name just in case
    safe_section = section_name.replace("/", "_").replace(" ", "_")
    filename = f"{command}_{safe_section}_{text_hash}.json"
    return _get_cache_dir() / filename

def get_cached_translation(command: str, section_name: str, original_text: str) -> str | None:
    """Returns the cached translation if it exists, otherwise None."""
    filepath = _get_cache_filepath(command, section_name, original_text)
    if filepath.exists():
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
                return data.get("translated_text")
        except Exception as e:
            print(f"Failed to read cache: {e}")
            return None
    return None

def set_cached_translation(command: str, section_name: str, original_text: str, translated_text: str) -> None:
    """Saves the translated text to the cache."""
    filepath = _get_cache_filepath(command, section_name, original_text)
    try:
        data = {
            "command": command,
            "section": section_name,
            "translated_text": translated_text
        }
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"Failed to write cache: {e}")
