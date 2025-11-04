# Given a string s, return true if it is a palindrome, or false otherwise.
# A palindrome is a string that reads the same forward and backward, 
# ignoring non-alphanumeric characters and case.


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Initialize two pointers
        i, j = 0, len(s) - 1

        # Move the pointers towards each other
        while i < j:
            # Skip non-alphanumeric characters from the left
            if i < j and not s[i].isalnum():
                i += 1
                continue
            # Skip non-alphanumeric characters from the right
            if i < j and not s[j].isalnum():
                j -= 1
                continue
            # Compare characters in a case-insensitive manner
            if s[i].lower() != s[j].lower():
                # Characters do not match, not a palindrome
                return False
            # Move both pointers inward
            i += 1
            j -= 1
        
        # All characters matched, it is a palindrome
        return True
