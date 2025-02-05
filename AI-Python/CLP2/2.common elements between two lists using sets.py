def common_elements(list1, list2):
    # Convert both lists to sets
    set1 = set(list1)
    set2 = set(list2)
    # Find the intersection of both sets
    common_set = set1.intersection(set2)
    # Convert the set back to a list
    common_list = list(common_set)
    return common_list

# Example usage
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
print(common_elements(list1, list2))