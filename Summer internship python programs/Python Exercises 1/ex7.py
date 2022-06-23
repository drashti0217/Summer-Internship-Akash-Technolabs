# Take a number and check whether it is zero, positive or negative.

num = float(input("Enter a number: "))
if num > 0:
   print(num , "is positive number")
elif num == 0:
   print(num , "is Zero")
else:
   print(num ," is a negative number")