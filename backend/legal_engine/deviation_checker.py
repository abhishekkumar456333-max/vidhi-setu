import re
from typing import List, Dict
from legal_engine.fair_baseline import get_fair_baseline

def parse_months(content: str) -> int:
    y_match = re.search(r'(\d+)\s*year', content, re.IGNORECASE)
    if y_match:
        return int(y_match.group(1)) * 12
    
    m_match = re.search(r'(\d+)\s*month', content, re.IGNORECASE)
    if m_match:
        return int(m_match.group(1))
    
    return 0

def parse_days(content: str) -> int:
    d_match = re.search(r'(\d+)\s*day', content, re.IGNORECASE)
    if d_match:
        return int(d_match.group(1))
    return 0

def check_deviations(elements: List[Dict], identified_risks: List[Dict]) -> List[Dict]:
    standard_baseline = get_fair_baseline()
    detected_gaps = []
    
    for issue in identified_risks:
        element_text = issue.get("text", "")
        legal_category = issue.get("law", "").lower()
        
        if "non-compete" in legal_category or "competition" in element_text.lower():
            span = parse_months(element_text)
            allowed_max = standard_baseline["non_compete"]["max_duration_months"]
            
            if span > allowed_max:
                detected_gaps.append({
                    "category": "Non-Compete Duration",
                    "severity": "High" if span > allowed_max * 2 else "Medium",
                    "actual": f"{span} months",
                    "fair_baseline": f"{allowed_max} months max",
                    "recommendation": f"Reduce restriction to {allowed_max} months",
                    "clause_reference": issue.get("clause_id")
                })
            
            if "india" in element_text.lower() and "all of" in element_text.lower():
                detected_gaps.append({
                    "category": "Non-Compete Geography",
                    "severity": "Medium",
                    "actual": "Unlimited (India-wide)",
                    "fair_baseline": "Restricted to specific region",
                    "recommendation": "Limit the ban to specific cities where the client operates",
                    "clause_reference": issue.get("clause_id")
                })
        
        if "termination" in legal_category or "terminate" in element_text.lower():
            period = parse_days(element_text)
            standard_min = standard_baseline["termination"]["min_notice_days"]
            
            if 0 < period < standard_min:
                detected_gaps.append({
                    "category": "Notice Period",
                    "severity": "Medium",
                    "actual": f"{period} days",
                    "fair_baseline": f"Minimum {standard_min} days",
                    "recommendation": f"Increase notice period to {standard_min} days",
                    "clause_reference": issue.get("clause_id")
                })
        
        if "intellectual property" in legal_category or "ip" in element_text.lower():
            has_preexisting_clause = any(term in element_text.lower() for term in ["pre-existing", "preexisting", "prior work", "existing"])
            
            if not has_preexisting_clause and "all" in element_text.lower():
                detected_gaps.append({
                    "category": "IP Ownership Scope",
                    "severity": "High",
                    "actual": "Blanket IP assignment",
                    "fair_baseline": standard_baseline["ip_assignment"]["fair_description"],
                    "recommendation": "Explicitly exclude your pre-existing tools and background IP",
                    "clause_reference": issue.get("clause_id")
                })
        
        if "indemnit" in element_text.lower():
            is_unilateral = "freelancer agrees to indemnify" in element_text.lower() and "client agrees" not in element_text.lower()
            
            if is_unilateral:
                detected_gaps.append({
                    "category": "Indemnity Balance",
                    "severity": "Medium",
                    "actual": "Unilateral (Freelancer only)",
                    "fair_baseline": standard_baseline["indemnity"]["fair_description"],
                    "recommendation": "Negotiate for a mutual indemnification clause",
                    "clause_reference": issue.get("clause_id")
                })
        
        if "payment" in element_text.lower() or "delay" in element_text.lower():
            grace_period = parse_days(element_text)
            max_allowed = standard_baseline["payment_terms"]["max_delay_days"]
            
            if grace_period > max_allowed:
                detected_gaps.append({
                    "category": "Payment Delay",
                    "severity": "Medium",
                    "actual": f"{grace_period} days",
                    "fair_baseline": f"{max_allowed} days max",
                    "recommendation": f"Crawl payment cycles back to {max_allowed} days",
                    "clause_reference": issue.get("clause_id")
                })
    
    return detected_gaps
