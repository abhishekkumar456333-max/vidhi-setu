import re
from typing import List, Dict

DETECTION_REGEX = re.compile(
    r"(?:\n|^)(\d+(?:\.\d+)*\s+[A-Z][^\n]+)"
)

def divide_into_clauses(full_text: str) -> List[Dict]:
    segmented_data = []
    fragments = DETECTION_REGEX.split(full_text)

    for i in range(1, len(fragments), 2):
        header = fragments[i].strip()
        body_content = fragments[i + 1].strip() if i + 1 < len(fragments) else ""

        segmented_data.append({
            "clause_id": header.split()[0],
            "title": header,
            "text": body_content
        })

    if not segmented_data:
        segmented_data.append({
            "clause_id": "1",
            "title": "Document Content",
            "text": full_text
        })

    return segmented_data
