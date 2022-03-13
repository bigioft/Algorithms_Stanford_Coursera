# coding=utf-8


def integer_multiplication(int1, int2):
    # Check whether the length (in the decimal notation) of the integer is more than 1 digit
    # Should this be with both below 1 or one below one? build both options and time them
    int_1_digits = len(str(int1))
    int_2_digits = len(str(int2))
    if int_1_digits < 2 or int_2_digits < 2:
        return int1 * int2
    # Add 2 elseif, for the 2 individually being below length 1 digit
    else:
        a_int = int1/(10**(int_1_digits/2))
        b_int = int1 - a_int * 10**(int_1_digits/2)
        c_int = int2/(10**(int_2_digits/2))
        d_int = int2 - c_int * (10**(int_2_digits/2))

        ac_int = integer_multiplication(a_int, c_int) * \
            (10**(int_1_digits/2)) * (10**(int_2_digits/2))  # degree of a * degree of c
        bd_int = integer_multiplication(b_int, d_int)
        bc_int = integer_multiplication(b_int, c_int) * (10**(int_2_digits/2))  # degree of c
        ad_int = integer_multiplication(a_int, d_int) * (10**(int_1_digits/2))  # degree of a
        return ac_int + bd_int + bc_int + ad_int


if __name__ == '__main__':
    integer_1 = 3141592653589793238462643383279502884197169399375105820974944592
    integer_2 = 2718281828459045235360287471352662497757247093699959574966967627

    testing_pairs = [[13, 14], [1234, 5678], [1234543, 5678098]]
    print("\n-----------------------------------------------------------------------")
    print("------------ Integer Multiplication implementation results ------------")
    print("-----------------------------------------------------------------------")
    for test_pair in testing_pairs:
        assert integer_multiplication(test_pair[0], test_pair[1]) == (test_pair[0] * test_pair[1])
        print("Test " + str(test_pair) +
              " passed wih result " + str(integer_multiplication(test_pair[0], test_pair[1])) + ".")
    print("The result of the assignment according to the implemented integer multiplication is: ")
    print(str(integer_multiplication(integer_1, integer_2)))
