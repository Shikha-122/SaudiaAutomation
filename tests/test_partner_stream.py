from pages.home_page import HomePage
from pages.partner_stream import PartnerStreamPage


def test_partner_stream_watch_now(page):
    home_page = HomePage(page)
    partner_stream = PartnerStreamPage(page)

    home_page.open_homepage()
    partner_stream.click_watch_now()

    page.wait_for_timeout(5000)