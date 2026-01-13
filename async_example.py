from playwright.async_api import async_playwright
import asyncio


# Асинхронная функция, в которой будет выполняться сценарий Playwright
async def main():
    # Запуск Playwright в асинхронном режиме
    async with async_playwright() as p:
        # Запуск браузера Chromium (headless=False — браузер открывается с UI)
        browser = await p.chromium.launch(headless=False)

        # Открытие новой вкладки (страницы)
        page = await browser.new_page()

        # Переход на страницу с симулятором интервью
        await page.goto("https://bigtesty.ru/simulators/interview")

        # Создание скриншота страницы и сохранение его в файл
        await page.screenshot(path="screenshot/interview.png")

        # Закрытие браузера
        await browser.close()


# Запуск асинхронной функции main через event loop asyncio
asyncio.run(main())
