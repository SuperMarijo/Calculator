a = int(input("Enter the first number of the operation "))

b = int(input("Now enter the second number of the operation "))

operation = input("To finish it, pick the operation you wish to perform ('+', '-', '*' or '/') ")

if operation == "+":
    print(a+b)
elif operation == "-":
    print(a-b)
elif operation == "*":
    print(a*b)
elif operation == "/":
    print(a/b)