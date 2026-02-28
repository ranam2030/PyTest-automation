class CheckoutPage:
    def __init__(self, page):
        self.page = page

    def add_item_and_checkout(self):
        self.page.click("#add-to-cart-sauce-labs-backpack")
        self.page.click(".shopping_cart_link")