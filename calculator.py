logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def add(n1, n2):
    return n1 + n2
def substract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : substract,
    "*" : multiply,
    "/" : divide,
}

def get_operation():
    while True:
        symbol = input("Pick an operation: ")
        for operation in operations:
            if operation == symbol:
                return symbol
        print("Incorrect operation selected.")

def get_num(message):
    while True:
        num = input(message)
        try:
            num = int(num)
            return num
        except:
            try:
                num = float(num)
                return num
            except:
                print("Incorrect input, select a number.")
            print("Incorrect input, select a number.")


def calculator():
    num1 = get_num("What's the first number? ")
    for operation in operations:
        print(operation)
    should_continue = True
    while should_continue:
        operation_symbol = get_operation()
        num2 = get_num("What's the next number? ")
        result = round(operations[operation_symbol](num1, num2), 2)
        print(f"{num1} {operation_symbol} {num2} = {result}")
        num1 = result
        user_input = input(f"Type \'y\' to continue calculating with {result}, \'n\' to start a new calculation or type \'exit\' to exit the program: ")
        if user_input == 'y' or user_input == 'yes':
            should_continue = True
        elif user_input == 'n' or user_input == 'new':
            calculator()
        else:
            should_continue = False

print(logo)
calculator()