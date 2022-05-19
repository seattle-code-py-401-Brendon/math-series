import pytest
import series



#get a initial failing test
def test_initial_fail():
    one = True
    two = False
    assert series.failing(one) == True
#get a initial passing test
def test_initial_pass():
    one = True
    two = False
    assert series.passing(two) != True


#Fibbonacci tests
def test_fibbonacci_0():
    fibbNum = 0
    assert series.fibonacci(fibbNum) == 0

def test_fibonacci_pass():
    fibbNum = 5
    assert series.fibonacci(fibbNum) == 5

def test_fibonacci_fail():
    fibbNum = 5
    assert series.fibonacci(fibbNum) != 4

#Lucas tests

def test_lucas_0():
    lucaNum = 0
    assert series.lucas(lucaNum) == 2

def test_lucas_pass():
    lucaNum = 1
    assert series.lucas(lucaNum) == 1

def test_lucas_fail():
    lucaNum = 3
    assert series.lucas(lucaNum) != 3

def test_lucas_pass():
    lucaNum = 4
    assert series.lucas(lucaNum) == 7