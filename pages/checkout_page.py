from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from utils.logger import get_logger


class CheckoutPage:

    PLACE_ORDER_BUTTON = (By.XPATH, "//button[text()='Place Order']")
    ORDER_MODAL = (By.ID, "orderModal")
    NAME_INPUT = (By.ID, "name")
    COUNTRY_INPUT = (By.ID, "country")
    CITY_INPUT = (By.ID, "city")
    CARD_INPUT = (By.ID, "card")
    MONTH_INPUT = (By.ID, "month")
    YEAR_INPUT = (By.ID, "year")
    PURCHASE_BUTTON = (By.XPATH, "//button[text()='Purchase']")
    ORDER_CONFIRMATION = (By.CSS_SELECTOR, ".sweet-alert h2")

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.logger = get_logger(__name__)

    def open_place_order(self):
        self.logger.info("Opening Place Order form")

        self.wait.until(
        EC.element_to_be_clickable(self.PLACE_ORDER_BUTTON)
    ).click()

        self.wait.until(
        EC.visibility_of_element_located(self.ORDER_MODAL)
    )

    def enter_order_details(self, name, country, city, card, month, year):
        self.logger.info("Entering order details")

        self.wait.until(
            EC.visibility_of_element_located(self.NAME_INPUT)
        ).send_keys(name)

        self.wait.until(
            EC.visibility_of_element_located(self.COUNTRY_INPUT)
        ).send_keys(country)

        self.wait.until(
            EC.visibility_of_element_located(self.CITY_INPUT)
        ).send_keys(city)

        self.wait.until(
            EC.visibility_of_element_located(self.CARD_INPUT)
        ).send_keys(card)

        self.wait.until(
            EC.visibility_of_element_located(self.MONTH_INPUT)
        ).send_keys(month)

        self.wait.until(
            EC.visibility_of_element_located(self.YEAR_INPUT)
        ).send_keys(year)

    def purchase_order(self):
        self.logger.info("Purchasing order")

        self.wait.until(
            EC.element_to_be_clickable(self.PURCHASE_BUTTON)
        ).click()

    def get_order_confirmation(self):
        self.logger.info("Checking order confirmation")

        return self.wait.until(
            EC.visibility_of_element_located(
                self.ORDER_CONFIRMATION
            )
        ).text