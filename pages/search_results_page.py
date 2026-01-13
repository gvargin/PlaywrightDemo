from playwright.sync_api import Locator
from pages.base_page import BasePage
import allure


class SearchResultsPage(BasePage):
    """
    Page Object для страницы результатов поиска.

    Содержит локаторы и действия, связанные с отображением
    и фильтрацией результатов поиска книг.
    """

    # ---------- Locators ----------

    @property
    def results_title(self) -> Locator:
        """
        Заголовок страницы результатов поиска.

        Используется для проверки, что страница поиска открылась.
        """
        return self.page.get_by_text("Результаты поиска")

    @property
    def books(self) -> Locator:
        """
        Список найденных книг.

        Представляет коллекцию карточек книг в результатах поиска.
        """
        return self.page.get_by_test_id("art__wrapper")

    @property
    def russian_filter(self) -> Locator:
        """
        Чекбокс фильтра по русскому языку.
        """
        return self.page.locator("label[for='languages-ru']")

    @property
    def russian_chip(self) -> Locator:
        """
        Чип активного фильтра «Русский».

        Используется для проверки, что фильтр успешно применён.
        """
        return self.page.locator(
            "[data-testid='chip-content']:has-text('Русский')"
        )

    # ---------- Actions ----------

    @allure.step("Применяем фильтр «Русский»")
    def apply_russian_filter(self) -> None:
        """
        Применяет фильтр по русскому языку в результатах поиска.
        """
        self.russian_filter.check()
