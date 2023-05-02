import pytest


@pytest.fixture(scope='module')
def class_fixture():
    print("Class Starting")
    yield
    print("Class Ending")


@pytest.fixture()
def method_fixture():
    print("Method Starting")
    yield
    print("Method Ending")
