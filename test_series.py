import pytest
from series import (
    fibonacci,
    lucas
)


#Fibbonacci tests
def test_fibbonacci_of_two():
    fibb_num = 2
    actual = fibonacci(fibb_num)
    expected = 1
    assert actual == expected

# @pytest.mark.skip("todo")
def test_fibonacci_no_value():
    actual = fibonacci()
    expected = 'Please enter an index/number'
    assert actual == expected
    
#Lucas tests

# @pytest.mark.skip("todo")
def test_lucas_of_two():
    luca_num = 2
    actual = lucas(luca_num)
    expected = 3
    assert actual == expected
    

# @pytest.mark.skip("todo")
def test_lucas_no_value():
    actual = lucas()
    expected = 'Please enter an index/number for lucas nums'
    assert actual == expected

@pytest.mark.skip("todo")
def test_sum_series_fibonacci():
    fibb_num
    

@pytest.mark.skip("todo")
def test_sum_series_lucas():
    pass
    