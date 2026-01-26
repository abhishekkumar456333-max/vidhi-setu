from legal_engine.india.contract_act import run_analysis

class CountryAdapter:
    def __init__(self, target_country: str):
        self.target_country = target_country.lower()

    def perform_checks(self, clauses):
        if self.target_country == "india":
            return self._handle_india_logic(clauses)
        return []

    def _handle_india_logic(self, clauses):
        results = []
        for item in clauses:
            results.extend(run_analysis(item))
        return results
