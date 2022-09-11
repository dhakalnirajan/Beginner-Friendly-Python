# String With String Functions
# Replace Function in String
sense = "hello World"
newS = sense.replace('h','H') # replacing 'h' with 'H' using replace function in the variable s.
print(newS) # new string is created. sense = "hello World"
# Creating a variable called 'Site' to store a string called 'Ted Evelyn Mosby', another variable called 's' to store 'heLLo WoRlD'
site = "Theodore Evelyn Mosby"
s = "heLLo WoRlD"
# Capitalizing a string
# Convertss first letter of a sentence in a string.
s2 = s.capitalize()
print(s2)
# Uppercasing the String
# Converts all alphabetic characters to uppercase
s3 = s.upper()
print(s3)
# Lowercasing a string
# Converts all alphabetic characters to lowercase
site2 = site.lower()
print(site2)
# Titlecasing a string
# Titlecasing Converts the first letter of each word to uppercase and remaining letters to lowercase
s4 = s.title()
print(s4)
# Swapcasing a String
# Swaps case of all alphabetic characters.
s5 = s.swapcase()
print(s5)
# iterate the first 8 characters of the string using slice operator

for char in site[0:8]:
    print(char)

# iterate the string in reversed order using slice operator
for char in site[::-1]:
    print(char)