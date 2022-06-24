# Write a program to swap 2 numbers without taking third variable.

n1 = int(input("\nEnter a number n1 :- "))
n2 = int(input("Enter a number n2 :- "))
 
print ("\nBefore swapping: ")
print("Value of n1 : ", n1)
print("Value of n2 : ", n2)
 
# Swap code
n1 = n1 + n2
n2 = n1 - n2 
n1 = n1 - n2 
 
print ("\nAfter swapping: ")
print("Value of n1 : ", n1)
print("Value of n2 : ", n2)