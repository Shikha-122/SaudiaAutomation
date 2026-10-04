from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class CompetitionsPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.competitions_section = page.locator(
            "section",
            has=page.get_by_role("heading", name="Competitions")
        )

        self.competitions_header = self.competitions_section.get_by_role(
            "heading",
            name="Competitions"
        )

        self.next_arrow = self.competitions_section.get_by_role(
            "button",
            name="Next slide"
        )

        self.previous_arrow = self.competitions_section.get_by_role(
            "button",
            name="Previous slide"
        )

    def verify_competitions_header(self):
        expect(self.competitions_header).to_be_visible()

    def click_next_arrow(self):
        self.page.wait_for_load_state("domcontentloaded")
        self.next_arrow.click()

    def click_previous_arrow(self):
        self.page.wait_for_load_state("domcontentloaded")
        self.previous_arrow.click()

    def click_slide(self, slide_number):
        self.page.wait_for_load_state("domcontentloaded")
        self.competitions_section.get_by_role(
            "tab",
            name=f"Go to slide {3}"
        ).click()