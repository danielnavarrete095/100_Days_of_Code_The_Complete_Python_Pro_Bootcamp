def func(*args):
    for i, arg in enumerate(args):
        print(f"args[{i}]: {arg}")

func("Hello", "world", 1, 2, 3, [1, 2, 3], {"1": 1, "2": 2, "3": 3})

def add(*args):
    return sum(args)

print(add(1, 2, 3))
print(add(4, 23, 23, 45, 56, 24, 132))

# Key Word Arguments
def calculate(n, **kwargs):
    result=[]
    print(kwargs)
    for (key, value) in kwargs.items():
        if key == "add":
            result.append(n + value)
        elif key == "multiply":
            result.append(n * value)
        elif key == "divide":
            result.append(n / value)
        else:
            print(f"Operation: {key} not supported!")

    # result.append(n + kwargs["add"])
    # result.append(n * kwargs["multiply"])
    # result.append(n * kwargs["divide"])
    return result

print(calculate(2, add = 3, multiply = 5, divide = 2, substract=1))
print(calculate(2, add = 3, multiply = 5))

class Car:
    def __init__(self, **kwargs):
        # This will raise an exception if key not in the dict
        # self.make = kwargs["make"]
        # self.model = kwargs["model"]
        # This is a better alternative, get() returns None if key not found!
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")

car = Car(make="Nissan", model="GT-R")
car1 = Car(model="A3")
print(car.make)
print(car.model)
print(car1.make)
print(car1.model)