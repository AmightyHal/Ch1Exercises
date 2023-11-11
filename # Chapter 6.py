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

# ex 6
# Function to calculate the average of numbers in a file
def average_of_numbers_in_file(file_name):
    try:
        # Open the file in read mode ('r')
        with open(file_name, 'r') as f:
            # Read the numbers from the file, split them, and convert to integers
            numbers = [int(num) for num in f.read().split()]

            # Calculate the sum of numbers
            sum_of_numbers = sum(numbers)

            # Calculate the average of numbers
            avg_of_numbers = sum_of_numbers / len(numbers)

            # Return the calculated average
            return avg_of_numbers
    except FileNotFoundError:
        # Handle the case where the file is not found
        print(f"The file: {file_name} was not found.")
    except Exception as e:
        # Handle other exceptions and print an error message
        print(f"An error occurred: {str(e)}")

# Calculate the average from the file
average = average_of_numbers_in_file("numbers.txt")

# Check if the average is calculated successfully before printing
if average is not None:
    # Print the calculated average
    print(f"The average of all numbers in the file is: {average}")

# ex 9
# Function to calculate the average of numbers in a file
def average_of_numbers_in_file(file_name):
    try:
        # Open the file in read mode ('r')
        with open(file_name, 'r') as f:
            # Read the numbers from the file, split them, and convert to integers
            numbers = [int(num) for num in f.read().split()]

            # Calculate the sum of numbers
            sum_of_numbers = sum(numbers)

            # Calculate the average of numbers
            avg_of_numbers = sum_of_numbers / len(numbers)

            # Return the calculated average
            return avg_of_numbers

    except FileNotFoundError:
        # Handle the case where the file is not found
        print(f"The file: {file_name} was not found.")

    except ValueError:
        # Handle the case where items from the file cannot be converted to a number
        print(f"Error: Cannot convert items from the file to a number.")

    except Exception as e:
        # Handle other exceptions and print an error message
        print(f"An error occurred: {str(e)}")

# Calculate the average from the file
average = average_of_numbers_in_file("numbers.txt")

# Check if the average is calculated successfully before printing
if average is not None:
    # Print the calculated average
    print(f"The average of all numbers in the file is: {average}")

# ex 12
# Function to calculate and display average steps for each month
def calculate_monthly_averages(filename):
    try:
        # Open the file in read mode ('r')
        with open(filename, 'r') as file:
            # Read all lines from the file
            lines = file.readlines()

            # Initialize lists to store monthly totals and counts
            monthly_totals = [0] * 12  # Assuming 12 months in a year
            monthly_counts = [0] * 12

            # Iterate through each line and update monthly totals and counts
            for day, line in enumerate(lines, start=1):
                # Extract the number of steps for the day
                steps = int(line)

                # Determine the month based on the day
                month = (day - 1) // 30  # Assuming an average of 30 days per month

                # Update monthly totals and counts
                monthly_totals[month] += steps
                monthly_counts[month] += 1

            # Calculate and display the average steps for each month
            for month, total, count in zip(range(1, 13), monthly_totals, monthly_counts):
                if count > 0:
                    average_steps = total / count
                    print(f"Month {month}: Average steps = {average_steps:.2f}")
                else:
                    print(f"Month {month}: No data available")

    except FileNotFoundError:
        # Handle the case where the file is not found
        print(f"The file {filename} was not found.")
    except ValueError:
        # Handle the case where steps data cannot be converted to an integer
        print("Error: Unable to convert steps to an integer.")
    except Exception as e:
        # Handle other exceptions and print an error message
        print(f"An error occurred: {str(e)}")

# Specify the filename to read from
input_filename = 'steps_data.txt'  # Change this to your actual filename

# Call the function to calculate and display monthly averages
calculate_monthly_averages(input_filename)
