# Take starting number and ending number from the user and print following series.

num = int(input("Enter starting number : "))

limit = int(input("Enter ending number : "))

for i in range(limit,0,-1):
    print(i*num) 