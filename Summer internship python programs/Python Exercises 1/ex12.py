""" 
Take a number check if a number is less than 100 or not. If it is less than 100 then check if it is odd or
even.
"""

num = int(input("Enter a number : "))
if num < 100 :
    print(num , "number is less than 100.")
    if (num % 2) == 0:
        print(num , "is even number.")
    else:
        print(num , "is odd number.")
else:
    print(num , "number is not less than 100")
