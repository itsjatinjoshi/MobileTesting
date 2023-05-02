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


def test_methodE(class_fixture, method_fixture):
    print("Method E started")


def test_methodF(class_fixture, method_fixture):
    print("Method F started")
