#******************************************************************************
#We can reverse number using loops and operators.
#*******************************************************************************/

r=0
n=int(input("Enter the number: "))
while n!=0:
    d = n%10
    n = int(n/10)
    r = r*10 + d; 
print("Reverse of number: {0}".format(r))

