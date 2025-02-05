numbers = [4, 2, 5, 1, 2, 4, 3, 5]

def remove_duplicates_and_sort(numbers):
    unique_numbers = set(numbers)
    sorted_numbers = sorted(unique_numbers)
    return sorted_numbers

print(remove_duplicates_and_sort(numbers))