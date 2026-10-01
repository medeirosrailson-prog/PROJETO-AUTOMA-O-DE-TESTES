import hashlib
import logging
import re
from pathlib import Path

import pytest
from guara import it
from guara.application import Application
from pytest_html import extras
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.remote.webdriver import WebDriver

from tests.config.settings import BASE_URL
from tests.transactions.login_transaction import LoginTransaction

pytest_plugins = ("tests.fixtures.data_fixture", "tests.fixtures.driver")

logger = logging.getLogger(__name__)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item: pytest.Item, call: pytest.CallInfo):
    outcome = yield
    report = outcome.get_result()
    if report.when != "call" or not report.failed:
        return

    driver = item.funcargs.get("driver")
    if not isinstance(driver, WebDriver):
        return

    reports_directory = Path("reports") / "screenshots"
    safe_test_name = re.sub(r"[^A-Za-z0-9_.-]+", "_", item.nodeid)[:80]
    test_hash = hashlib.sha256(item.nodeid.encode("utf-8")).hexdigest()[:12]
    screenshot_path = reports_directory / f"{safe_test_name}-{test_hash}.png"

    try:
        reports_directory.mkdir(parents=True, exist_ok=True)
        if not driver.save_screenshot(str(screenshot_path)):
            raise OSError(f"WebDriver did not save screenshot to {screenshot_path}")

        report_extras = getattr(report, "extras", [])
        report_extras.append(
            extras.image(
                driver.get_screenshot_as_base64(),
                name="Screenshot on failure",
            )
        )
        report.extras = report_extras
    except (OSError, WebDriverException) as error:
        message = f"Screenshot capture failed: {error}"
        logger.warning("%s for %s", message, item.nodeid)
        report.sections.append(("Screenshot capture", message))


@pytest.fixture
def app(driver):
    return Application(driver)


@pytest.fixture
def logged_in_app(app, login_data):
    credentials = login_data["valid_user"]
    app.at(
        LoginTransaction,
        url=BASE_URL,
        username=credentials["username"],
        password=credentials["password"],
    ).asserts(it.Contains, "inventory.html")
    return app
