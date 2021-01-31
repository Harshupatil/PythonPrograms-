#******************************************************************************
#Armstrong Number, is the number that is equal to sum of cube of it's degits.
#For example 0, 1, 153, 370, 371, 407 are armstrong numbers.
#*******************************************************************************/

def armstrong():
    sum=0;
    n=int(input("Enter the number: "))
    n1=n;
    while(n1!=0):
        d = n1%10;
        n1 = int(n1/10);
        sum = sum + d*d*d;
    if sum==n:
        print("Number is Armstrong number")
        
    else:
        print("Number is not Armstrong number")
        print(sum)

armstrong()
