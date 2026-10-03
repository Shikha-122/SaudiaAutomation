from pages.home_page import HomePage
from pages.latest_content import LatestContentPage

def test_latest_content(page):
    home_page=HomePage(page)
    latest_content=LatestContentPage(page)
    home_page.open_homepage()
    latest_content.verify_play_now()
    latest_content.click_play_now()