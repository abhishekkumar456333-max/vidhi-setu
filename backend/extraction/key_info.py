import re
from typing import Dict

def extract_key_details(document_text: str) -> Dict:
    details = {}

    price_pattern = re.search(r"(₹|\$|INR)\s?\d+[,\d]*", document_text)
    span_pattern = re.search(r"(\d+\s+(months?|years?))", document_text, re.IGNORECASE)
    notice_pattern = re.search(r"(\d+\s+days?\s+notice)", document_text, re.IGNORECASE)
    jurisdiction_pattern = re.search(r"governed by the laws of ([A-Za-z ]+)", document_text, re.IGNORECASE)

    details["fees"] = price_pattern.group() if price_pattern else "Not detected"
    details["duration"] = span_pattern.group() if span_pattern else "Not detected"
    details["termination_notice"] = notice_pattern.group() if notice_pattern else "Not detected"
    details["governing_law"] = jurisdiction_pattern.group(1) if jurisdiction_pattern else "Not specified"

    if "intellectual property" in document_text.lower():
        if "client" in document_text.lower():
            details["ip_ownership"] = "Client"
        elif "contractor" in document_text.lower():
            details["ip_ownership"] = "Freelancer"
        else:
            details["ip_ownership"] = "Mentioned (context unclear)"
    else:
        details["ip_ownership"] = "Not found"

    return details
