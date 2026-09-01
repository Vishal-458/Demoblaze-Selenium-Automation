import os

import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def driver(request):
    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver

    # Capture screenshot if test fails
    if request.node.rep_call.failed:
        os.makedirs("screenshots", exist_ok=True)

        screenshot_name = f"{request.node.name}.png"
        screenshot_path = os.path.join(
            "screenshots",
            screenshot_name
        )

        driver.save_screenshot(screenshot_path)

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    setattr(item, f"rep_{report.when}", report)


@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 10)