from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from utils.logger import get_logger


class ProductsPage:

    # Locators
    PRODUCTS = (By.CSS_SELECTOR, ".card-title")
    PRODUCT_NAMES = (By.CSS_SELECTOR, ".card-title a")

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.logger = get_logger(__name__)

    def get_products(self):
        self.logger.info("Getting products from products page")

        return self.wait.until(
            EC.presence_of_all_elements_located(self.PRODUCTS)
        )

    def get_product_names(self):
        self.logger.info("Getting product names")

        products = self.wait.until(
            EC.presence_of_all_elements_located(self.PRODUCT_NAMES)
        )

        return [product.text for product in products]

    def select_product(self, product_name):
        self.logger.info(f"Selecting product: {product_name}")

        product_locator = (
        By.XPATH,
        f"//a[text()='{product_name}']"
    )

        self.wait.until(
        EC.element_to_be_clickable(product_locator)
    ).click()
    def add_to_cart(self):
        self.logger.info("Adding product to cart")

        add_to_cart_link = (
        By.LINK_TEXT,
        "Add to cart"
    )

        self.wait.until(
            EC.element_to_be_clickable(add_to_cart_link)
        ).click()

        self.wait.until(EC.alert_is_present())

        alert = self.driver.switch_to.alert
        self.logger.info(f"Cart alert: {alert.text}")
        alert.accept()