from pages.home_page import HomePage
from pages.game_content import GameContentPage


def test_r3act_game_content(page):
    home_page = HomePage(page)
    game_content_page = GameContentPage(page)

    home_page.open_homepage()

    game_content_page.scroll_to_game_content()
    game_content_page.verify_play_now()
    game_content_page.click_play_now()