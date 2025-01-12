import pytest

@pytest.mark.profile
def test_SmokeTesting():
    print("This is Smoke Testing")

@pytest.mark.profile
def test_SanityTesting():
    print("This is Sanity Testing")

def test_UnitTesting():
    print("This is Unit Testing")

def test_RegressionTesting():
    print("This is Regression Testing")