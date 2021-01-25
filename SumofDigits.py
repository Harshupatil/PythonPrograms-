#******************************************************************************
#We can find sum of digits of number, using loops and mathematical operators.
#*******************************************************************************/

sum=0
n=int(input("Enter the number: "))
n1 = n
while (n1!=0):
    d = n1%10
    n1 = int(n1/10)
    sum = sum + d
print("Sum of digit: {0}".format(sum))
 
