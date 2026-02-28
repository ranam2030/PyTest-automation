def test_inventory_page_has_items(page):
    page.goto("https://www.saucedemo.com/inventory.html")
    assert page.locator(".inventory_item").count() > 0