from abc import ABC, abstractmethod
from typing import List, Dict, Any


class BaseParser(ABC):
    """
    Базовый класс для всех парсеров отчётов.
    Наследуйся от него, когда добавляешь новый инструмент (Bandit, ZAP, Semgrep, Coverage и т.д.).
    """
    name: str = "Unknown Tool"  # Будет отображаться в HTML-отчёте

    def __init__(self, filepath: str):
        self.filepath = filepath

    @abstractmethod
    def parse(self) -> List[Dict[str, Any]]:
        """
        Основной метод — парсит файл и возвращает список проблем/метрик.
        Каждая проблема должна быть словарем с полями (можно добавлять свои):
            - tool: str
            - severity: str (CRITICAL, HIGH, MEDIUM, LOW, INFO)
            - title: str
            - description: str (опционально)
            - file: str
            - line: int
            - code: str (опционально)
        """
        pass

    def get_summary(self, issues: List[Dict[str, Any]]) -> Dict[str, int]:
        """
        Подсчитывает количество проблем по уровням критичности.
        Используется для красивой статистики в отчёте.
        """
        counts = {"CRITICAL": 0, "HIGH": 0, "MEDIUM": 0, "LOW": 0, "INFO": 0}
        for issue in issues:
            # Поддерживаем разные варианты написания severity
            sev = str(issue.get("severity", "INFO")).upper()
            if sev in counts:
                counts[sev] += 1
            elif sev == "CRITICAL":
                counts["CRITICAL"] += 1
        return counts