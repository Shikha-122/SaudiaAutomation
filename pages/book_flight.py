from playwright.sync_api import Page
from pages.base_page import BasePage


class BookFlightPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    def verify_book_flight_page_opened(self):
        self.page.wait_for_load_state("domcontentloaded")
        print("Book Flight URL:", self.page.url)

