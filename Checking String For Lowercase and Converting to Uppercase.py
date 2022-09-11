# Asking the user to input string in a variable called string.
str = input("Enter a string: ")
# Starting a Nested Loop.
for char in str:
    k = char.islower()
    # Checking whether the string has lowercase characters. If the string has lowercase characters, converting the all the lowercase characters to uppercase.
    if k == True:
        print(str.upper())
        break # Breaking the Condition for converting to uppercase.
# If the string has uppercase values, it displays a message.
if(k != 1):
    print('The string does not have any uppercase character. It only has the string called', str, 'and it is in uppercase.')