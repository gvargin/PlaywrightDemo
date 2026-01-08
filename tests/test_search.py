from playwright.sync_api import Page, expect

def test_main_actions(page: Page):
    page.get_by_test_id("search__input").fill("python")
    page.keyboard.press("Enter")

    expect(page).to_have_url("https://www.litres.ru/search/?q=python")
    page.locator("xpath=//*[@aria-description='Книги, которые можно читать без ограничений с активной Литрес: Подпиской']").dblclick()
    page.locator("xpath=//*[@aria-description='Книги, которые можно взять по Литрес: Абонементу']").click()


    # page.locator("label[for='languages-ru']").check(force=True)
    page.check("label[for='languages-ru']")

    page.locator("button:has-text('Принять')").click()


    page.pause()

def test_waiting(page: Page):
    page.get_by_placeholder("Искать на Литрес").fill("Самоучитель Python")
    page.get_by_test_id("search__button").click()

    expect(page.get_by_text("Результаты поиска «Самоучитель Python»")).to_be_visible()
    expect(page).to_have_title("Результаты поиска по книгам: «Самоучитель Python»")

    # expect(page.get_by_text("TestError"), "Show log message for test error demo").to_be_visible()

    result_title = page.locator("text=Результаты поиска «Самоучитель Python»")
    result_title.wait_for(timeout=7000)

    #bad test example
    #page.wait_for_timeout(10000)
    #assert "Результаты поиска «Самоучитель Python»" in page.inner_text("body")

    books = page.get_by_test_id("art__wrapper")
    expect(books).to_have_count(24, timeout=10000)