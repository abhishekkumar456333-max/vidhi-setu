import logging
import re
from typing import Any

class SensitiveContentFilter(logging.Filter):
    
    PATTERNS_TO_REDACT = [
        'file_bytes',
        'clean_text',
        'raw_text',
        'tokenized_text',
        'clauses',
        'text',
        'content'
    ]
    
    def filter(self, record: logging.LogRecord) -> bool:
        if hasattr(record, 'msg'):
            message = str(record.msg)
            
            if len(message) > 500:
                record.msg = f"[Automatic Redaction: Text of {len(message)} characters removed for privacy]"
            
            for key in self.PATTERNS_TO_REDACT:
                if key in message.lower():
                    record.msg = re.sub(
                        rf'{key}["\']?\s*[:=]\s*["\']?[^,"}}]+',
                        f'{key}=[REDACTED]',
                        message,
                        flags=re.IGNORECASE
                    )
        
        return True

def configure_logging():
    root_logger = logging.getLogger()
    
    redaction_logic = SensitiveContentFilter()
    for handler in root_logger.handlers:
        handler.addFilter(redaction_logic)
    
    uvicorn_access = logging.getLogger("uvicorn.access")
    uvicorn_access.addFilter(redaction_logic)
    
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    return root_logger
