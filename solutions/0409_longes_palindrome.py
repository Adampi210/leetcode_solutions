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

# Another possible solution is to use a set and track characters with even counts
# It works in-time, i.e. after iterating over the string once
# The way it works: for any character not in the set, we add it
# If we see it again, we remove it from the set and increase the total length by 2
# At the end, if the set is not empty, we can add 1 to the total length
# since we can place one odd character in the center of the palindrome
class SolutionSet(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Initialize an empty set to track characters with odd counts
        char_set = set()
        # Initialize the total length of the palindrome
        total_len = 0
        # Iterate through each character in the string
        for char_s in s:
            # If the character is already in the set, it means we've seen it an even number of times
            if char_s in char_set:
                # Remove it from the set and increase total_len by 2
                char_set.remove(char_s)
                total_len += 2
            else:
                # If it's not in the set, add it (indicating an odd count)
                char_set.add(char_s)
        # After processing all characters, if the set is not empty,
        # it means we have at least one character with an odd count
        # We can place one such character in the center of the palindrome
        if char_set:
            total_len += 1
        return total_len