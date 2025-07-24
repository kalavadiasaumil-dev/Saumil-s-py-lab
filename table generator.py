# Prompt the user to input the number for which they want the multiplication table
a = int(input("Enter whose table you want: "))

# Prompt the user to input the range (till what number they want the table)
b = int(input("Till which number ?: "))

# Start a loop from 1 to b (inclusive) to generate the multiplication table
for i in range(1, b+1):
    
    # Print the current multiplication result in the format: a × i = result
    print(a, " × ", i , "=", a*i)
    
    # Check if the current number is the last in the range, then break the loop (though this is redundant)
    if(i == b):
        break
