import pytest
from playwright.sync_api import Page , expect

def test_launch_website(page:Page):

    #Launch URl
    page.goto('https://takeyourseat.saudia.com/', wait_until="domcontentloaded")
    expect(page).to_have_url('https://takeyourseat.saudia.com/')
    expect(page).to_have_title('Saudia | Take your seat')

    # Verifying Url
    # print('Url:', page.url)

def verify_logo(page:Page):
    logo=page.locator("//a[@class='flex items-center gap-2']")
    expect(logo).to_be_visible()

def verify_home(page:Page):
    home= page.locator("//a[text()='Home']")
    expect(home).to_be_visible()

def verify_news(page:Page):
    news=page.locator("//a[text()='News']")
    expect(news).to_be_visible()

def verify_games(page:Page):
    games=page.locator("//a[text()='Games']")
    expect(games).to_be_visible()

def verify_competitions(page:Page):
    competitions=page.locator("//a[text()='Competitions']")
    expect(competitions).to_be_visible()

def verify_bookflight(page:Page):
    bookflight=page.locator("//a[text()='Book flights']")
    expect(bookflight).to_be_visible()

def verify_english_button(page:Page):
    eng=page.locator("//button[@class='btn text-white bg-saudiaGreen']")
    expect(eng).to_be_visible()

def verify_arabic_button(page:Page):
    ar=page.locator("//button[@class='btn text-green-700']")
    expect(ar).to_be_visible()




