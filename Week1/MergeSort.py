# coding=utf-8


def merge(list_1, list_2):
    # Initialize list counters and final list
    i = 0
    j = 0
    merged_list = []
    # Loop through the individually sorted lists, and
    # append the smallest of the smallest numbers to the final list
    # until one of the lists has been exhausted
    while (i < len(list_1)) & (j < len(list_2)):
        if list_1[i] < list_2[j]:
            merged_list.append(list_1[i])
            i += 1
        else:
            merged_list.append(list_2[j])
            j += 1
    # One of the 2 will be empty, so the order doesn't matter
    remaining_numbers = list_1[i:len(list_1)] + list_2[j:len(list_2)]
    merged_list = merged_list + remaining_numbers
    return merged_list


def sort(list_of_numbers):
    n_num = len(list_of_numbers)
    if n_num == 1:
        # Case 0 of the recursive function
        return list_of_numbers
    else:
        # Recursive iteration
        list_1 = sort(list_of_numbers[0:(n_num/2)])
        list_2 = sort(list_of_numbers[(n_num/2):n_num])
        list_of_numbers = merge(list_1, list_2)
        return list_of_numbers


if __name__ == '__main__':
    test_samples = [[3, 4, 2, 5, 8, 9, 1, 6, 0]]
    print("\n------------------------------------------------------------------------")
    print("------------------- Mergesort implementation results -------------------")
    print("------------------------------------------------------------------------")
    for test_sample in test_samples:
        print("Unsorted list: ")
        print(test_sample)
        print("Sorted list: ")
        print(sort(test_sample))