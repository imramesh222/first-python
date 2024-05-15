# print("hello")
# num_char=len("hello")
# print(num_char)

#create or defining own function

# def my_function():
#   print("my_function")
#   print("hello")

# my_function()

# "Write a Python function called calculate_average that takes a list of numbers as input and returns the average (mean) of those numbers. Then, write a program that prompts the user to enter a list of numbers separated by spaces, calls the calculate_average function, and prints the resulting average."

def calculate_average(numbers):
    """
    Function to calculate the average of a list of numbers.
    
    Parameters:
        numbers (list of float): List of numbers to calculate the average from.
    
    Returns:
        float: The average of the numbers.
    """
    if len(numbers) == 0:
        return 0
    else:
        return sum(numbers) / len(numbers)

# Prompting the user for input
input_numbers = input("Enter a list of numbers separated by spaces: ")
numbers_list = [float(num) for num in input_numbers.split()]

# Calling the calculate_average function and printing the result
average = calculate_average(numbers_list)
print("The average of the numbers is:", average)