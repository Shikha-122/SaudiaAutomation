from playwright.sync_api import Page,expect
from pages.base_page import BasePage

class HomePage(BasePage):
    def __init__(self,page:Page):
        super().__init__(page) # Calling BasePage Constructor

        self.book_flight_link = page.locator("//a[.='Book flights']")
        self.news_link=page.locator("a:has-text('News')")
        self.games_link=page.locator("a:has-text('Games')")
        self.competitions_link=page.locator("a:has-text('Competitions')")
        self.english_button=page.get_by_role("button", name="EN")
        self.arabic_button=page.locator("button:has-text('AR')")
        self.arabic_games_link = page.locator("a:has-text('الألعاب')")
    def open_homepage(self):
        self.navigate("https://takeyourseat.saudia.com/")

    def verify_homepage_url(self):
        self.verify_url("https://takeyourseat.saudia.com/")

    def verify_homepage_title(self):
        self.verify_title("Saudia | Take your seat")

    def verify_book_flight(self):
        expect(self.book_flight_link).to_be_visible()

    def click_book_flight(self):
        self.book_flight_link.click()
        self.page.wait_for_timeout(5000)

    def verify_news(self):
        expect(self.news_link).to_be_visible()
    def click_news(self):
        self.news_link.click()
        self.page.wait_for_timeout(2000)

    def verify_games(self):
        expect(self.games_link).to_be_visible()
    def click_games(self):
        self.games_link.click()
        self.page.wait_for_timeout(2000)

    def verify_competitions(self):
        expect(self.competitions_link).to_be_visible()

    def click_competitions(self):
        self.competitions_link.click()
        self.page.wait_for_timeout(3000)

    def verify_english(self):
        expect(self.english_button).to_be_visible()
    def verify_arabic(self):
        expect(self.arabic_button).to_be_visible()
    def click_arabic(self):
        self.arabic_button.click()
        self.page.wait_for_timeout(2000)

    def verify_arabic_games(self):
        expect(self.arabic_games_link).to_be_visible()