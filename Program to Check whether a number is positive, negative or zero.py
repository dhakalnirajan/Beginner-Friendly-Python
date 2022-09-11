# Program to check whether a user-given number is positive, negative or zero.
# Creating a variable to ask the user to input a number and store the number in the variable.

n = int(input("Enter any number whether positive, negative or zero."))

# A number line is drawn.
#   -5  -4  -3  -2  -1             0           +1  +2  +3  +4  +5
# ______N_E_G_A_T_I_V_E_________Z_E_R_O_______P_O_S_I_T_I_V_E_________
# The numbers towards the left of 0 are negative, the numbers towards the right are positive, the marginal number, 0 is, well, 0 'Zero'.
# Applying the conditions:
if n > 0:
    print('The number,',n,', is positive!')
elif n< 0:
    print('The number,',n,', is negative!')
else:
    print('The number is Zero!')