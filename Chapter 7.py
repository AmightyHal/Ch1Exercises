# chapter 7 hw
# algo workbench 8

# first we will create the variable list1
list1 = [1, 2, 3, 4, 5]
# next we will use list comprehension to create a new list containing squares of numbers in list1
# Using x**2 will calculate squares of each element x in list1
squared_list = [x**2 for x in list1]
# print the squared list for our results
print(squared_list)

#algo workbench 9
# first we will create the variable list1
list1 = [90, 110, 200, 150, 60, 84]
# next use list comprehension to create a new list containing elements greater than 100
greater_than_100 = [x for x in list1 if x > 100]
# print our list resulting in numbers greater than 100
print(greater_than_100)

# programing exercise 1
# first we will define a function to ask the user for sales per day to calculate weekly sales
def calc_weekly_sales():
    # we will need an empty list to store our daily sales in
    daily_sales = []
    # now we will prompt the user to enter sales for every day of the week
    for day in ['Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun']:
        # get sales amount for current day using user input
        sales = float(input(f"Enter sales for {day}: $"))
        # add sales amount to the list
        daily_sales.append(sales)
    # using the sum() function we will calculate total weekly sales
    total_sales = sum(daily_sales)
    # now we will display the total sales for the week making sure to only have 2 decimal places
    print(f"\nTotal sales for the week: ${total_sales:.2f}")
# now call the function to run the program
calc_weekly_sales()

# programming exercise 14
import matplotlib.pyplot as plt

file_path = 'C:\Users\Ethan Meeuwenberg\.ipynb_checkpoints\expenses.txt'

def read_expenses_file(file_path):
    # Initialize an empty dictionary to store expenses
    expenses = {}
    # Open the file and read expenses
    with open(file_path, 'r') as file:
        # Iterate through each line in the file
        for line in file:
            # Split the line into category and amount using a comma as a separator
            category, amount = line.strip().split(',')
            # Convert the amount to a float and store it in the dictionary
            expenses[category] = float(amount)
    # Return the dictionary containing expenses
    return expenses
def plot_pie_chart(expenses):
    # Extract data for plotting
    categories = list(expenses.keys())
    amounts = list(expenses.values())

    # Plotting the pie chart
    plt.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title('Expense Distribution')

    # Display the pie chart
    plt.show()
def main():
    # Specify the path to your expenses file
    file_path = 'expenses.txt'

    # Read expenses from the file
    expenses = read_expenses_file(file_path)

    # Plot a pie chart based on the expenses
    plot_pie_chart(expenses)
def main():
    # Specify the path to your expenses file
    file_path = 'expenses.txt'

    # Read expenses from the file
    expenses = read_expenses_file(file_path)

# Plot a pie chart based on the expenses
plot_pie_chart(expenses)

# programming exercise 8

file_path = 'C:\Users\Ethan Meeuwenberg\Desktop\BoyNames.txt'

def read_names_from_file(file_path):
    # Initialize an empty list to store names
    names = []

    # Open the file and read names
    with open(file_path, 'r') as file:
        # Iterate through each line in the file
        for line in file:
            # Append each name to the list after removing leading and trailing whitespaces
            names.append(line.strip())
     # Return the list containing names
    return names

def check_popularity(user_name, popular_names):
    # Check if the user-entered name is among the most popular names
    if user_name in popular_names:
        return f"{user_name} is among the most popular baby names!"
    else:
        return f"{user_name} is not among the most popular baby names."

def main():
    # Specify the path to the file containing popular baby names
    file_path = 'BoyNames.txt'

    # Read names from the file
    popular_names = read_names_from_file(file_path)

    # Get user input for a name
    user_input = input("Enter a name to check popularity: ")

    # Check and display the popularity of the entered name
    result_message = check_popularity(user_input, popular_names)
    print(result_message)

# Entry point of the program
if __name__ == "__main__":
    # Call the main function to execute the program
    main()

# programming exercise 4
def get_user_numbers():
    # Initialize an empty list to store user-entered numbers
    numbers = []

    # Prompt the user to enter 20 numbers
    for i in range(20):
        # Use try-except to handle invalid inputs (non-numeric)
        while True:
            try:
                # Get a number from the user
                num = float(input(f"Enter number {i+1}: "))
                # Add the number to the list
                numbers.append(num)
                break  # Break the loop if the input is valid
            except ValueError:
                # Display an error message for invalid inputs
                print("Invalid input. Please enter a valid number.")

    return numbers
def analyze_numbers(numbers):
    # Calculate the required statistics
    lowest_number = min(numbers)
    highest_number = max(numbers)
    total = sum(numbers)
    average = total / len(numbers)

    # Display the results
    print(f"\nLowest number: {lowest_number}")
    print(f"Highest number: {highest_number}")
    print(f"Total of the numbers: {total}")
    print(f"Average of the numbers: {average:.2f}")
def main():
    # Get 20 numbers from the user
    user_numbers = get_user_numbers()

    # Analyze and display the statistics
    analyze_numbers(user_numbers)

# Entry point of the program
if __name__ == "__main__":
    # Call the main function to execute the program
    main()
