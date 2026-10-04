from pages.home_page import HomePage
from pages.latest_content import LatestContentPage


def test_latest_content(page):
    home_page = HomePage(page)
    latest_content = LatestContentPage(page)

    home_page.open_homepage()

    latest_content.click_view_all()
    latest_content.verify_play_now()

    new_page = latest_content.click_third_play_now()

    assert new_page.url != "", "New tab did not open a valid URL"

    print("Final video tab URL:", new_page.url)

    new_page.close()