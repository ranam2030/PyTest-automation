from pages.login_page import LoginPage
from pages.checkout_page import CheckoutPage
from utils.config import USERNAME, PASSWORD

def test_user_can_add_item_to_cart(page):
    LoginPage(page).login(USERNAME, PASSWORD)
    checkout = CheckoutPage(page)
    checkout.add_item_and_checkout()

    assert page.is_visible(".cart_item")