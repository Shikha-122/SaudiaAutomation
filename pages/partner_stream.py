from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class PartnerStreamPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.partner_stream_section = page.locator(
            "h2:has-text('Partner Streams')"
        ).locator("..")

        self.watch_now = self.partner_stream_section.locator(
            "a:has-text('Watch Now')"
        )

    def click_watch_now(self):
        expect(self.watch_now.first).to_be_visible()
        expect(self.watch_now.first).to_be_enabled()

        self.watch_now.first.click()

        self.page.wait_for_load_state("domcontentloaded")
        self.page.wait_for_timeout(5000)