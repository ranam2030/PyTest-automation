from pages.login_page import LoginPage
from pages.home_page import HomePage
from utils.config import USERNAME, PASSWORD

def test_user_can_login(page):
    login = LoginPage(page)
    home = HomePage(page)

    login.login(USERNAME, PASSWORD)
    assert home.is_logged_in()