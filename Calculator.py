def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b != 0:
        return a/b
    else:
        return "Division by 0 is not allowed"
    
print("Welcome to calculator app")
print("Choose an operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter your choice (1/2/3/4):")

num1 = float(input("Enter your first number:"))
num2 = float(input("Enter your second number:"))
if choice == '1':
    print(f"The result is: {add(num1, num2)}")
elif choice == '2':
    print(f"The result is: {subtract(num1, num2)}")
elif choice == '3':
    print("The result is:" + str(multiply(num1, num2)))
elif choice == '4':
    print(f"The result is: {divide(num1, num2)}")
else:
    print("Invalid input")
    