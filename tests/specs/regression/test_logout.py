import pytest
from guara import it

from tests.config.settings import BASE_URL
from tests.transactions.logout_transaction import LogoutTransaction


@pytest.mark.regression
@pytest.mark.e2e
@pytest.mark.login
def test_logout_retorna_para_tela_de_login(logged_in_app):
    logged_in_app.when(LogoutTransaction).asserts(it.IsEqualTo, BASE_URL)
