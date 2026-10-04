from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class PartnerUpdatesPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.partner_updates_heading = page.locator(
            "h2:has-text('Partner Updates')"
        )

        self.all_tab = page.get_by_role("button", name="All")
        self.esports_world_cup_tab = page.get_by_role(
            "button", name="Esports World Cup"
        )
        self.spl_tab = page.get_by_role("button", name="SPL")
        self.formula_e_tab = page.get_by_role("button", name="Formula E")

        self.read_more_button = page.get_by_role(
            "button", name="Read More", exact=True
        )


    def verify_partner_updates_section(self):
        expect(self.partner_updates_heading).to_be_visible(timeout=10000)

    def click_all_tab(self):
        self.all_tab.click()
        self.page.wait_for_timeout(1000)
        self.partner_updates_heading.scroll_into_view_if_needed()
        self.page.wait_for_timeout(1000)

    def click_esports_world_cup_tab(self):
        self.esports_world_cup_tab.click()
        self.page.wait_for_timeout(1000)

    def click_spl_tab(self):
        self.spl_tab.click()
        self.page.wait_for_timeout(1000)

    def click_formula_e_tab(self):
        self.formula_e_tab.click()
        self.page.wait_for_timeout(1000)

    def click_read_more(self):
        expect(
            self.read_more_button.first
        ).to_be_visible(timeout=10000)

        with self.page.expect_popup() as new_page_info:
            self.read_more_button.first.evaluate(
                "element => element.click()"
            )

        new_page = new_page_info.value

        new_page.wait_for_load_state("domcontentloaded")
        new_page.wait_for_timeout(5000)