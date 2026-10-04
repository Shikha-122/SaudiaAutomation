from pages.home_page import HomePage
from pages.book_flight import BookFlightPage


def test_book_flight_opens_new_tab(page):
    home_page = HomePage(page)

    home_page.open_homepage()

    new_page = home_page.click_book_flight()

    book_flight_page = BookFlightPage(new_page)

    book_flight_page.verify_book_flight_page_opened()

    assert new_page.url != page.url
