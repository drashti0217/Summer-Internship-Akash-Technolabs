# Take a number and check whether it is zero, positive or negative using nested IF...ELSE statement.

num = int(input("\nEnter a number: "))
# Checking the number
if num > 0:
    print(num , "number is positive.")
elif num == 0:
    print(num , "number is zero.")
else:
    print(num , "number is negative.")