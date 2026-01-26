import re
from typing import Dict, Tuple

class SensitiveDataScanner:
    def __init__(self):
        self.mapping = {}
        self.lookup = {}
        self.person_idx = 0
        self.company_idx = 0
        self.email_idx = 0
        self.phone_idx = 0
    
    def process(self, text: str) -> Tuple[str, Dict]:
        refined_text = text
        
        emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
        for email in set(emails):
            self.email_idx += 1
            id_token = f"[EMAIL_{self.email_idx}]"
            self.mapping[id_token] = email
            self.lookup[email] = id_token
            refined_text = refined_text.replace(email, id_token)
        
        phones = re.findall(r'\+?91[-\s]?\d{10}|\d{10}', text)
        for phone in set(phones):
            self.phone_idx += 1
            id_token = f"[PHONE_{self.phone_idx}]"
            self.mapping[id_token] = phone
            self.lookup[phone] = id_token
            refined_text = refined_text.replace(phone, id_token)
        
        org_entities = re.findall(r'\b[A-Z][A-Za-z\s&]+(?:Private Limited|Pvt\.?\s*Ltd\.?|Limited|Inc\.?|Corporation|Corp\.?)\b', text)
        for org in set(org_entities):
            self.company_idx += 1
            id_token = f"[COMPANY_{chr(65 + self.company_idx - 1)}]"
            self.mapping[id_token] = org
            self.lookup[org] = id_token
            refined_text = refined_text.replace(org, id_token)
        
        signature_fields = [
            r'(?:Name|By|Freelancer|Client):\s*([A-Z][a-z]+(?:\s+[A-Z][a-z]+){0,2})',
            r'\*\*(?:Client|Freelancer):\*\*\s*([A-Z][a-z]+(?:\s+[A-Z][a-z]+){0,2})'
        ]
        
        for rule in signature_fields:
            found_persons = re.findall(rule, text)
            for person in set(found_persons):
                if person not in self.lookup:
                    self.person_idx += 1
                    id_token = f"[PERSON_{self.person_idx}]"
                    self.mapping[id_token] = person
                    self.lookup[person] = id_token
                    refined_text = refined_text.replace(person, id_token)
        
        return refined_text, self.mapping
    
    def restore(self, text: str) -> str:
        output = text
        for token, original in self.mapping.items():
            output = output.replace(token, original)
        return output

def tokenize_document(text: str) -> Tuple[str, Dict]:
    scanner = SensitiveDataScanner()
    return scanner.process(text)
