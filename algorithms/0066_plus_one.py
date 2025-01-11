# You are given a large integer represented as an integer array digits, 
# where each digits[i] is the ith digit of the integer. 
# The digits are ordered from most significant to 
# least significant in left-to-right order. 
# The large integer does not contain any leading 0's.
# Increment the large integer by one and 
# return the resulting array of digits.

# Adds one at the end of the array
def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    # Start with the remainder being 1 to initiate the loop
    remainder = 1
    new_digits = []
    # Pop the last digit and add 1 to it as long as there is a remainder
    while remainder != 0:
        # If there are no more digits, add 1 to the new_digits array (so init digit to 0)
        try:
            digit = digits.pop()
        except:
            digit = 0
        # Increment the digit and add it to the new_digits array
        digit = (digit + 1) % 10
        new_digits = [digit,] + new_digits
        # If the digit is 0, there is a remainder, otherwise there is none
        if digit == 0:
            remainder = 1
        else:
            remainder = 0
        if remainder == 0:
            break
    # Add the remaining digits (that werent iterated over) to the new_digits array
    return digits + new_digits
