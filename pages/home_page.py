from playwright.sync_api import Locator
from pages.base_page import BasePage
import allure


class HomePage(BasePage):
    """
    Page Object для главной страницы сайта LitRes.

    Содержит локаторы и действия, связанные с поиском книг
    на главной странице.
    """

    # ---------- Locators ----------

    @property
    def search_input(self) -> Locator:
        """
        Поле ввода поискового запроса.

        :return: Locator для поля поиска
        """
        return self.page.get_by_placeholder("Искать на Литрес")

    @property
    def search_button(self) -> Locator:
        """
        Кнопка запуска поиска.

        :return: Locator для кнопки поиска
        """
        return self.page.get_by_test_id("search__button")

    # ---------- Actions ----------

    @allure.step("Ищем книгу: {query}")
    def search(self, query: str, submit_with_enter: bool = False) -> None:
        """
        Выполняет поиск книги по заданному запросу.

        Может запускать поиск двумя способами:
        - нажатием Enter
        - кликом по кнопке поиска

        :param query: Текст поискового запроса
        :param submit_with_enter: Если True — поиск запускается клавишей Enter,
                                  если False — кликом по кнопке
        """
        self.search_input.fill(query)

        if submit_with_enter:
            self.page.keyboard.press("Enter")
        else:
            self.search_button.click()
