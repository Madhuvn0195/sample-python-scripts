def name():
    return name

def age():
    return age

def diff():
    return 100-num

    
print("Welcome to age calculating app")

name1 = str(input("Please enter your name:"))

while True:
    try:
        num = int(input("Please enter your age: "))
        break  # Break the loop if the input is valid
    except ValueError:
        print("Invalid input. Please enter a valid number for age.") 

if num < 100:  # Check if age is less than 100
        print(f"You will reach 100 years in: {diff()}")
elif num > 100:
        print("You are already 100 years or older!")

    