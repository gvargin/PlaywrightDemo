import json
from pathlib import Path
from dataclasses import dataclass
from typing import Optional, Iterable

import pytest
import allure
from playwright.sync_api import Page

from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage


# =========================
# TEST DATA
# =========================

# Директория с тестовыми данными (JSON-файлы)
DATA_DIR = Path(__file__).parent / "test_data"


@dataclass
class SearchTestDada:
    """
    Модель тестовых данных для поиска.

    Используется для передачи данных из JSON в тесты
    в виде типизированного объекта.
    """
    id: str
    query: str
    expected_count: str
    description: str


def load_search_test_data(selected_ids: Optional[Iterable[str]] = None):
    """
    Загружает тестовые данные для поиска из JSON-файла.

    При необходимости позволяет отфильтровать данные
    по списку идентификаторов тест-кейсов.

    :param selected_ids: Список id тест-кейсов, которые нужно загрузить.
                         Если None — загружаются все данные.
    :return: Список объектов SearchTestDada
    """
    with open(DATA_DIR / "search_data.json", encoding="utf-8") as f:
        raw_data = json.load(f)["search_input"]

    # Фильтрация тестовых данных по id, если список передан
    if selected_ids is not None:
        raw_data = [item for item in raw_data if item["id"] in selected_ids]

    # Преобразование словарей из JSON в объекты dataclass
    return [
        SearchTestDada(
            id=item["id"],
            query=item["query"],
            expected_count=item["expected_results_count"],
            description=item["description"]
        )
        for item in raw_data
    ]


# =========================
# PYTEST FIXTURES
# =========================

@pytest.fixture(autouse=True)
def open_litres(page: Page):
    """
    Автоматически открывает главную страницу LitRes
    перед каждым тестом.
    """
    page.goto("https://www.litres.ru")
    yield page


@pytest.fixture
def home(page: Page) -> HomePage:
    """
    Фикстура для работы с главной страницей сайта.
    """
    return HomePage(page)


@pytest.fixture
def results(page: Page) -> SearchResultsPage:
    """
    Фикстура для работы со страницей результатов поиска.
    """
    return SearchResultsPage(page)


# =========================
# ALLURE REPORTING
# =========================

@pytest.fixture(autouse=True)
def screenshot_on_failure(page, request):
    """
    Делает скриншот страницы и прикрепляет его к Allure-отчёту,
    если тест завершился с ошибкой.
    """
    yield

    if request.node.rep_call.failed:
        screenshot = page.screenshot(full_page=True)
        allure.attach(
            screenshot,
            name="Screenshot on failure",
            attachment_type=allure.attachment_type.PNG
        )
