# Given two binary strings a and b, return their sum as a binary string.

def addBinary(self, a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    # Get the maximum length of the two strings
    max_len = max(len(a), len(b))
    # Then fill the strings with 0s to make them the same length
    a = a.zfill(max_len)
    b = b.zfill(max_len)

    # Initialize the result and carry
    result = ""
    carry = 0

    # Iterate over the strings from right to left
    for i in range(max_len - 1, -1, -1):
        # Calculate r as the sum of the carry and the two digits
        r = carry
        r += 1 if a[i] == "1" else 0
        r += 1 if b[i] == "1" else 0
        # Add the remainder of r % 2 to the result
        result = str(r % 2) + result
        # Recalculate the carry
        carry = 0 if r < 2 else 1

    # If there is a carry left, add it to the result
    if carry != 0:
        result = "1" + result

    return result
