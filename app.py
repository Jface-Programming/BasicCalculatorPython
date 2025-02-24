while True:
    result = 0;
    num1 = input("enter your first number")
    num2 = input("enter your second number")
    operator = input("enter an operation")
    if operator == "+":
        result = int(num1) + int(num2)
        print(result)
    if operator == "-":
        result = int(num1) - int(num2)
        print(result)
    if operator == "*":
        result = int(num1) * int(num2)
        print(result)
    if operator == "/":
        result = int(num1) / int(num2)
        print(result)