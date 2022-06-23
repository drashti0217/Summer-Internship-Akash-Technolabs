a=10
print(a, "is of type", type(a))     #10 is of type <class 'int'>

b=20.5
print(b, "is of type", type(b))     #20.5 is of type <class 'float'>
print(b, "is complex number?", isinstance(20.5, int))
#20.5 is complex number? False

c=1+2j
print(c, "is of type", type(c))
#(1+2j) is of type <class 'complex'>
print(c, "is complex number?", isinstance(1+2j, complex))
#(1+2j) is complex number? True
