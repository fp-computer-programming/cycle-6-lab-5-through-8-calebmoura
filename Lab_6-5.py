# Author: Caleb Moura

# Defining the function that takes a list of numbers as input
def find_highest_and_lowest(numbers):
    # Check if the list has at least 2 unique numbers
    unique_numbers = set(numbers)
    if len(unique_numbers) < 2:
        return "error: list does not meet specifications"

    # Find highest and lowest values in list
    highest = max(numbers)
    lowest = min(numbers)

    # Return the results
    return highest, lowest


# Example usage of the function
if __name__ == "__main__":
    # Testing with lists
    list1 = [3, 1, 7, 4, 2, 5]
    result1 = find_highest_and_lowest(list1)
    print(f"List: {list1}, Result: {result1}")

    list2 = [5, 5, 5, 5, 5]
    result2 = find_highest_and_lowest(list2)
    print(f"List: {list2}, Result: {result2}")

    list3 = [8, 8, 1, 2, 3, 4]
    result3 = find_highest_and_lowest(list3)
    print(f"List: {list3}, Result: {result3}")