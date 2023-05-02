import time

import pytest
from AppiumFramework.base.DriverClass import Driver


@pytest.fixture(scope='class')
def class_fixture(request):
    print("Before Class")
    driver = Driver()
    driver = driver.getDriverMethod()
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    time.sleep(5)
    driver.quit()
    print("After Class")


@pytest.fixture()
def method_fixture():
    print("Method Starting")
    yield
    print("Method Ending")
