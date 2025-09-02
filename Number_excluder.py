
n=int(input("Enter till how much do you want to have your Range: "))
#asks the user the range from 1 to n+1 (in python way)

Universal=set(range(1,n+1)) 
#genrates the universal set according to value of n


b=set(map(int, input("Enter the numbers you want to exclude (comma separated with no spaces):  ").split(","))) 
#first the b is defined as set , 
#map makes the values in set
#int makes string to integer value
#split makes the input values divided in seperate  #parts and further for the calculation

print(sorted(Universal-b))
#prints the difference of the universal set and set b
