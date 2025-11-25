# DevSecOps Reporter — Универсальный агрегатор отчётов безопасности

**Один клик — один красивый HTML-отчёт со всеми сканерами безопасности и покрытия кода**

Живая версия отчёта (обновляется автоматически):  
https://nevermind532.github.io/devsecops-reporter/

---
Программа собирает JSON-отчёты от разных инструментов статического и динамического анализа кода (SAST, DAST, SCA, Coverage) и превращает их в **единый красивый HTML-отчёт** с графиками, статистикой и таблицами.

**Для кого:**
- DevSecOps-инженеры
- Команды безопасности приложений
- Разработчики, которым лень открывать 10 разных отчётов
- Аудиторы перед релизом

**Основные возможности:**
- Поддержка Bandit, OWASP ZAP, Semgrep, Coverage.py (легко добавить любой другой)
- Автоматическая статистика по критичности (Critical/High/Medium/Low)
- Красивый отчёт с Chart.js (тёмная тема, диаграмма-«пончик», таблицы)
- Полная автоматизация в GitHub Actions + публикация на GitHub Pages

---

### 3. Установка и запуск

```bash
# 1. Клонируем репозиторий
git clone https://github.com/nevermind532/devsecops-reporter.git
cd devsecops-reporter/devsecops-reporter

# 2. (Опционально) Устанавливаем зависимости
pip install jinja2

# 3. Запускаем — всё!
python run.py
# или
python main.py
```
### 4. пример использования проекта
Кидаем любой JSON - файл в папку reports_examples/ (например, my-bandit-scan.json) 
после чего заходим в терминал и запускаем наш проект
нас перекидывает на сайт где происходит отчет вашего кода

Пример результата:
<img width="1895" height="933" alt="image" src="https://github.com/user-attachments/assets/d6749ad9-bbca-4969-95bf-d5007d015212" />

### 5. Структура репозитория
devsecops-reporter/
├── run.py (или main.py)      ← запуск проекта
├── reporter/
│   └── parsers/              ← парсеры для каждого инструмента
│       ├── base.py           ← базовый класс
│       ├── bandit.py
│       ├── zap.py
│       ├── semgrep.py
│       └── coverage.py
├── templates/report.html     ← шаблон отчёта (Jinja2 + Chart.js)
├── reports_examples/         ← сюда кидаем любые JSON-отчёты
├── .github/workflows/        ← CI/CD + публикация на GitHub Pages
└── screenshot.png            ← пример готового отчёта

### 6. Технические требования

Python 3.8+
ОС: Windows / Linux / macOS
Зависимости: только jinja2 (pip install jinja2)

Никаких Docker, баз данных или сложных настроек — работает из коробки
### 7. Nevermind532 — автор проекта, архитектура, реализация всех парсеров, дизайн отчёта, CI/CD
Роль: Full-stack DevSecOps студент → junior+ уровень

### 8. Контакты и обратная связь

GitHub: https://github.com/nevermind532
почта: brawlctiker@gmail.com
