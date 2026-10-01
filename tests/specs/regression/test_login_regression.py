import pytest
from guara import it

from tests.config.settings import BASE_URL
from tests.transactions.login_transaction import LoginTransaction


@pytest.mark.regression
@pytest.mark.login
def test_login_com_credenciais_invalidas_exibe_erro(app, login_data):
    credentials = login_data["invalid_user"]
    app.at(
        LoginTransaction,
        url=BASE_URL,
        username=credentials["username"],
        password=credentials["password"],
    ).asserts(it.Contains, "Username and password do not match")


@pytest.mark.regression
@pytest.mark.login
def test_usuario_bloqueado_nao_acessa_catalogo(app, login_data):
    credentials = login_data["locked_user"]
    app.at(
        LoginTransaction,
        url=BASE_URL,
        username=credentials["username"],
        password=credentials["password"],
    ).asserts(it.Contains, "locked out")
