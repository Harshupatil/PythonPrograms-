#******************************************************************************
#Factorial of number is the product of all numbers from 1 to that number, it is 
#denoted as n!. For example
#3! = 1*2*3 = 6
#5! = 1*2*3*4*5 = 120
#*******************************************************************************

factorial=1
n = int(input("Enter the number: "))
for i in range(1,int(n+1)):
    factorial = int(factorial*i)
print("Factorial of {0} is {1}".format(n,factorial))

