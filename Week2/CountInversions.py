# coding=utf-8

from MergeCount import merge_count


def count_inversions(vec):
    n = len(vec)
    split_point = n/2
    if n == 1:
        #  base case
        return [vec, 0]
    else:
        ordered_left_side, x = count_inversions(vec[0:split_point])
        ordered_right_side, y = count_inversions(vec[split_point:n])
        ordered_vec, z = merge_count(ordered_left_side, ordered_right_side)
        return [ordered_vec, x + y + z]


if __name__ == '__main__':
    list_of_tests = [[[1, 3, 5, 2, 4, 6], 3],  # Test case 1 and answer
                     [[1, 5, 3, 2, 4], 4],  # Test case 2 and answer
                     [[9, 12, 3, 1, 6, 8, 2, 5, 14, 13, 11, 7, 10, 4, 0], 56],  # Test case 3 and answer
                     [[4, 80, 70, 23, 9, 60, 68, 27, 66, 78, 12, 40, 52, 53, 44, 8, 49, 28, 18, 46,
                       21, 39, 51, 7, 87, 99, 69, 62, 84, 6, 79, 67, 14, 98, 83, 0, 96, 5, 82, 10,
                       26, 48, 3, 2, 15, 92, 11, 55, 63, 97, 43, 45, 81, 42, 95, 20, 25, 74, 24, 72,
                       91, 35, 86, 19, 75, 58, 71, 47, 76, 59, 64, 93, 17, 50, 56, 94, 90, 89, 32,
                       37, 34, 65, 1, 73, 41, 36, 57, 77, 30, 22, 13, 29, 38, 16, 88, 61, 31, 85, 33,
                       54], 2372]]  # Test case 4 and answer
    print("\n-----------------------------------------------------------------------------")
    print("------------------- CountInversions implementation results -------------------")
    print("------------------------------------------------------------------------------")
    for test in list_of_tests:
        assert count_inversions(vec=test[0])[1] == test[1]
        print("Test " + str(test) +
              " passed with result " + str(count_inversions(vec=test[0])[1]) + ".")
    with open('IntegerArray.txt', 'r') as f:
        exam_vec = [int(vec_val.strip("\r\n")) for vec_val in f.readlines()]

    print("The final response to the exercise is:")
    print(count_inversions(vec=exam_vec)[1])
