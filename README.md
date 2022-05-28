# Lab 02 Modules, Containers, and Testing

### Author: Brendon H
-------
### Links and Resources
-------
### Setup
-------
### How to initialize/run your application (where applicable)
* python series.py (check console)
-------
### How to use your library (where applicable)
-------
### Tests
* To run tests, start virtual env then run pytest. 
* *The tests that I failed are actually passed based on receving the wrong expected output. example: _3 != 4 == passes the test_* __<<---this is old and outdated__

there are 7 tests in total
>fibonacci 
- (1)test_fibbonacci_of_two(n)
- (2)test_fibonacci_no_value( )
>lucas 
- (1)test_lucas_of_two(n)
- (2)test_lucas_no_value( )
>sum series 
- (1)test_sum_series_fibonacci(n,p1,p2)
- (2)test_default_fibonacci_return(n)
- (3)test_sum_series_lucas(n,p1,p2)
-------

## Overview
The Fibonacci Series is a numeric series starting with the integers 0 and 1. In this series, the next integer is determined by summing the previous two. This gives us:

0, 1, 1, 2, 3, 5, 8, 13, ...
Note When asking for the nth number in series presume starting at zero.

fibonacci(0) == 0, fibonacci(1) == 1, fibonacci(2) == 1, etc.

The Lucas Numbers are a related series of integers that start with the values 2 and 1 rather than 0 and 1. The resulting series looks like this:

2, 1, 3, 4, 7, 11, 18, 29, ...
## Configuration
Create a local git repo with root folder named math-series.
Create new repository named math-series
Link your local and remote repositories.
Feature Tasks and Requirements
Create a module series.py.
Add a file test_series.py to your repository. As you work on the tasks below, use TDD practices. Write tests first, then implement code. Make small changes with many cycles of Red-Green-Refactor
This is not an overly long assignment, so take the time to do the testing right.

Create a function called fibonacci. The function should have one parameter n. The function should return the nth value in the fibonacci series. You may implement the function using recursion or iteration. If you are feeling particularly frisky, do both as separate functions.

Ensure that your function(s) has a well-formed docstring

In your series.py module, add a new function lucas that returns the nth value in the lucas numbers Again, you may use recursion or iteration, or both. Again, ensure that your function has a well-formed docstring.

Both the fibonacci series and the lucas numbers are based on an identical formula. Add a third function called sum_series with one required parameter and two optional parameters. The required parameter will determine which element in the series to print. The two optional parameters will have default values of 0 and 1 and will determine the first two values for the series to be produced.

Calling this function with no optional parameters will produce numbers from the fibonacci series. Calling it with the optional arguments 2 and 1 will produce values from the lucas numbers. Other values for the optional parameters will produce other series. Again, you may use recursion or iteration, or both. Again, ensure that your function has a well-formed docstring.

Add your series.py and test_series.py modules to your repository and commit frequently while working on your implementation. Include good commit messages that explain concisely both what you are doing and why.

## Implementation Notes
### User Acceptance Tests
Your test requirements for today are straight forward. Use Test Driven Development to verify correct behavior as you build.
Test all three functions.
## Submission Instructions
Refer to the the Lab Submission Instructions for the complete lab submission process and expectations