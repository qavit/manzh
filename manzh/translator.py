import os
from openai import OpenAI
from manzh.glossary import GLOSSARY, apply_glossary
from manzh.cache import get_cached_translation, set_cached_translation

def get_translate_prompt() -> str:
    glossary_str = "\n".join([f"   - {k} = {v}" for k, v in GLOSSARY.items()])
    return f"""你正在翻譯 Unix man page 的特定章節成台灣正體中文。

要求：
1. **不要**翻譯命令名稱。
2. **不要**翻譯 flag（例如 `-r`, `--help`）。
3. **不要**翻譯 code block、路徑名稱（path）、環境變數。
4. 保留原本段落結構與空行。
5. 僅翻譯這段說明文字，請保持語氣精確，不要過度意譯。
6. 使用台灣正體中文術語：
{glossary_str}

請直接回傳翻譯後的內容，不要加上其他解釋或語氣詞。"""

def translate_section(command: str, text: str, section_name: str, model: str = "gpt-4o") -> str:
    """Translates a specific section of a man page using OpenAI API, with caching."""
    # Some sections we might want to skip translation completely
    skip_sections = ["SYNOPSIS", "SEE ALSO", "ENVIRONMENT", "FILES"]
    if section_name.strip() in skip_sections:
        return text

    # Check cache first
    cached_text = get_cached_translation(command, section_name, text)
    if cached_text:
        return cached_text

    client = OpenAI() # Assumes OPENAI_API_KEY is in environment
    
    prompt = get_translate_prompt()
    
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": text}
            ],
            temperature=0.1 # Keep it deterministic and factual
        )
        translated_text = response.choices[0].message.content
        if translated_text:
             final_text = apply_glossary(translated_text)
             # Save to cache
             set_cached_translation(command, section_name, text, final_text)
             return final_text
        return text
    except Exception as e:
        print(f"Failed to translate section {section_name}: {e}")
        return text
