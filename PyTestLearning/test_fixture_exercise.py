import pytest


@pytest.fixture(scope='module')
def rule1():
    print("Always execute this first")
    print("Login SUCCESS")

    yield
    print("Always execute this last")
    print("Logout SUCCESS")


@pytest.mark.usefixtures("rule1")
def test_order_create():
    print("ORDER CREATED SUCCESS")
