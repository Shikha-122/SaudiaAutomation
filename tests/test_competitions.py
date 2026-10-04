from pages.home_page import HomePage
from pages.competitions import CompetitionsPage


def test_competitions_arrows(page):
    home_page = HomePage(page)
    competitions_page = CompetitionsPage(page)

    # Open homepage
    home_page.open_homepage()

    # Wait for DOM to be fully loaded
    page.wait_for_load_state("domcontentloaded")

    # Scroll to Competitions section
    competitions_page.competitions_header.scroll_into_view_if_needed()

    # Verify Competitions section
    competitions_page.verify_competitions_header()

    # Click next arrow
    competitions_page.click_next_arrow()

    # Wait for carousel movement
    page.wait_for_timeout(1000)

    # Click previous arrow
    competitions_page.click_previous_arrow()

    # Wait for carousel movement
    page.wait_for_timeout(1000)


def test_competitions_pagination(page):
    home_page = HomePage(page)
    competitions_page = CompetitionsPage(page)

    # Open homepage
    home_page.open_homepage()

    # Wait for DOM to be fully loaded
    page.wait_for_load_state("domcontentloaded")

    # Scroll to Competitions section
    competitions_page.competitions_header.scroll_into_view_if_needed()

    # Verify Competitions section
    competitions_page.verify_competitions_header()

    # Click 3rd pagination dot
    competitions_page.click_slide(3)

    # Wait for carousel movement
    page.wait_for_timeout(1000)