# Chapter 8
# Algo Workbench 1
if choice == 'Y' or choice == 'y':
# To rewrite this statement we will use the choice.lower() function so we only have to check for the lowercase value
if choice.lower() == 'y':

# Algo Workbench 2
# Define my_string with a sample statement that includes spaces to count
my_string = "Hello there are spaces here to count :D."

# Define a variable to count the spaces
space_count = 0

# Now we will go through each character in the string
for char in my_string:
    # Check current character to see if it's a space
    if char == ' ':
        # If a space is found add 1 to the space_count variable
        space_count += 1

# Print final count of space characters
print("Number of spaces:", space_count)

# Programming Exercise 1
# First we will ask for the user to input their full name
full_name = input("Enter your full name: ")

# Now we must split the name using the split() function and add them to a new variable
names = full_name.split()

# Now we will extract the initals by pulling the first character, 0, and add a "." after each letter
