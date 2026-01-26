from typing import List

def run_analysis(clause_data: dict) -> List[dict]:
    content = clause_data["text"].lower()
    discovered_flags = []

    if "non compete" in content or "shall not engage" in content:
        discovered_flags.append({
            "clause_id": clause_data["clause_id"],
            "title": clause_data["title"],
            "risk_level": "High",
            "law": "The Indian Contract Act, 1872",
            "section": "Section 27",
            "reason": "Restraint of trade clauses are generally void in India"
        })

    if "terminate at any time" in content and "without notice" in content:
        discovered_flags.append({
            "clause_id": clause_data["clause_id"],
            "title": clause_data["title"],
            "risk_level": "Medium",
            "law": "The Indian Contract Act, 1872",
            "section": "Section 23",
            "reason": "Unfair or unconscionable contract terms may be unlawful"
        })

    if "indemnify" in content and "all losses" in content:
        discovered_flags.append({
            "clause_id": clause_data["clause_id"],
            "title": clause_data["title"],
            "risk_level": "Medium",
            "law": "The Indian Contract Act, 1872",
            "section": "Section 124–125",
            "reason": "Broad indemnity obligations may expose disproportionate liability"
        })

    if "intellectual property" in content and "all rights" in content:
        discovered_flags.append({
            "clause_id": clause_data["clause_id"],
            "title": clause_data["title"],
            "risk_level": "High",
            "law": "Copyright Act, 1957",
            "section": "Section 19",
            "reason": "Assignment of all present and future IP may be excessive"
        })

    return discovered_flags
