# Chapter 6
# Algorithim Workbench
# problem 1
# Function to write my name to a file
def write_name_to_file(filename, name):
    try:
        # Open the file in write mode
        with open(filename, 'w') as file:
            # Write the provided name to the file
            file.write(name)
        # Print a success message
        print(f"Wrote {name} to {filename}")
    except Exception as e:
        # If an error occurs, print an error message
        print(f"Error: {e}")
# Define output filename
output_filename = 'myname.txt'
# Define the name to be written to the file
my_name = 'Ethan Meeuwenberg'
# Call the function to write the name to the file
write_name_to_file(output_filename, my_name)

# problem 2
# Function to read the file
def read_name_from_file(filename):
    try:
        # Open the file in read mode ('r')
        with open(filename, 'r') as file:
            # Read the content (name) from the file
            name = file.read()
            # Display the name on the screen
            print(f"Read the name from {filename}: {name}")
    except Exception as e:
        # If an error occurs, print an error message
        print(f"Error: {e}")

# Specify the filename to read from
input_filename = 'myname.txt'

# Call the function to read the name from the file and display it
read_name_from_file(input_filename)

# programming excercises
# ex 1
# Function to display numbers from the file
def display_numbers_from_file(filename):
    try:
        # Open the file in read mode ('r')
        with open(filename, 'r') as file:
            # Read all lines from the file
            lines = file.readlines()

            # Iterate through each line and display the numbers
            for line in lines:
                # Split the line into individual numbers
                numbers = line.split()

                # Display each number on the screen
                for number in numbers:
                    print(number)

    except Exception as e:
        # If an error occurs, print an error message
        print(f"Error: {e}")

# Define the filename to read from
input_filename = 'numbers.txt'  # Change this to your actual filename

# Call the function to display all numbers from the file
display_numbers_from_file(input_filename)

