from playwright.sync_api import Page, expect
import pytest
from conftest import results
from urllib.parse import quote, quote_plus


def test_main_actions(page, home, results, query):
    query = "python"
    home.search(query, True)

    expect(page).to_have_url(f"https://www.litres.ru/search/?q={quote_plus(query)}")

    results.apply_russian_filter()
    expect(results.russian_chip).to_be_visible()


def test_waiting(page, home, results):
    query = "Самоучитель Python"
    home.search(query)

    expect(page).to_have_url(f"https://www.litres.ru/search/?q={quote_plus(query)}")
    expect(results.results_title).to_contain_text(query)
    expect(results.books).to_have_count(3, timeout=10000)
