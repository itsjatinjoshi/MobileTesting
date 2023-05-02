import pytest


@pytest.mark.run(order=2)
def test_methodA():
    print("This is Method A.")


@pytest.mark.run(order=4)
def test_methodB():
    print("This is Method B.")


@pytest.mark.run(order=1)
def test_methodC():
    print("This is Method C.")


@pytest.mark.run(order=3)
def test_methodD():
    print("This is Method D.")
