import pytest
from series import (
    fibonacci,
    lucas
)


#Fibbonacci tests
def test_fibbonacci_0():
    fibbNum = 0
    assert fibonacci(fibbNum) == 0

def test_fibonacci_pass():
    fibbNum = 5
    assert fibonacci(fibbNum) == 5

def test_fibonacci_fail():
    fibbNum = 5
    assert fibonacci(fibbNum) != 4

#Lucas tests

def test_lucas_0():
    lucaNum = 0
    assert lucas(lucaNum) == 2

def test_lucas_pass():
    lucaNum = 1
    assert lucas(lucaNum) == 1

def test_lucas_fail():
    lucaNum = 3
    assert lucas(lucaNum) != 3

def test_lucas_pass():
    lucaNum = 4
    assert lucas(lucaNum) == 7