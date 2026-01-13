from playwright.sync_api import sync_playwright


# Запуск Playwright в синхронном режиме
with sync_playwright() as p:
    # Запуск браузера Chromium (headless=False — браузер открывается с UI)
    browser = p.chromium.launch(headless=False)

    # Открытие новой вкладки (страницы)
    page = browser.new_page()

    # Переход на указанный сайт
    page.goto("https://bigtesty.ru/")

    # Создание скриншота главной страницы и сохранение его в файл
    page.screenshot(path="screenshot/homepage.png")

    # Закрытие браузера
    browser.close()
