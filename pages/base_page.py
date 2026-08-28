from playwright.sync_api import Page,expect

class BasePage:
    def __init__(self,page:Page):
        self.page=page
    def navigate(self, url:str):
        self.page.goto(url,wait_until="domcontentloaded")
    def verify_url(self,url:str):
        expect(self.page).to_have_url(url)
    def verify_title(self,title: str):
        expect(self.page).to_have_title(title)