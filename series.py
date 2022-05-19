
#fibbonacci sequence 0,1,1,2,3,5,8,13....
#get nth number (where it is located in the sequence)
#Lucas Numbers 2,1,3,4,7,11,18...

#def the fib function 
def fibonacci(n):
    ''' fibbonacci sequence 0,1,1,2,3,5,8,13....
    nth = location in the sequence, not the value but the values location. starts the sequence always with 0 and 1 '''
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
 
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def lucas(n):
    ''' fibbonacci sequence 2,1,3,4,7,11,18...
    nth = location in the sequence, not the value but the values location. similar to fibbonacci but starts with 2 and 1 '''
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)

#initial pass and fail tests
def failing(n):
    return n

def passing(n):
    return n

