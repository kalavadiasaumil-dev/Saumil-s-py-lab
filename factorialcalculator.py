while True:
	
	def fac(n):#defining a function 
		try:
	
	
			if(n==0 or n==1):
				return 1					#logic setting , if n is 3 then 3 * fac(2) which is 2*fac(1) hence fac 1 is 1 then the interpreter will eventually do 3*2*1   . 
			else:
				b=n*fac(n-1)
				return(b)
		except:
			print("Invalid input!!!!")
	
	try:
		
		n=int(input("Enter the number whose factorial you want: "))
		print(fac(n))
	except:
		print("Invalid input!!")
	
	q=input("Do you want to continue?(y/n): ").lower()
	if q=="n":
		break