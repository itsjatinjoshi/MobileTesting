
def f():
    yield True


try:
    g = f()
    h = next(g)
    assert h is True
    print("True")
    h = next(g)
    assert h in None
    print("None")
except AssertionError:
    print("Err")
except GeneratorExit:
    print("Exit")
except StopIteration:
    print("Stop")
