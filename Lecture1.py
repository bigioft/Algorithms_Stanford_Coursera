# coding=utf-8

import math


def karatsuba_multiplication(int1, int2):
    # TODO: karatsuba can work with any base, generalize the function and allow the base as an input
    #  and remember that this interpretation is incompatible with the one of the number of digits,
    #  which is specifically for base 10. Adjust accordingly.
    #  Ref: https://iq.opengenus.org/karatsuba-algorithm/
    # The function behaves assuming the inputted numbers have an equal number of digits (n) which is a power of 2
    # that is equivalent to padding the left side both numbers with 0s until n digits are reached
    # Check whether the length (in the decimal notation) of the integer is more than 1 digit
    # Should this be with both below 1 or one below one? build both options and time them
    int_1_digits = len(str(int1))
    int_2_digits = len(str(int2))
    n = 2**(int(math.ceil(math.log(max(int_1_digits, int_2_digits), 2))))
    if int_1_digits<2 or int_2_digits<2:
        return int1 * int2
    # TODO: Add 2 elseif, for the 2 individually being below length 1 digit
    else:
        a_int = int1/(10**(n/2))
        b_int = int1 - a_int * 10**(n/2)
        c_int = int2/(10**(n/2))
        d_int = int2 - c_int * (10**(n/2))
        ac_int = karatsuba_multiplication(a_int, c_int)
        bd_int = karatsuba_multiplication(b_int, d_int)
        ad_plus_bc_int = karatsuba_multiplication(a_int + b_int, c_int + d_int) - ac_int - bd_int
        return ac_int * 10**(n) + \
               ad_plus_bc_int * 10**(n/2) + \
               bd_int


def integer_multiplication(int1, int2):
    # Check whether the length (in the decimal notation) of the integer is more than 1 digit
    # Should this be with both below 1 or one below one? build both options and time them
    int_1_digits = len(str(int1))
    int_2_digits = len(str(int2))
    if int_1_digits<2 or int_2_digits<2:
        return int1 * int2
    # Add 2 elseif, for the 2 individually being below length 1 digit
    else:
        a_int = int1/(10**(int_1_digits/2))
        b_int = int1 - a_int * 10**(int_1_digits/2)
        c_int = int2/(10**(int_2_digits/2))
        d_int = int2 - c_int * (10**(int_2_digits/2))

        ac_int = integer_multiplication(a_int, c_int) * (10**(int_1_digits/2)) * (10**(int_2_digits/2)) # degree of a * degree of c
        bd_int = integer_multiplication(b_int, d_int)
        bc_int = integer_multiplication(b_int, c_int) * (10**(int_2_digits/2)) # degree of c
        ad_int = integer_multiplication(a_int, d_int) * (10**(int_1_digits/2)) # degree of a
        return ac_int + bd_int + bc_int + ad_int


def Merge(list_1, list_2):
    # Initialize list counters and final list
    i = 0; j = 0; merged_list = []
    # Loop through the individually sorted lists, and
    # append the smallest of the smallest numbers to the final list
    # until one of the lists has been exhausted
    while (i<len(list_1)) & (j<len(list_2)):
        if list_1[i] < list_2[j]:
            merged_list.append(list_1[i])
            i+=1
        else:
            merged_list.append(list_2[j])
            j+=1
    # One of the 2 will be empty, so the order doesn't matter
    remaining_numbers = list_1[i:len(list_1)] + list_2[j:len(list_2)]
    merged_list = merged_list + remaining_numbers
    return merged_list

def Sort(list_of_numbers):
    N_num = len(list_of_numbers)
    if N_num == 1:
        # Case 0 of the recursive function
        return list_of_numbers
    else:
        # Recursive iteration
        list_1 = Sort(list_of_numbers[0:(N_num/2)])
        list_2 = Sort(list_of_numbers[(N_num/2):N_num])
        list_of_numbers = Merge(list_1, list_2)
        return list_of_numbers

list_of_numbers = [3,4,2,5,8,9,1,6,0]

integer_1 = 3141592653589793238462643383279502884197169399375105820974944592
integer_2 = 2718281828459045235360287471352662497757247093699959574966967627

testing_pairs = [[13, 14], [1234, 5678], [1234543, 5678098]]

if __name__ == '__main__':
    print("\n-----------------------------------------------------------------------")
    print("------------ Integer Multiplication implementation results ------------")
    print("-----------------------------------------------------------------------")
    for test_pair in testing_pairs:
        assert integer_multiplication(test_pair[0], test_pair[1]) == (test_pair[0] * test_pair[1])
        print("Test " + str(test_pair) +
              " passed wih result " + str(integer_multiplication(test_pair[0], test_pair[1])) + ".")
    print("The result of the assignment according to the implemented integer multiplication is: ")
    print(str(integer_multiplication(integer_1, integer_2)))

    print("\n-------------------------------------------------------------------------")
    print("------------ Karatsuba Multiplication implementation results ------------")
    print("-------------------------------------------------------------------------")
    for test_pair in testing_pairs:
        assert karatsuba_multiplication(test_pair[0], test_pair[1]) == (test_pair[0] * test_pair[1])
        print("Test " + str(test_pair) +
              " passed wih result " + str(karatsuba_multiplication(test_pair[0], test_pair[1])) + ".")
    print("The result of the assignment according to the implemented Karatsuba multiplication is: ")
    print(str(karatsuba_multiplication(integer_1, integer_2)))

    print("\nInteger Multiplication and Karatsuba Multiplication yield the same result to the assignment: " + str(karatsuba_multiplication(integer_1, integer_2) == integer_multiplication(integer_1, integer_2)) + "\n")

    print("\n------------------------------------------------------------------------")
    print("------------------- Mergesort implementation results -------------------")
    print("------------------------------------------------------------------------")
    print("Unsorted list: ")
    print(list_of_numbers)
    print("Sorted list: ")
    print(Sort(list_of_numbers))


