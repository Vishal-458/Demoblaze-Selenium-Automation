from utils.helpers import load_test_data

import os

from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from utils.config import BASE_URL

test_data = load_test_data("test_data/test_data.json")

test_data["valid_login"]["username"] = os.getenv(
    "DEMOBLAZE_USERNAME",
    test_data["valid_login"]["username"]
)

test_data["valid_login"]["password"] = os.getenv(
    "DEMOBLAZE_PASSWORD",
    test_data["valid_login"]["password"]
)


def test_valid_login(driver, wait):

    driver.get(BASE_URL)

    login_page = LoginPage(driver, wait)

    login_page.open_login_popup()
    login_page.enter_username(test_data["valid_login"]["username"])
    login_page.enter_password(test_data["valid_login"]["password"])
    login_page.click_login()

    welcome_message = login_page.get_welcome_message()

    assert "Welcome" in welcome_message


def test_invalid_login(driver, wait):

    driver.get(BASE_URL)

    login_page = LoginPage(driver, wait)

    login_page.open_login_popup()
    login_page.enter_username(test_data["invalid_login"]["username"])
    login_page.enter_password(test_data["invalid_login"]["password"])
    login_page.click_login()

    alert = wait.until(EC.alert_is_present())

    assert alert.text in [
        "Wrong password.",
        "User does not exist."
    ]

    alert.accept()