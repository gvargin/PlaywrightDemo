import json
from typing import Optional

from playwright.sync_api import Page
import pytest
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from pathlib import Path
from dataclasses import dataclass
from typing import Optional, Iterable

# TEST DATA
DATA_DIR = Path(__file__).parent / "test_data"

@dataclass
class SearchTestDada:
    id: str
    query: str
    expected_count: str

def load_search_test_data(ids: Optional[Iterable[str]] = None):

    with open(DATA_DIR / "search_data.json", encoding="utf-8") as f:
        raw_data = json.load(f)["search_input"]

    if ids is not None:

        raw_data = [item for item in raw_data if item["id"] in ids]

    return [
        SearchTestDada(
            id=item["id"],
            query=item["query"],
            expected_count=item["expected_results_count"]
        )
        for item in raw_data
    ]




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
