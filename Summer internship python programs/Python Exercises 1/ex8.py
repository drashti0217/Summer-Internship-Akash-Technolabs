# Take 2 numbers and display greatest number. (Also check equal number condition)

num1 = int(input("Enter first number: "))      
num2 = int(input("Enter second number: ")) 
#Compare both the number 
if num1 >= num2:   
    if num1 == num2:    
         print(num1 ,"and", num2 , "both are equal numbers.")       
    else:  
         print(num1, "is greatest number.")
else:   
    print(num2, "is greatest number.") 