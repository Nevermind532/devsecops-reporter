import json
import sys
from pathlib import Path

# Это строка полностью убирает ошибку "Не удаётся разрешить импорт '.base'" в VS Code/PyCharm
# и гарантирует, что импорт будет работать при запуске из любой папки
sys.path.insert(0, str(Path(__file__).parent.parent))

# Теперь импорт абсолютный — редактор доволен, и код работает
from reporter.parsers.base import BaseParser


class BanditParser(BaseParser):
    name = "Bandit (SAST)"

    def parse(self) -> list:
        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                data = json.load(f)

            issues = []
            for result in data.get("results", []):
                issues.append(
                    {
                        "tool": self.name,
                        "severity": result.get("issue_severity", "LOW").upper(),
                        "title": result.get("issue_text", "No title").strip(),
                        "description": result.get("more_info", "") or result.get("issue_text", ""),
                        "file": result.get("filename", ""),
                        "line": result.get("line_number", 0),
                        "code": result.get("code", ""),
                    }
                )
            return issues

        except Exception as e:
            # На случай битого файла — всё равно вернём понятную ошибку
            return [
                {
                    "tool": self.name,
                    "severity": "INFO",
                    "title": "Ошибка парсинга отчёта Bandit",
                    "description": str(e),
                    "file": "",
                    "line": 0,
                    "code": "",
                }
            ]