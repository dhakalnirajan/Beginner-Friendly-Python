# Creating variables for Principal (p), Time (t), Rate(r) and asking the user for the user-defined value.

p = float(input("Enter the Principal Amount: "))
t = float(input("Enter the time period: "))
r = float(input("Enter the rate of interest: "))

# Applying the formula of Compound Interest. Creating variable called ci for compound interest.
# formula for compound interest is ci = p * ((1+r/100)^t - 1), p = principal, t = time, r = rate
# In the code below, the function/complexity of time is raised to the power using in-built mathematics operator

ci = p * ((1 + r / 100)** t)
print(ci)
