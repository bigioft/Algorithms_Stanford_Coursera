# coding=utf-8


def merge_count(list_1, list_2):
    # TODO: Add a check to ensure the incoming lists are sorted individually
    # Counts the number of inversions between list 1 and list 2
    # building block for the "CountInversions.py" script
    # Initialize list counters and final list
    i = 0
    j = 0
    count = 0
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
            # This is actually the important step, counting how many times list_2
            # takes priority over list_1
            count += len(list_1) - i
    # One of the 2 will be empty, so the order doesn't matter
    remaining_numbers = list_1[i:len(list_1)] + list_2[j:len(list_2)]
    merged_list = merged_list + remaining_numbers
    return [merged_list, count]


if __name__ == '__main__':
    list_of_tests = [[[1, 3, 5, 7], [2, 4, 6, 8]]]
    print("\n------------------------------------------------------------------------")
    print("------------------- MergeCount implementation results -------------------")
    print("------------------------------------------------------------------------")
    for test in list_of_tests:
        print(merge_count(list_1=test[0], list_2=test[1]))
