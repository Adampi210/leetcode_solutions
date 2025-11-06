# Constant
INT_32_MAX = 2**31 - 1

# Given a 32-bit signed integer, reverse digits of an integer.
def reverse_int_32(x):
    """
    :type x: int
    :rtype: int
    """
    # Initialize variables
    reversed_int = 0
    multip_neg = 1
    # If the integer is negative, make it positive and
    # remember to make the result negative
    if x < 0:
        x *= -1
        multip_neg = -1
    # Reverse the integer
    while x > 0:
        reversed_int = reversed_int * 10 + x % 10
        x = x // 10
    # If the reversed integer is greater than
    # the 32-bit signed integer limit, return 0
    if reversed_int > INT_32_MAX:
        return 0
    return reversed_int * multip_neg


if __name__ == "__main__":
    print(reverse_int_32(-123))  # -321
