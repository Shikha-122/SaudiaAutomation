from pages.home_page import HomePage

def test_launch_website(page):
    home_page=HomePage(page)
    home_page.open_homepage()
    home_page.verify_homepage_url()
    home_page.verify_homepage_title()
    home_page.verify_news()
    home_page.click_news()
    home_page.verify_games()
    home_page.click_games()
    home_page.verify_competitions()
    home_page.click_competitions()
    home_page.verify_english()
    home_page.verify_arabic()
    home_page.click_arabic()
    home_page.verify_arabic_games()