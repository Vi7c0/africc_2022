num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

operator = input("Enter an operator, + - / *: ")

if operator == "+":
    total = num1 + num2
    print("Answer is, ", total)

elif operator == "-":
    total = num1 - num2
    print("Answer is, ", total)

elif operator == "*":
    total = num1 * num2
    print("Answer is, ", total)

elif operator == "/":
    total = num1 / num2
    print("Answer is, ", total)


