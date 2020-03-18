import pytest
from Invoice import Invoice


@pytest.fixture()
def products():
    products = {'Pen': {'qnt': 10, 'unit_price': 3.75, 'discount': 5},
                'Notebook': {'qnt': 5, 'unit_price': 7.5, 'discount': 10}}
    return products

@pytest.fixture()
def invoice():
    invoice = Invoice()
    return invoice


def test_CanCalucateTotalImpurePrice(invoice, products):
    invoice.totalImpurePrice(products)
    assert invoice.totalImpurePrice(products) == 75

def test_CanCalucateTotalDiscount(invoice, products):
    invoice.totalDiscount(products)
    assert invoice.totalDiscount(products) == 5.62

def test_CanCalucateTotalPurePrice(invoice, products):
    invoice.totalPurePrice(products)
    assert invoice.totalPurePrice(products) == 69.38

def test_addProduct(invoice):
    invoice.addProduct(10,100,5)
    assert invoice.addProduct(10,100,5) == invoice.items
def test_remove_product(invoice):
    invoice.addProduct(10, 100, 5)
    invoice.addProduct(20, 100, 5)
    invoice.addProduct(30, 100, 5)
    assert len(invoice.items) == 3
    invoice.remove_product(1)
    assert len(invoice.items) == 2
    invoice.remove_product(1)
    assert len(invoice.items) == 1





