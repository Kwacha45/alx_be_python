from re import match

num1=float(input("Enter the first number:"))
num2=float(input("Enter the second number:"))
operation=(input("Choose the operation (+, -, *, /):"))
match(operation):
    case "+":
        addition=num1 + num2
        print("The result is:",addition)
    case "-":
        subtraction= num1-num2
        print("The result is:",subtraction)
    case "*":
        multiplication= num1*num2
        print("The result is :",multiplication)
    case "/":
        division=num1/num2
        print("The result is :",division)
    case _ :
        print("Cannot divide by zero!",division)