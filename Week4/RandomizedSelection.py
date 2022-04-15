# coding=utf-8
import random


def randomized_selection(list_of_numbers, nth_order = 0):
    # TODO: proper description of the function
    """
    Randomized Selection algorithm that follows the course's approach exactly

    :rtype: list
    """
    print(nth_order)
    n_num = len(list_of_numbers)
    if n_num <= 1:
        # Case 0 of the recursive function
        return list_of_numbers
    initial_pivot_i = random.randint(0, n_num - 1)
    i = 0
    list_of_numbers[i], list_of_numbers[initial_pivot_i] = list_of_numbers[initial_pivot_i], list_of_numbers[i]
    # Recursive iteration
    for k in range(1, n_num):
        if list_of_numbers[k] < list_of_numbers[0]:
            i += 1
            list_of_numbers[i], list_of_numbers[k] = list_of_numbers[k], list_of_numbers[i]
    if i == nth_order:
        selected_quantile = list_of_numbers[0]
    elif nth_order > i:
        new_nth_order = nth_order - i - 1
        selected_quantile = randomized_selection(list_of_numbers[(i+1):], nth_order = new_nth_order)
    elif nth_order < i:
        new_nth_order = nth_order
        selected_quantile = randomized_selection(list_of_numbers[1:i], nth_order = new_nth_order)
    return selected_quantile



if __name__ == '__main__':
    test_samples_first = [{'data':[3, 4, 2, 5, 8, 9, 1, 6, 0, 12, 7, 4, -3, -2, -1],
                           'nth_order': 4,
                           'answer' : 1}]
    print("\n------------------------------------------------------------------------")
    print("------------------- Selection implementation results -------------------")
    print("------------------------------------------------------------------------")
    for test_sample in test_samples_first:
        print("Starting task: ")
        print(test_sample)
        print("Extracted quantile: ")
        print(randomized_selection(test_sample['data'], test_sample['nth_order']))
