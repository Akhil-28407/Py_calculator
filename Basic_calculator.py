num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
operator = input("Enter the operation: ")

if operator == "+":
    print(num1+num2)
elif operator == "-":
    print(num1-num2)
elif operator == "/":
    print(num1/num2)
elif operator == "*":
    print(num1*num2)
else:
    print("You have entered invalid operator !! Please check the operator")
