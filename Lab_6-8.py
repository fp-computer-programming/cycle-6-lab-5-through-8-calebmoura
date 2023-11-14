# Author: Caleb Moura

# Prompt input from the user
num1 = float(input("Enter the first numeric value: "))
num2 = float(input("Enter the second numeric value: "))
num3 = float(input("Enter the third numeric value: "))

# List with the user-input values
numbers_list = [num1, num2, num3]

# Checking if all numbers in the list are even
if all(num % 2 == 0 for num in numbers_list):
    print("even")

# Checking if all numbers in the list are odd
elif all(num % 2 != 0 for num in numbers_list):
    print("odd")

# Neither all even nor all odd = mixed list
else:
    print("mixed")