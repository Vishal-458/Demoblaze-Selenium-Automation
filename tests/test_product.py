from pages.products_page import ProductsPage
from utils.config import BASE_URL


def test_products_are_displayed(driver, wait):

    driver.get(BASE_URL)

    products_page = ProductsPage(driver, wait)

    product_names = products_page.get_product_names()

    assert len(product_names) > 0