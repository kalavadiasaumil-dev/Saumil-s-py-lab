# Prompt the user to enter the first number of the Arithmetic Progression (AP) series and store it as an integer in variable 'x'
x = int(input("Enter the first number of your AP series: "))

# Prompt the user to enter the last number of the AP series and store it as an integer in variable 'a'
a = int(input("Enter the last number of your AP series: "))

# Prompt the user to enter the common difference between terms in the AP and store it as an integer in variable 'b'
b = int(input("Enter the common diffrence: "))

# Use a for loop to iterate over the AP series starting from 'x' up to and including 'a', with a step size of 'b'
for i in range(x, a + 1, b):
    # Print each term of the AP series
    print(i)