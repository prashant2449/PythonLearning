import pytest


@pytest.mark.login
def test_login():
    a = 3
    b = 3
    assert a == b
    print("test_login")


def test_checkout():
    p = 7
    q = 7
    assert p == q
    print("test_checkout")

