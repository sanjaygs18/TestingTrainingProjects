import pytest

@pytest.fixture
def fixtureMethod():
    print("This is a fixture method")

def test_login_app(fixtureMethod):
    print("This is a login app method")
@pytest.mark.skip
def test_search_product(login_app):
    print("This is a search product functionality")

def test_addItemToCart(search_product):
    print("This is add item to cart functionality")
@pytest.mark.skip
def test_checkingAddItem(addItemToCart):
    print("This is checking items in cart functionality")
@pytest.mark.xfail
def test_paymentDetails(checkingAddItem):
    print("This is payment processing application")

def deliveryStatus(paymentDetails):
    print("This is delivery status functionality")

def removeItemFromCart(deliveryStatus):
    print("This is remove item from cart")

def logout():
    print("This is logout functionality")