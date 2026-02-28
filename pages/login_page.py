from pages.base_page import BasePage
from utils.config import BASE_URL

class LoginPage(BasePage):
    def login(self, username, password):
        self.page.goto(BASE_URL)
        self.page.fill("#user-name", username)
        self.page.fill("#password", password)
        self.page.click("#login-button")