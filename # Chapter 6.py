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
