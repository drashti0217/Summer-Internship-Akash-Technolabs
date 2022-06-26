# (1) No argument, No Return Type
def show():
    n1 = int(input("Enter a number n1 :- "))
    n2 = int(input("Enter a number n2 :- "))
    sum = n1+n2
    print("Sum is :- ",sum)
show()
"""
OUTPUT:-

Enter a number n1 :- 12
Enter a number n2 :- 54
Sum is :-  66

"""

# (2) Argument, return Type
def show1(n1,n2):
    sum = n1+n2
    return sum
sum = show1(100,200)
print("Sum is :- ",sum)      
"""
OUTPUT:-

Sum is :- 300

"""

# (3) Argument, No Return Type
def show2(n1,n2):
    sum = n1+n2
    print("Sum is :- ",sum)
show(10,20)
"""
OUTPUT:

Sum is :- 30

"""

# (4) No argument, Return type
def show3():
    n1 = int(input("Enter a number n1 :- "))
    n2 = int(input("Enter a number n2 :- "))
    sum = n1+n2
    return sum
sum = show3()
print("Sum is :- ",sum)
"""
OUTPUT:

Enter a number n1 :- 54
Enter a number n2 :- 11
Sum is :- 65

"""