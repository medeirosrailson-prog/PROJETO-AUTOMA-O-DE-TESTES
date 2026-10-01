import pytest
from guara import it

from tests.config.settings import BASE_URL
from tests.transactions.login_transaction import LoginTransaction


@pytest.mark.smoke
def test_login_com_sucesso_exibe_catalogo(app, login_data):
    credentials = login_data["valid_user"]
    app.at(
        LoginTransaction,
        url=BASE_URL,
        username=credentials["username"],
        password=credentials["password"],
    ).asserts(it.Contains, "inventory.html")
