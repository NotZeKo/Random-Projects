import art

def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide,
}


def calculator():
    print(art.logo)
    number1 = float(input("What's the first number?: "))
    while True:
        op = input("+\n-\n*\n/\nPick an operation: ")
        number2 = float(input("What's the next number?: "))
        value = (operations[op](number1, number2))
        print(f"{number1} {op} {number2} = {value}")
        conti = input(f"Type 'y' to continue calculating with {value}, or 'n' to start a new calculation: ")
        if conti.lower() == "y":
            number1 = value
        else:
            break


go = True
while go == True:
    calculator()



