import pytest
from playwright.sync_api import expect
from conftest import results, load_search_test_data
import allure


# Проверка применения фильтра «Русский» для произвольных поисковых запросов
# Используется простая параметризация без тестовых данных из JSON
@pytest.mark.parametrize("query", ["Python", "Игра Престолов", "Стивен Кинг"])
def test_filters(home, results, query):
    allure.dynamic.title(f"Поиск книги {query}")
    home.search(query, True)
    results.apply_russian_filter()
    expect(results.russian_chip).to_be_visible()


# Проверка применения фильтра «Русский» для конкретных тест-кейсов,
# загружаемых из JSON-файла по их идентификаторам
@pytest.mark.parametrize(
    "td",
    load_search_test_data(selected_ids=["python_books", "game_of_thrones"]),
    ids=lambda td: td.id
)
def test_filters2(home, results, td):
    allure.dynamic.title(td.description)
    home.search(td.query, True)
    results.apply_russian_filter()
    expect(results.russian_chip).to_be_visible()


# Проверка количества найденных книг в результатах поиска
# для заранее заданных тестовых данных из JSON
@pytest.mark.parametrize(
    "td",
    load_search_test_data(selected_ids=["richard_bransen", "stephen_king"]),
    ids=lambda td: td.id
)
def test_results_count(home, results, td):
    allure.dynamic.title(td.description)
    home.search(td.query)
    expect(results.results_title).to_contain_text(td.query)
    expect(results.books).to_have_count(td.expected_count, timeout=10000)
