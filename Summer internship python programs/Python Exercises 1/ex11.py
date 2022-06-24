# Take 2 numbers and find smallest number.

n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))

if n1 < n2:
    small = n1
else:
    small = n2

print("\nSmallest = %d" %(small))