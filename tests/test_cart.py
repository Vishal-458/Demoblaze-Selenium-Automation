from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from utils.config import BASE_URL


def test_add_product_to_cart(driver, wait):

    driver.get(BASE_URL)

    products_page = ProductsPage(driver, wait)

    products_page.select_product("Samsung galaxy s6")
    products_page.add_to_cart()

    cart_page = CartPage(driver, wait)

    cart_page.open_cart()

    assert cart_page.is_product_in_cart("Samsung galaxy s6")