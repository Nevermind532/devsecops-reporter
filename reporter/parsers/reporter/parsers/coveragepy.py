import json
from .base import BaseParser

class CoverageParser(BaseParser):
    name = "Coverage.py"
    
    def parse(self):
        try:
            with open(self.filepath, 'r') as f:
                data = json.load(f)
            coverage = data.get("totals", {}).get("percent_covered", 0)
            return [{
                "tool": self.name,
                "coverage_percent": round(float(coverage), 2),
                "status": "OK" if coverage >= 80 else "LOW"
            }]
        except:
            return [{"tool": self.name, "error": "Failed to parse"}]