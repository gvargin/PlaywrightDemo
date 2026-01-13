# PlaywrightDemo

Автоматизированные UI тесты для сайта **LitRes** с использованием **Playwright** и **pytest**.

> 💡 Этот код создан в рамках курса на YouTube: [Playwright с нуля](https://www.youtube.com/watch?v=Y7p6a5HowLU&list=PLXFaXx3Pg2MOJwUOXpfpQDcx2UJfQLS4i)  

---

## 🚀 Возможности проекта

- Поиск книг на LitRes
- Применение фильтров (например, "Русский")
- Проверка количества результатов поиска
- Скриншоты и отчёты Allure
- Асинхронные и синхронные тесты

---

## 🛠 Стек технологий

- Python 3.11
- Playwright (sync & async)
- pytest
- Allure & pytest-html

---

---

## 📝 Как запускать тесты

С **Allure**:

```bash
pytest tests/test_search.py --alluredir=reports/allure_raw
allure serve reports/allure_raw
```


## 🔗 Полезные ссылки

- 🌐 [Playwright Docs](https://playwright.dev/python/)
- 🐍 [pytest Docs](https://docs.pytest.org/)
- 📊 [Allure Reports](https://docs.qameta.io/allure/)
- ▶️ [Мой YouTube канал](https://www.youtube.com/@GVARGIN/videos)



