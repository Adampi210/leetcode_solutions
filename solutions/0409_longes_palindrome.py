# Given a string s which consists of lowercase or uppercase letters,
# return the length of the longest palindrome
# that can be built with those letters.
# Letters are case sensitive, for example,
# "Aa" is not considered a palindrome.


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Create a frequency dictionary to count occurrences of each character
        char_freq = {}
        # Populate the frequency dictionary
        for char_s in s:
            char_freq[char_s] = char_freq.get(char_s, 0) + 1
        # Calculate the length of the longest palindrome
        # We'll sum up all even frequencies
        # For odd frequencies, we can use freq - 1 (the largest even number less than freq)
        # and we can have at most one odd character in the center of the palindrome
        max_len_even = 0
        if_odd = 0
        # Iterate through the frequency dictionary
        for freq in char_freq.values():
            # Check if the frequency is even or odd
            if freq % 2 == 0:
                # If even, add the entire frequency to max_len_even
                max_len_even += freq
            else:
                # If odd, add freq - 1 to max_len_even and set if_odd to 1
                max_len_even += freq - 1
                if_odd = 1
        # The total length of the longest palindrome 
        # is the sum of max_len_even and if_odd
        return max_len_even + if_odd
