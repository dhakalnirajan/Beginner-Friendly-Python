# Program to Convert Metre to Centimetre
# Creating a variable called 'm' to ask the user to input a measure of length in metre.

m = int(input("Enter a number of a certain length: "))
# creating a variable called 'cm' to convert the user value in metre to centimetre
cm = m * 100
# creating a variable called 'feet' for feet and 'inch' for inchesft = n
feet=int(input("Enter the length in feet: "))
inch = 12 * feet
# Printing the values
print("The length in centimetre is: ",round(cm,2))
print("The length in Inches is",round(inch,2))