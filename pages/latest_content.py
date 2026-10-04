from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class LatestContentPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        # View All
        self.view_all = page.get_by_text("View All", exact=True)

        # All visible Play now buttons
        self.play_now_buttons = page.locator(
            "button:has-text('Play now'):visible"
        )

    def click_view_all(self):
        self.view_all.click()

    def verify_play_now(self):
        expect(self.play_now_buttons.nth(2)).to_be_visible(timeout=15000)

    def click_third_play_now(self):
        print(
            "Visible Play now buttons:",
            self.play_now_buttons.count()
        )

        with self.page.context.expect_page(timeout=15000) as new_page_info:
            self.play_now_buttons.nth(2).click()

        new_page = new_page_info.value
        new_page.wait_for_load_state()

        print("New tab URL:", new_page.url)

        return new_page