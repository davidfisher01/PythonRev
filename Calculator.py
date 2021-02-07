num1 = float(input("Enter the first #"))
op = float(input("Enter operator"))
num2 = float(input("Enter the second #"))
if op is "+" :
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op is "*":
    result = num1*num2
elif op == "/":
    result = num1/num2
else:
    print("invalid operator")

print(result)
