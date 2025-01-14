# Convert a roman numeral to an integer

def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    # Dictionary to map the roman numerals to integers
    val_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    # Keep track of the integer and the previous value
    integer = 0
    prev_value = 0

    # Traverse the string from right to left
    for char in reversed(s):
        value = val_map[char]

        # If the current value is less than the previous value,
        # it should be subtracted (so for example IX will be 10 - 1 = 9)
        if value < prev_value:
            integer -= value
        # Otherwise, add the value to the integer
        else:
            integer += value
            prev_value = value  # Update the previous value

    return integer
