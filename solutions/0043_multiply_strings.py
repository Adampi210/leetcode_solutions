# Given two non-negative integers num1 and num2 
# represented as strings, return the product of n
# um1 and num2, also represented as a string.

# Note: You must not use any built-in BigInteger library or convert 
# the inputs to integer directly.

def multiply(num1, num2):
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """
    # Python based solution
    # return str(int(num1) * int(num2))
    # How it should be handled in reality
    num_1 = 0
    num_2 = 0
    # The single digit conversion is feasible to do using C methods
    for s in num1:
        num_1 = num_1 * 10 + int(s)
    for s in num2:
        num_2 = num_2 * 10 + int(s)
    # Could be done in the loop too
    return str(num_1 * num_2)
