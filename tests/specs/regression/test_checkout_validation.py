import pytest
from guara import it

from tests.transactions.add_to_cart_transaction import AddToCartTransaction
from tests.transactions.checkout_validation_transaction import (
    CheckoutValidationTransaction,
)
from tests.transactions.open_cart_transaction import OpenCartTransaction


@pytest.mark.regression
def test_checkout_sem_preencher_dados_exibe_erro(logged_in_app):
    logged_in_app.when(AddToCartTransaction)
    logged_in_app.when(OpenCartTransaction)
    logged_in_app.when(
        CheckoutValidationTransaction,
        first_name="",
        last_name="",
        postal_code="",
    ).asserts(it.Contains, "First Name is required")


@pytest.mark.regression
def test_checkout_parcial_exige_cep(logged_in_app):
    logged_in_app.when(AddToCartTransaction)
    logged_in_app.when(OpenCartTransaction)
    logged_in_app.when(
        CheckoutValidationTransaction,
        first_name="Pessoa",
        last_name="Exemplo",
        postal_code="",
    ).asserts(it.Contains, "Postal Code is required")
