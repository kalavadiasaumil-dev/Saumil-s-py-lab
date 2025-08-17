def fac(n):#defining a function 
	
	
	if(n==0 or n==1):
		return 1					 
	else:
		b=n*fac(n-1)       #logic setting , if n is 3 then 3 * fac(2) which is 2*fac(1) hence fac 1 is 1 then the interpreter will eventually do 3*2*1   .
		return(b)
n=int(input("Enter the number whose factorial you want: "))
print(fac(n))