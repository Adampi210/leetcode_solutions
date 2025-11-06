import re

INT_32_MAX = 2**31 - 1
INT_32_MIN = -(2**31)

# Given a string s, implement the myAtoi(s) function
# which converts a string to a 32-bit signed integer
# This one uses regex to match the string
def myAtoi_regex(self, s):
    """
    :type s: str
    :rtype: int
    """
    # Regular expression pattern
    # ^         - Match to the start of the string
    # \s*       - Match zero or more whitespace characters
    # ([+-]?)   - Check for an optional plus or minus sign
    # (0*)      - Match zero or more leading zeros
    # (\d+)     - Finally, get one or more digits
    pattern = r"^\s*([+-]?)(0*)(\d+)"
    match = re.match(pattern, s)
    # If didn't find a match, return 0
    if not match:
        return 0
    # Extract the sign and the number
    sign_str, _, num_str = match.groups()
    # Get the final number within the 32-bit signed integer range
    sign = -1 if sign_str == "-" else 1
    num = sign * int(num_str)
    if num > INT_32_MAX:
        return INT_32_MAX
    if num < INT_32_MIN:
        return INT_32_MIN
    return num
