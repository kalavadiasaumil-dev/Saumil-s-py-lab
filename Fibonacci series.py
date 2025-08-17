def fibonacci(n):
	
	if n==0 or n==1:
		if(n==0):
			return [0]
		elif(n==1):
			return[0,1]
	seq= fibonacci(n-1)		#logic setting , if user enters 3 the interpreter will go to this line and calculate the recursion of the code and finally it will give output [0,1,1,2]
	seq.append(seq[-1]+seq[-2])
		
	return seq


n=int(input("Enter the number of terms of your fibonacci sequence:  "))
print(fibonacci(n))

#the value type will be list because base cases are in list