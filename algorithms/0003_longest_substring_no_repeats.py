# Given a string s, find the length of the longest
# substring without repeating characters

# Faster than 73% of python submissions
def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    # Initialize variables for keeping the sliding window
    max_len = 0
    curr_len = 0
    start_idx = 0
    end_idx = 1
    letters_in = {}
    # Iterate over all characters in the string
    for i, letter in enumerate(s):
        # If the letter is in the dictionary, update the start index
        # Either go to the next index after the last occurrence of the letter
        # Or stay at the current start index (if the last occurrence is before the current start index)
        if letter in letters_in:
            start_idx = max(letters_in[letter] + 1, start_idx)
        # Always update the end index, dictionary, and the current length
        end_idx += 1
        letters_in[letter] = i
        curr_len = end_idx - start_idx - 1
        # Update the maximum length if the current length is greater
        if curr_len > max_len:
            max_len = curr_len
    return max_len
