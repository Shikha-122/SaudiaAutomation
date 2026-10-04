from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class GameContentPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.game_card = self.page.get_by_role("group").filter(has_text="R3ACT")
        self.play_now_button = self.game_card.get_by_role(
            "button", name="Play Now"
        )

    def scroll_to_game_content(self):
        self.page.get_by_text("Games", exact=True).scroll_into_view_if_needed()
        self.page.wait_for_timeout(2000)

    def verify_play_now(self):
        expect(self.play_now_button).to_be_visible(timeout=15000)


    def click_play_now(self):
        self.play_now_button.scroll_into_view_if_needed()
        self.page.wait_for_timeout(2000)
        self.play_now_button.click()
        self.page.wait_for_timeout(3000)