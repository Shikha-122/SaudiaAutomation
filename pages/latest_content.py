from playwright.sync_api import Page,expect
from pages.base_page import BasePage

class LatestContentPage(BasePage):

    def __init__(self,page:Page):
        super().__init__(page)

        self.play_now_button = page.locator("button:has-text('Play now'):visible").first

    def verify_play_now(self):
        expect(self.play_now_button).to_be_visible(timeout=15000)

    def click_play_now(self):
        with self.page.context.expect_page() as new_page_info:
            self.play_now_button.click()
        new_page = new_page_info.value
        new_page.wait_for_load_state()
        return new_page