# Given a string s consisting of words and spaces, 
# return the length of the last word in the string

def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """
    # Remove trailing spaces
    s = s.rstrip(" ")
    # Then start from the end
    x = -1
    len_s = len(s)
    # Iterate until reaching space or the end of the string
    while -x - 1 != len_s and s[x] != " ":
        # Change the index from the right
        x -= 1
    # Return the length of the last word (which corresponds to the index from the right)
    return -x - 1
