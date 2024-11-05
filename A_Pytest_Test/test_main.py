import main
import pytest

def test_function_nothing():
    assert main.do_nothing("x","y") == None