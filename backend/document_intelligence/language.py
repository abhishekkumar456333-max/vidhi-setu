from langdetect import detect

def identify_language(input_text: str) -> str:
    try:
        return detect(input_text)
    except Exception:
        return "unknown"
