import pytest
from guara import it
from guara.application import Application

from tests.config.settings import BASE_URL
from tests.transactions.login_transaction import LoginTransaction

pytest_plugins = ("tests.fixtures.data_fixture", "tests.fixtures.driver")


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
