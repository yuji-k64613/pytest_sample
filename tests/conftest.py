import pytest
import os
import sys

sys.path.append(
    os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + "/../src/")
)


@pytest.fixture(scope="session", autouse=True)
def my_session():
    prev = os.environ.get("PYENV_SHELL")
    os.environ["PYENV_SHELL"] = "sh"
    yield
    if prev:
        os.environ["PYENV_SHELL"] = prev


@pytest.fixture
def numbers():
    return (1, 2, 3)
