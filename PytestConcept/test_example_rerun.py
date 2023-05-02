# Two way to run failure test
# first one "pytest --reruns 5 test_example_rerun.py"
# second, use fixture "@pytest.mark.flaky(reruns=5)"
# And,  if wants to add delay in between execution of rerun "pytest --reruns 5 --reruns-delay 1 test_example_rerun.py"
import pytest


def test_runA():
    print("Running A.")


def test_runB():
    a = 1
    b = 2
    assert a == b


@pytest.mark.flaky(reruns=5)
def test_runC():
    a = 4
    b = 2
    assert a == b
