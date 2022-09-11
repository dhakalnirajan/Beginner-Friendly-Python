# Program to Find the Smallest Number Among Three Numbers.

# Creating three variables 'a', 'b', 'c', asking the values and storing three numbers separately in the variables.

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if (a < b) and (a < c):
   smallest = a
elif (b < a) and (b < c):
   smallest = b
else:
   smallest = c

print("The smallest number is: ", smallest)