# Python Program For Menu-based Calculator Depending on the Operator of User Choice.
# Defining the functions of various operators
# Addition function
def add(a , b):
    sum = a + b
    print(a,"+",b,"=",sum)

# Subtraction Function
def subtract(a , b):
    difference = a - b
    print(a,"-",b,"=",subtract)

# Multiplication Function
def multiply(a , b):
    product = a * b
    print(a,"*",b,"=",product)

# Division Function
def divide(a , b):
    division = a / b
    print(a,"/",b,"=",division)

# Creating the Heading
print("WELCOME TO THE MENU BASED CALCULATOR")

# Using the While loop to print the menu list
while True:
    print("\nMENU")
    print("1. Sum of Two Numbers")
    print("2. Difference Between Two Numbers")
    print("3. Product of Two Numbers")
    print("4. Division of Two Numbers")
    print("5. Exit")

    choice = int(input("\nEnter the Choice: "))
    
   # Using the While loop to print the menu list
while True:
    print("\nMENU")
    print("1. Sum of Two Numbers")
    print("2. Difference Between Two Numbers")
    print("3. Product of Two Numbers")
    print("4. Division of Two Numbers")
    print("5. Exit")

    choice = int(input("\nEnter the Choice: "))
    # Using If-elif-else Conditions To Call The Different Relavant Functions Based on the User Choice.
    if choice == 1:
        print("\nADDITION\n")
        
        a = int(input("First Number: "))
        b = int(input("second Number: "))
        add(a,b)

    elif choice == 2:
        print("\nSUBTRACTION\n")
        
        a = int(input("First Number: "))
        b = int(input("second Number: "))
        subtract(a,b)

    elif choice == 3:
        print("\nMULTIPLICATION")
        
        a = int(input("first Number: "))
        b = int(input("second Number: "))
        multiply(a,b)

    elif choice == 4:
        print("\nDIVISION")
        
        a = int(input("first Number: "))
        b = int(input("second Number: "))
        divide(a,b)

# Exiting the while loop
    elif choice == 5:
        print("Thank You! Check Out Other Menu Options Or Exit The Program.")
        
        break

    else:
        print("Please Provide a Valid Input!")