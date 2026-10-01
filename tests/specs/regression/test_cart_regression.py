import pytest
from guara import it

from tests.transactions.add_to_cart_transaction import AddToCartTransaction
from tests.transactions.continue_shopping_transaction import (
    ContinueShoppingTransaction,
)
from tests.transactions.open_cart_transaction import OpenCartTransaction
from tests.transactions.remove_from_cart_transaction import (
    RemoveFromCartTransaction,
)
from tests.transactions.reset_cart_transaction import ResetCartTransaction
from tests.transactions.view_cart_transaction import ViewCartTransaction


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.e2e
def test_adicionar_produto_ao_carrinho(logged_in_app):
    logged_in_app.when(AddToCartTransaction).asserts(it.IsEqualTo, "1")


@pytest.mark.regression
def test_remover_produto_do_carrinho(logged_in_app):
    logged_in_app.when(AddToCartTransaction)
    logged_in_app.when(OpenCartTransaction).asserts(it.Contains, "Sauce Labs Backpack")
    logged_in_app.when(RemoveFromCartTransaction).asserts(it.IsEqualTo, 0)


@pytest.mark.regression
def test_continuar_comprando_apos_adicionar_produto(logged_in_app):
    logged_in_app.when(AddToCartTransaction).asserts(it.IsEqualTo, "1")
    logged_in_app.when(OpenCartTransaction).asserts(it.Contains, "Sauce Labs Backpack")
    logged_in_app.when(ContinueShoppingTransaction).asserts(
        it.Contains, "inventory.html"
    )


@pytest.mark.regression
def test_resetar_carrinho_limpa_o_indicador(logged_in_app):
    logged_in_app.when(AddToCartTransaction).asserts(it.IsEqualTo, "1")
    logged_in_app.when(ResetCartTransaction).asserts(it.IsEqualTo, "0")


@pytest.mark.regression
def test_acessar_carrinho_vazio_nao_exibe_produtos(logged_in_app):
    logged_in_app.when(ViewCartTransaction).asserts(it.IsEqualTo, 0)
