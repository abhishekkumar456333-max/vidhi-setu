from typing import List, Dict, Tuple

PROHIBITED_LEGAL_CONCEPTS = [
    "at-will employment",
    "at will employment",
    "employment at will",
    "right to work",
    "punitive damages",
    "discovery process",
    "deposition",
    "securities and exchange commission",
    "sec filing",
    "delaware law",
    "california law",
    "new york law",
    "federal law",
    "state law",
    "unfair dismissal",
    "tribunal",
    "redundancy payment",
    "paye",
    "hmrc",
    "tort",
    "common law jurisdiction",
    "case law precedent",
    "stare decisis",
]

RECOGNIZED_INDIAN_STATUTES = [
    "indian contract act",
    "copyright act",
    "information technology act",
    "shops and establishments act",
    "payment of wages act",
    "industrial disputes act",
    "arbitration and conciliation act",
    "consumer protection act",
]

def check_jurisdiction_compliance(flags: List[Dict]) -> Tuple[List[Dict], List[str]]:
    valid_flags = []
    compliance_notes = []
    
    for flag in flags:
        citation = flag.get("law", "").lower()
        justification = flag.get("reason", "").lower()
        combined_context = f"{citation} {justification}"
        
        matches = [term for term in PROHIBITED_LEGAL_CONCEPTS if term in combined_context]
        
        if matches:
            compliance_notes.append(
                f"Clause {flag.get('clause_id')} removed: References foreign concept ({', '.join(matches)})"
            )
            continue
        
        is_explicitly_indian = any(statute in citation for statute in RECOGNIZED_INDIAN_STATUTES)
        
        if not is_explicitly_indian and citation:
            compliance_notes.append(
                f"Clause {flag.get('clause_id')}: Law '{citation}' is outside standard Indian whitelist (proceeding with caution)"
            )
        
        valid_flags.append(flag)
    
    return valid_flags, compliance_notes

def filter_foreign_references(content: str) -> str:
    cleaned = content
    for concept in PROHIBITED_LEGAL_CONCEPTS:
        if concept in cleaned.lower():
            cleaned = cleaned.replace(concept, "[REDACTED_NON_INDIAN_LAW]")
            cleaned = cleaned.replace(concept.title(), "[REDACTED_NON_INDIAN_LAW]")
    return cleaned
