#******************************************************************************
#Common factors of two numbers, this are the numbers which divide both input 
#numbers. 
#*******************************************************************************/
count=0
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a<b:
	n=a
else:
	n=b;
for i in range(1,n+1):
	if a%i==0 and b%i==0:
			count=count+1;
print(count)