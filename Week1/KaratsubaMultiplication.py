# coding=utf-8

import math
from IntegerMultiplication import integer_multiplication


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
    if int_1_digits < 2 or int_2_digits < 2:
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
        return ac_int * 10**n + ad_plus_bc_int * 10**(n/2) + bd_int


if __name__ == '__main__':
    integer_1 = 3141592653589793238462643383279502884197169399375105820974944592
    integer_2 = 2718281828459045235360287471352662497757247093699959574966967627

    testing_pairs = [[13, 14], [1234, 5678], [1234543, 5678098]]

    print("\n-------------------------------------------------------------------------")
    print("------------ Karatsuba Multiplication implementation results ------------")
    print("-------------------------------------------------------------------------")
    for test_pair in testing_pairs:
        assert karatsuba_multiplication(test_pair[0], test_pair[1]) == (test_pair[0] * test_pair[1])
        print("Test " + str(test_pair) +
              " passed with result " + str(karatsuba_multiplication(test_pair[0], test_pair[1])) + ".")
    print("The result of the assignment according to the implemented Karatsuba multiplication is: ")
    print(str(karatsuba_multiplication(integer_1, integer_2)))

    print("\nInteger Multiplication and Karatsuba Multiplication yield the same result to the assignment: " +
          str(karatsuba_multiplication(integer_1, integer_2) == integer_multiplication(integer_1, integer_2)) +
          "\n")
