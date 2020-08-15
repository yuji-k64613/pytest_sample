import pytest
import logging
import os
import main
import sub1.client1 as cli1
import sub2.client2 as cli2


@pytest.mark.slow
def test_func():
    hello = main.func("foo")
    assert hello == "hello foo"


@pytest.mark.parametrize(
    "x, y, z", [(1, 2, 3), (3, 4, 7), (5, 6, 11),],
)
def test_func_with_param(x, y, z):
    a = cli1.func1(x, y)
    assert a == z


# Fixtures
def test_func_with_param(numbers):
    x = numbers[0]
    y = numbers[1]
    z = numbers[2]

    a = cli1.func1(x, y)
    assert a == z


# Fixtures
def test_func_autouse():
    shell = os.environ.get("PYENV_SHELL")
    assert shell == "sh"


# Mock
def test_mock(mocker):
    mocker.patch("sub1.client1.func1", return_value=10)
    assert cli1.func1() == 10

    mocker.patch("main.func", return_value="XXX")
    hello = main.func("foo")
    assert hello == "XXX"
