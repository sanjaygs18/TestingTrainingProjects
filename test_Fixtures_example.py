import pytest

@pytest.fixture
def fixtureMethod():
    print("This is a Fixture Method")

def test_SystemTesting(fixtureMethod):
    print("This is system testing")

def test_FunctionalTesting(fixtureMethod):
    print("This is functional Testing")

def test_Retesting(fixtureMethod):
    print("This is retesting")

def test_AlphaTesting(fixtureMethod):
    print("This is Alpha Testing")