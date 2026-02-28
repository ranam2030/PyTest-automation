class HomePage:
    def __init__(self, page):
        self.page = page

    def is_logged_in(self):
        return self.page.is_visible(".inventory_list")