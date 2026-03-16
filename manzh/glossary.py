from typing import Dict

# 台灣正體中文術語表
GLOSSARY: Dict[str, str] = {
    "file": "檔案",
    "directory": "目錄",
    "path": "路徑",
    "pathname": "路徑名稱",
    "standard input": "標準輸入",
    "standard output": "標準輸出",
    "standard error": "標準錯誤",
    "current working directory": "目前工作目錄",
    "option": "選項",
    "flag": "旗標",
    "argument": "引數",
    "parameter": "參數",
    "pattern": "模式",
    "regular expression": "正則表達式",
    "regex": "正則表達式",
    "recursively": "遞迴地",
    "recursive": "遞迴的",
    "command": "指令",
    "shell": "shell",
    "terminal": "終端機",
    "operand": "運算元",
    "stdin": "標準輸入",
    "stdout": "標準輸出",
    "stderr": "標準錯誤",
    "default": "預設",
    "print": "印出",
    "character": "字元",
    "string": "字串",
    "message": "訊息",
    "memory": "記憶體",
    "hardware": "硬體",
    "software": "軟體",
    "network": "網路",
    "support": "支援",
    "interactive": "互動",
}

def apply_glossary(text: str) -> str:
    """
    Applies the glossary terms to a translated text as a post-translation correction step.
    Note: A naive replace might break English code blocks or options, but we expect
    those to remain mostly untouched if the LLM follows prompts. If the LLM has already
    used terms like "文件", we might need more advanced rules. For now, this is a basic sweep.
    """
    # Replacing common simplified Chinese or alternative terms that the LLM might output
    corrections = {
        "文件": "檔案",
        "文件夾": "目錄",
        "命令行": "命令列",
        "程序": "程式",
        "參數": "引數",
        "選項": "選項",
        "標准輸入": "標準輸入",
        "標准輸出": "標準輸出",
        "默認": "預設",
        "打印": "印出",
        "字符": "字元",
        "字符串": "字串",
        "二進制": "二進位",
        "信息": "訊息",
        "網絡": "網路",
        "支持": "支援",
        "進程": "行程",
        "內存": "記憶體",
        "硬件": "硬體",
        "軟件": "軟體",
        "緩存": "快取",
        "變量": "變數",
        "交互": "互動",
        "退出": "結束",
        "激活": "啟用",
        "撤銷": "復原",
        "數據": "資料",
        "源碼": "原始碼",
        "代碼": "程式碼",
        "宏": "巨集",
        "指針": "指標",
        "視圖": "檢視",
        "操作系統": "作業系統",
        "聯網": "網路連線",
        "卸載": "解除安裝",
        "保存": "儲存",
        "運行": "執行",
        "存儲": "儲存",
    }
    
    corrected_text = text
    for wrong, right in corrections.items():
        corrected_text = corrected_text.replace(wrong, right)
        
    return corrected_text
