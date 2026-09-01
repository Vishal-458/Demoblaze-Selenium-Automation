from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import get_logger


class LoginPage:

    # Locators
    LOGIN_LINK = (By.ID, "login2")
    USERNAME_INPUT = (By.ID, "loginusername")
    PASSWORD_INPUT = (By.ID, "loginpassword")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Log in']")
    WELCOME_USER = (By.ID, "nameofuser")

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.logger = get_logger(__name__)

    def open_login_popup(self):
        self.logger.info("Opening login popup")
        self.wait.until(
        EC.element_to_be_clickable(self.LOGIN_LINK)
    ).click()


    def enter_username(self, username):
        self.logger.info("Entering username")
        self.wait.until(
            EC.visibility_of_element_located(self.USERNAME_INPUT)
        ).send_keys(username)


    def enter_password(self, password):
        self.logger.info("Entering password")
        self.wait.until(
            EC.visibility_of_element_located(self.PASSWORD_INPUT)
        ).send_keys(password)


    def click_login(self):
        self.logger.info("Clicking Login button")
        self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        ).click()


    def get_welcome_message(self):
        self.logger.info("Checking welcome message")
        return self.wait.until(
            EC.visibility_of_element_located(self.WELCOME_USER)
        ).text