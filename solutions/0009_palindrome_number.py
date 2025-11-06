# Given an integer x, return true if x is
# a palindrome and false otherwise.

# Note: this is a clever way to solve this, think about that in the future
# What if we reverse the order? What if we look at the problem from a different angle?
# By reversing we're achieving the same result as comparing the first half with the second half
# But we're only doing half the work
# We don't have to know the length of the number in advance using this solution
# This makes it very efficient
def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    # If x is negative or ends with 0 and is not 0
    # then it is not a palindrome number
    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    # Reverse bottom half of the number
    # That way we can compare them easily to see if they are equal
    reversed_half = 0
    # To reverse, run the loop until x is less or equal to the reversed_half
    while x > reversed_half:
        reversed_half = 10 * reversed_half + x % 10
        x //= 10

    # If the integer has an even number of digits, then x == reversed_half
    # If its odd, then x == reversed_half // 10 (this removes the middle number)
    return x == reversed_half or x == reversed_half // 10
