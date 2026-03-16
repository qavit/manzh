# manzh (Man Page Translator)

`manzh` is a specialized tool designed to translate Linux `man` pages into Traditional Chinese (zh-TW). By combining the powerful translation capabilities of OpenAI with localized expertise, it provides developers with smooth and accurate command references.

## ✨ Features
- **Accurate Translation**: Context-aware professional translation using Large Language Models.
- **Local Caching**: Automatically caches translation results locally to save API costs and speed up subsequent access.
- **Optimized Formatting**: Preserves the original layout and hierarchy of the `man` manual.

## 🚀 Installation & Setup

### 1. Get the Source Code
```bash
git clone https://github.com/qavit/manzh.git
cd manzh
```

### 2. Install Dependencies
This project recommends using `uv` or `pip` for installation:
```bash
# Using uv
uv pip install -e .

# Or using pip
pip install -e .
```

### 3. Configure API Key
`manzh` requires an OpenAI API key to function. Copy `.env.example` to `.env` and fill in your key:
```bash
cp .env.example .env
```
Edit `.env`:
```text
OPENAI_API_KEY=sk-your-real-api-key
```

## 📖 Usage
Simply input the command you wish to translate:
```bash
# Translate the 'ls' command
python main.py ls

# Translate the 'git' command
python main.py git
```

## ⚠️ Security & Privacy
- **API Key Security**: Always ensure your `.env` file is **NOT** uploaded to Git. This project includes `.env` in `.gitignore` by default.
- **License**: This project is licensed under **AGPL-3.0**. If you modify this project and provide it as a network service (SaaS) to others, you must disclose your source code under the AGPL terms.
- **Cache Data**: Translation results are stored in the local `cache/` directory. You can clear this folder at any time to reset translations.

---
Made with ❤️ for the Linux community.
