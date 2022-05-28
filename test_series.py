import pytest
from series import (
    fibonacci,
    lucas,
    sum_series
)


#Fibbonacci tests
# @pytest.mark.skip("fibb test (1)")
def test_fibbonacci_of_two():
    fibb_num = 2
    actual = fibonacci(fibb_num)
    expected = 1
    assert actual == expected

# @pytest.mark.skip("fibb test (2)")
def test_fibonacci_no_value():
    actual = fibonacci()
    expected = 'Please enter an index/number'
    assert actual == expected
    
#Lucas tests
# @pytest.mark.skip("Lucas test (1)")
def test_lucas_of_two():
    luca_num = 2
    actual = lucas(luca_num)
    expected = 3
    assert actual == expected
    

# @pytest.mark.skip("Lucas test (2)")
def test_lucas_no_value():
    actual = lucas()
    expected = 'Please enter an index/number for lucas nums'
    assert actual == expected

# @pytest.mark.skip("sum series test (1)")
def test_sum_series_fibonacci():
    fibb_num = 2
    parameter_one = 0
    parameter_two = 1
    actual = sum_series(fibb_num,parameter_one,parameter_two)
    expected = 1
    assert actual == expected

# @pytest.mark.skip("sum series test (2)")
def test_default_fibonacci_return():
    nth_num = 5
    actual = sum_series(nth_num)
    expected = 5
    assert actual == expected

    
# @pytest.mark.skip("sum series test (3)")
def test_sum_series_lucas():
    luca_num = 3
    parameter_one = 2
    parameter_two = 1
    actual = sum_series(luca_num,parameter_one,parameter_two)
    expected = 4
    assert actual == expected