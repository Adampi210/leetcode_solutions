# 242. Valid Anagram
# Given two strings s and t, return true if t is an anagram of s,
# and false otherwise.

# KEY IDEAS:
# - An anagram means both strings have the same characters with the same frequencies
# - We can use a hash map (dictionary) to count the frequency of each character in both strings
# - First count the characters in string s
# - Then decrement the count for each character found in string t
# - If at any point a character in t is not found in the dictionary or its count goes below zero, return false
# - Finally, if all counts are zero, return true
# - At most O(2N)
# NOTE: There is a potentially faster solution using zip but only works for letters (the above is faster for UNICODE)

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Create a dictionary to count the frequency of each character
        letters_dict = {}
        # First check if the lengths are different (if yes, return false)
        if len(s) != len(t):
            return False
        # Count the frequency of each character in s
        for s_char in s:
            letters_dict[s_char] = letters_dict.get(s_char, 0) + 1
        # Decrement the frequency for each character in t
        for t_char in t:
            # If the character is not found in the dictionary, return false
            if t_char not in letters_dict:
                return False
            # Decrement the count
            letters_dict[t_char] = letters_dict.get(t_char, 0) - 1
            # If the count goes below zero, return false
            if letters_dict[t_char] < 0:
                return False
        # Finally, check if all counts are zero
        return True

### Second Solution using zip
# For letters it's O(N + 26)
# For unicode characters it's O(N + M) where M is the size of the character set
class SolutionZip(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        letters_dict = {}
        # First check if the lengths are different (if yes, return false)
        if len(s) != len(t):
            return False
        # Count the frequency of each character in s and t simultaneously
        for s_char, t_char in zip(s, t):
            letters_dict[s_char] = letters_dict.get(s_char, 0) + 1
            letters_dict[t_char] = letters_dict.get(t_char, 0) - 1
        # Finally, check if all counts are zero
        if any(letters_dict.values()):
            # If any value is not zero, return false
            return False
        # If all values are zero, return true
        return True
