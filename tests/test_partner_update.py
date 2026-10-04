from pages.home_page import HomePage
from pages.partner_updates import PartnerUpdatesPage


def test_partner_updates_tabs(page):

    home_page = HomePage(page)
    home_page.open_homepage()

    partner_updates = PartnerUpdatesPage(page)

    partner_updates.verify_partner_updates_section()

    partner_updates.click_all_tab()
    partner_updates.click_esports_world_cup_tab()
    partner_updates.click_spl_tab()
    partner_updates.click_formula_e_tab()
    partner_updates.click_all_tab()
    partner_updates.click_read_more()

