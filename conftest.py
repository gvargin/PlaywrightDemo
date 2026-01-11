from playwright.sync_api import Page
import pytest
import json
from pathlib import Path

from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage

DATA_DIR = Path(__file__).parent / "test_data"


@pytest.fixture(autouse=True)
def open_litres(page: Page):
    page.goto("https://www.litres.ru")

    yield page


@pytest.fixture
def home(page: Page) -> HomePage:
    return HomePage(page)


@pytest.fixture
def results(page: Page) -> SearchResultsPage:
    return SearchResultsPage(page)
