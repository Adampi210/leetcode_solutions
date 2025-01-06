# Given a string s containing just the characters 
# '(', ')', '{', '}', '[' and ']'
# determine if the input string is valid.

# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type

def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    # First of all, create a dictionary that will map the closed brackets to open brackets
    bracket_map = {")": "(", "}": "{", "]": "["}
    # Define a set of open brackets for O(1) lookup
    open_brackets = set(bracket_map.values())
    # Define the stack for the brackets
    bracket_stack = []

    # Go through all the brackets in the input string
    for bracket in s:
        # If it is an open bracket, add it to the stack
        if bracket in open_brackets:
            bracket_stack.append(bracket)
        # If it is a closed bracket, run some checks
        # First check if the stack is empty (if yes, then it's invalid)
        # Second check if the last bracket in the stack is the corresponding open bracket
        # If no, then it's invalid
        else:
            if not bracket_stack or bracket_map[bracket] != bracket_stack[-1]:
                return False
            # If the checks were fine, pop the last bracket from the stack (the open one)
            bracket_stack.pop()
    # Then return if the stack is empty (if it is, then all brackets were closed)
    # If not, then there are some open brackets left
    return not bracket_stack
