
a= float(input("first number:"))
operator = input("Enter operator:")
b = float(input("second number: "))
operator = input("Enter operator:")
c = float(input("third number: "))


if operator == "+":

    sum = a + b + c
    print(sum)
elif operator == "-":
    difference = a - b - c
    print(difference)
elif operator == "*":
    product = a * b * c
    print(product)
elif operator == "/":
    quotient = a / b / c
    print(quotient)
else:
    print("Invalid operation")
    