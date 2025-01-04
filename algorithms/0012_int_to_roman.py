# Convert an integer num to roman representation

# Function to convert
def intToRoman(num):
    """
    :type num: int
    :rtype: str
    """
    # Create the value map for specific roman numerals
    # Need to include all values that can repeat and all values that are unique
    # Basically all the standard ones as well as the 9 and 4 cases
    val_map = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]

    roman = ""
    # Iterate through the value map
    # We go from highest to lowest value
    # That way it is easiest to see how the values repeat
    # Also it handles the 9 and 4 cases nicely, because if such a case 
    # is found, it will be used once thanks to the order of the value map
    # Then the value map will find 0 for the next count and will move on to the next digit
    # Once again, this is done in kind of a reverse order, think about it in the future
    for value, symbol in val_map:
        # If the number is 0, we're done
        if num == 0:
            break
        # Count how many times the value fits into the number
        # Note that for the 9 and 4 cases, the value will be used once 
        # (has to since otherwise the bigger value is used earlier)
        count = num // value
        # If there is at least one occurrence of the symbol, add it to the roman numeral
        if count:
            roman += symbol * count
            num -= value * count
    return roman
