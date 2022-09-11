# Program to calculate the grade of a student.
print("Enter the student details below:")

name = input("Enter the name of a student: ")
grade = int(input("Enter the class of the student"))
roll_no = int(input("Enter the roll number of the student"))

print("Enter the marks obtained by the student below for the following subjects:")
# Entering the marks for the subjects. The subjects include English, Nepali, Mathematics, Physics, Chemistry, Computer, Social Studies and Life Skills.
Eng = int(input())
Nep = int(input())
Math = int(input())
Phy = int(input())
Chem = int(input())
Comp = int(input())
Soc = int(input())
Lski = int(input())

# Adding the marks of all the subjects. Creating a variable called 'total' for summation of marks of subjects.
total = Eng+Nep+Math+Phy+Chem+Comp+Soc+Lski
# Creating a variable called 'avg' to calculate the average of total marks.
avg = total/8

# Processing The Output
print("Name: ", name)

print("Grade: ", grade)

print("Roll no: ", roll_no)

print("The marks obtained in the examination are: ")

print("English", Eng)
print("Nepali", Nep)
print("Mathematics", Math)
print("Physics", Phy)
print("Chemistry", Chem)
print("Computer", Comp)
print("Social Studies", Soc)
print("Life Skills", Lski)
print("The Total Marks Secured: ", total)

if avg>=91 and avg<=100:
    print("Your Grade is A+")
elif avg>=81 and avg<91:
    print("Your Grade is A")
elif avg>=71 and avg<81:
    print("Your Grade is B+")
elif avg>=61 and avg<71:
    print("Your Grade is B")
elif avg>=51 and avg<61:
    print("Your Grade is C+")
elif avg>=41 and avg<51:
    print("Your Grade is C")
elif avg>=33 and avg<41:
    print("Your Grade is D")
elif avg>=21 and avg<33:
    print("Your Grade is E+")
elif avg>=0 and avg<21:
    print("Your Grade is E")
else:
    print("Invalid Input!")