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

def read_expenses_file(file_path):
    # Initialize an empty dictionary to store expenses
    expenses = {}