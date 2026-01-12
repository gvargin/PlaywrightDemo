import pytest
from playwright.sync_api import expect
from conftest import results, load_search_test_data


@pytest.mark.parametrize("query", ["Python", "Игра Престолов", "Стивен Кинг"])
def test_filters(home, results, query):
    home.search(query, True)
    results.apply_russian_filter()
    expect(results.russian_chip).to_be_visible()

@pytest.mark.parametrize("td", load_search_test_data(ids=["python_books", "game_of_thrones"]))
def test_filters2(home, results, td):
    home.search(td.query, True)
    results.apply_russian_filter()
    expect(results.russian_chip).to_be_visible()

@pytest.mark.parametrize("td", load_search_test_data(ids=["richard_bransen", "stephen_king"]))
def test_results_count(home, results, td):
    home.search(td.query)
    expect(results.results_title).to_contain_text(td.query)
    expect(results.books).to_have_count(td.expected_count, timeout=10000)
