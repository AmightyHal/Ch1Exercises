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
initials = [name[0].upper() + "." for name in names]

# now we will print the initials and add spaces with .join() method
print("Initials:", " ".join(initials))

# Programming Exercise 2
# First we will ask the user to enter a series of single-digit numbers with nothing seperating them
start_num = input("Enter a series of single digit numbers with nothing seperating them.")

# Define the variable for the sum
sum_num = 0

# Now go through each character in the input string
for char in start_num:
    # Make sure what we are looking at is a digit
    if char.isdigit():
        # add the digit to the sum
        sum_num += int(char)

# Now display the sum of the single digit numbers
print("Sum of single-digit numbers:", sum_num)

# Programming Exercise 3
# Ask for input of a date in the form mm/dd/yyyy
date_input = input("Enter a date in the format mm/dd/yyyy: ")

# Now seperate the date into month, day, and year
month, day, year = map(int, date_input.split('/'))

# Make a list including all month names
months = [
    "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"
]

# Print the date in the format we want
format_date = f"{months[month - 1]} {day}, {year}"
print("The formatted version of this date is: ", format_date)

# Programming Exercise 10
# Get a string from the user
user_input = input("Enter a string: ")

# Create a list to store character frequencies
char_freq = {}
