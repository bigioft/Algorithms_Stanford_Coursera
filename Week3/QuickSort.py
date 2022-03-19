# coding=utf-8
import random
n_comparisons = None


def quick_sort_v0(list_of_numbers, pivot_element="random", initialize_counter=True):
    # TODO: proper description of the function
    """

    :rtype: list
    """
    n_num = len(list_of_numbers)
    if n_num <= 1:
        # Case 0 of the recursive function
        return list_of_numbers
    # Count the computational cost of the comparison operations
    global n_comparisons
    if initialize_counter:
        n_comparisons = 0
    n_comparisons += n_num - 1
    print(n_comparisons)
    # Index of the pivot number (only works starting with 0)
    i = 0
    # Choose Pivot: Randomized
    if pivot_element == "random":
        initial_pivot_i = random.randint(0, n_num - 1)  # Random randint can yield also right-end number
    elif pivot_element == "first":
        initial_pivot_i = 0
    elif pivot_element == "last":
        initial_pivot_i = n_num - 1
    elif pivot_element == "median_of_3":
        if n_num == 2:
            return [min(list_of_numbers), max(list_of_numbers)]
        three_elements = list(map(list_of_numbers.__getitem__, [0, n_num / 2, n_num - 1]))
        initial_pivot_i = sorted(zip(three_elements, [0, n_num / 2, n_num - 1]))[1][1]
    else:
        raise ValueError("pivot_element only takes values in ('random', 'first', 'last', 'median_of_3'")
    list_of_numbers.insert(0, list_of_numbers.pop(initial_pivot_i))
    # Recursive iteration
    for k in range(1, n_num):
        if list_of_numbers[k] < list_of_numbers[i]:
            i += 1
            list_of_numbers.insert(0, list_of_numbers.pop(k))
    list_of_numbers = \
        quick_sort(list_of_numbers[0:i], pivot_element=pivot_element, initialize_counter=False) + \
        list_of_numbers[i:(i+1)] + \
        quick_sort(list_of_numbers[(i+1):n_num], pivot_element=pivot_element, initialize_counter=False)
    return list_of_numbers


def quick_sort(list_of_numbers, pivot_element="random", initialize_counter=True):
    # TODO: proper description of the function
    """

    :rtype: list
    """
    n_num = len(list_of_numbers)
    if n_num <= 1:
        # Case 0 of the recursive function
        return list_of_numbers
    # Count the computational cost of the comparison operations
    global n_comparisons
    if initialize_counter:
        n_comparisons = 0
    n_comparisons += n_num - 1
    # Index of the pivot number (only works starting with 0)
    i = 0
    # Choose Pivot: Randomized
    if pivot_element == "random":
        initial_pivot_i = random.randint(0, n_num - 1)  # Random randint can yield also right-end number
    elif pivot_element == "first":
        initial_pivot_i = 0
    elif pivot_element == "last":
        initial_pivot_i = n_num - 1
    elif pivot_element == "median_of_3":
        if n_num == 2:
            return [min(list_of_numbers), max(list_of_numbers)]
        three_elements = list(map(list_of_numbers.__getitem__, [0, (n_num - 1) / 2, n_num - 1]))
        initial_pivot_i = sorted(zip(three_elements, [0, (n_num - 1) / 2, n_num - 1]))[1][1]
    else:
        raise ValueError("pivot_element only takes values in ('random', 'first', 'last', 'median_of_3'")
    list_of_numbers[0], list_of_numbers[initial_pivot_i] = list_of_numbers[initial_pivot_i], list_of_numbers[0]
    # Recursive iteration
    for k in range(1, n_num):
        if list_of_numbers[k] < list_of_numbers[0]:
            i += 1
            list_of_numbers[i], list_of_numbers[k] = list_of_numbers[k], list_of_numbers[i]
    list_of_numbers[0], list_of_numbers[i] = list_of_numbers[i], list_of_numbers[0]
    list_of_numbers = \
        quick_sort(list_of_numbers[0:i], pivot_element=pivot_element, initialize_counter=False) + \
        list_of_numbers[i:(i+1)] + \
        quick_sort(list_of_numbers[(i+1):n_num], pivot_element=pivot_element, initialize_counter=False)
    return list_of_numbers


if __name__ == '__main__':
    test_samples_first = [[[3, 4, 2, 5, 8, 9, 1, 6, 0, 12, 7, 4, -3, -2, -1], 50],
                          [[4, 5, 2, 3, 1], 7]]
    print("\n------------------------------------------------------------------------")
    print("------------------- QuickSort implementation results -------------------")
    print("------------------------------------------------------------------------")
    for test_sample in test_samples_first:
        print("Unsorted list: ")
        print(test_sample[0])
        print("Sorted list: ")
        print(quick_sort(test_sample[0], pivot_element="first"))
        print(n_comparisons)
    with open('QuickSort_array.txt', 'r') as f:
        exam_vec = [int(vec_val.strip("\r\n")) for vec_val in f.readlines()]

    print("The final response to the first exercise is:")
    sorted_array_1 = quick_sort(list(exam_vec), pivot_element="first")  # type: list
    print(n_comparisons)

    print("The final response to the second exercise is:")
    sorted_array_2 = quick_sort(list(exam_vec), pivot_element="last")  # type: list
    print(n_comparisons)

    print("The final response to the third exercise is:")
    sorted_array_3 = quick_sort(list(exam_vec), pivot_element="median_of_3")  # type: list
    print(n_comparisons)

    assert sorted_array_1 == sorted_array_2
    assert sorted_array_1 == sorted_array_3
