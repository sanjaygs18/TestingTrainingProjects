import pytest

@pytest.fixture
def fixtureMethod():
    print("This is a fixture method")

def test_login_app(fixtureMethod):
    print("This is a login app method")

def test_search_product(fixtureMethod):
    print("This is a search product functionality")

def test_addItemToCart(fixtureMethod):
    print("This is add item to cart functionality")

def test_checkingAddItem(fixtureMethod):
    print("This is checking items in cart functionality")

def test_paymentDetails(fixtureMethod):
    print("This is payment processing application")

def test_deliveryStatus():
    print("This is delivery status functionality")

def test_removeItemFromCart():
    print("This is remove item from cart")

def test_logout():
    print("This is logout functionality")