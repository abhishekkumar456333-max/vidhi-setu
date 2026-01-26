REASONABLE_THRESHOLDS = {
    "non_compete": {
        "max_duration_months": 6,
        "geographic_scope": "specific_region",
        "fair_description": "Limited to 6 months in a specific region"
    },
    "termination": {
        "min_notice_days": 30,
        "fair_description": "At least 30 days written notice"
    },
    "ip_assignment": {
        "allows_preexisting_retention": True,
        "fair_description": "Freelancer retains pre-existing IP, assigns only new work"
    },
    "indemnity": {
        "mutual": True,
        "fair_description": "Mutual indemnification, not one-sided"
    },
    "payment_terms": {
        "max_delay_days": 15,
        "requires_milestones": True,
        "fair_description": "Clear milestones with payment within 15 days"
    },
    "liability_cap": {
        "exists": True,
        "fair_description": "Liability capped at project value or reasonable amount"
    }
}

def get_fair_baseline():
    return REASONABLE_THRESHOLDS
