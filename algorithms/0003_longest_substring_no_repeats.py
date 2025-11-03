# Given a string s, find the length of the longest
# substring without repeating characters


# Faster than 73% of python submissions
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Sliding window approach
        # Initialize variables
        start_idx = 0   # Pointer to the start of the current substring
        max_len = 0     # Length of the longest substring found
        letters_in = {} # Dictionary to store the last seen index of each letter

        # Iterate through the string
        for end_idx, letter in enumerate(s):
            # If the letter is already in the current substring,
            # move the start pointer based on: 
            # If the letter was seen after the current start_idx,
            # move start_idx to one position after the last seen index of that letter
            # If the letter was seen before the current start_idx,
            # do not move start_idx (since it's already ahead, so doesn't contain the letter)
            if letter in letters_in:
                start_idx = max(start_idx, letters_in[letter] + 1)
            # Update the last seen index of the letter
            letters_in[letter] = end_idx
            # Calculate the length of the current substring
            curr_len = end_idx - start_idx + 1
            # Update max_len if the current length is greater
            if curr_len > max_len:
                max_len = curr_len
        return max_len
