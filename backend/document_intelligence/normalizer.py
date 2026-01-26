import re

def normalize_text(raw_input: str) -> str:
    if not raw_input:
        return ""
    
    clean_output = raw_input.strip()
    clean_output = re.sub(r'\s+', ' ', clean_output)
    clean_output = re.sub(r'[^\x00-\x7F]+', '', clean_output)
    
    return clean_output
