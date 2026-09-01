from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from utils.logger import get_logger


class CartPage:

    CART_LINK = (By.ID, "cartur")
    CART_PRODUCTS = (By.CSS_SELECTOR, "#tbodyid tr")

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.logger = get_logger(__name__)

    def open_cart(self):
        self.logger.info("Opening cart")

        self.wait.until(
            EC.element_to_be_clickable(self.CART_LINK)
        ).click()

    def get_cart_products(self):
        self.logger.info("Getting products from cart")

        return self.wait.until(
            EC.presence_of_all_elements_located(self.CART_PRODUCTS)
        )

    def is_product_in_cart(self, product_name):
        self.logger.info(f"Checking product in cart: {product_name}")

        products = self.get_cart_products()

        return any(
            product_name in product.text
            for product in products
        )