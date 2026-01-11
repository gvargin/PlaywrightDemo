from playwright.sync_api import Locator
from pages.base_page import BasePage


class SearchResultsPage(BasePage):

    # Locators
    @property
    def results_title(self) -> Locator:
        return self.page.get_by_text("Результаты поиска")

    @property
    def books(self) -> Locator:
        return self.page.get_by_test_id("art__wrapper")

    @property
    def russian_filter(self) -> Locator:
        return self.page.locator("label[for='languages-ru']")

    @property
    def russian_chip(self) -> Locator:
        return self.page.locator("[data-testid='chip-content']:has-text('Русский')")

    # Actions

    def apply_russian_filter(self) -> None:
        self.russian_filter.check()
