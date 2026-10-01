import os
from collections.abc import Iterator
from tempfile import TemporaryDirectory

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver


@pytest.fixture
def driver() -> Iterator[WebDriver]:
    options = Options()
    options.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False,
        },
    )
    options.add_argument("--disable-features=PasswordLeakDetection")
    options.add_argument("--safebrowsing-disable-leak-detection")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-extensions")

    headless_default = "true" if os.getenv("CI") else "false"
    if os.getenv("HEADLESS", headless_default).lower() == "true":
        options.add_argument("--headless=new")

    if os.getenv("CI"):
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

    with TemporaryDirectory(prefix="saucedemo-chrome-") as user_data_dir:
        options.add_argument(f"--user-data-dir={user_data_dir}")
        browser = webdriver.Chrome(options=options)
        try:
            yield browser
        finally:
            browser.quit()
