# Author: Caleb Moura

# Prompt user to input 3 numeric values
value1 = float(input("Enter the first numeric value: "))
value2 = float(input("Enter the second numeric value: "))
value3 = float(input("Enter the third numeric value: "))

# List of the 3 input values in the order provided by the user
values_list = [value1, value2, value3]

# Display of the original list
print("Original list:", values_list)

# Each value doubled and displayed in the the updated list
doubled_values = [int(value * 2) for value in values_list]
print("Doubled values:", doubled_values)