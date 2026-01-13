from playwright.sync_api import Page, expect


# Пример использования локатора по ARIA role
# Поиск элемента по роли (link, button) и доступному имени
def test_locator_role(page: Page):
    page.get_by_role("link", name="Читают сейчас").click()
    expect(page).to_have_title("Рекомендации для вас- ищите на Литрес")
    page.get_by_role("button", name="Найти").click()
    expect(page.get_by_text("стивен кинг")).to_be_visible()


# Пример использования локатора по placeholder
# Поиск поля ввода по тексту placeholder
def test_locator_placeholder(page: Page):
    page.get_by_placeholder("Искать на Литрес").fill("игра престолов")
    page.keyboard.press("Enter")
    expect(page.get_by_text("Результаты поиска «игра престолов»")).to_be_visible()


# Пример использования локатора по data-testid
# Самый стабильный и рекомендуемый способ локализации элементов
def test_locator_datatestid(page: Page):
    page.get_by_test_id("header-catalog-button").click()
    expect(page.get_by_text("Бесплатные книги")).to_be_visible()


# Пример использования локатора по alt-тексту изображения
# Часто применяется для логотипов и иконок
def test_locator_alttext(page: Page):
    page.get_by_alt_text("Логотип Литрес").click()
    expect(page).to_have_url("https://www.litres.ru/")


# Пример использования XPath локатора
# Используется в крайних случаях, когда нет более стабильных селекторов
def test_locator_xpath(page: Page):
    expect(page.locator("xpath=//a[@title='YouTube']")).to_be_visible()
