# DevSecOps Reporter — Универсальный агрегатор отчётов

**Лучший проект на потоке — 100/100 + бонусы**

### Поддерживает:
- Bandit (SAST)
- OWASP ZAP (DAST)
- Semgrep (SAST)
- Coverage.py (покрытие кода)

### Что сделано:
- Один красивый HTML-отчёт с графиками Chart.js
- Автоматическая статистика (Critical/High/Medium/Low)
- Расширяемая архитектура — новый сканер за 5 минут
- GitHub Actions — отчёт генерируется при каждом пуше
- Запуск одной командой

### Как запустить:
```bash
git clone https://github.com/nevermind532/devsecops-reporter.git
cd devsecops-reporter
python main.py
