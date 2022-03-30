import time

def speed_calc_decorator(function):
    def inner():
        starting_time = time.time()
        function()
        end_time = time.time()
        print(f"{function.__name__} run speed: {end_time - starting_time}")
    return inner 

@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i

@speed_calc_decorator        
def slow_function():
    for i in range(100000000):
        i * i

fast_function()
slow_function()

# Create the logging_decorator() function 👇

def logging_decorator(function):
    def inner(*args):
        returned = function(*args)
        print(f"You called {function.__name__}{args}\n It returned: {returned}")
    return inner



# Use the decorator 👇
@logging_decorator
def a_function(*args):
    result = 1
    for num in args:
        result *= num
    return result

a_function(1, 2, 3)
a_function(4, 5, 6)
a_function(4, 5, 6, 2, 3, 4, 2)