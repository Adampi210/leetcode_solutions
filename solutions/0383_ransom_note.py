# Given two strings ransomNote and magazine, 
# return true if ransomNote can be constructed 
# by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.


# Key insight: Count frequency of each letter in ransomNote
# Then decrement the count for each letter found in magazine
# If any letter's count is still positive after processing magazine,
# it means ransomNote cannot be constructed

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # Count frequency of each letter in ransomNote
        letters_in_ransom_Note = {}
        # Build frequency dictionary for ransomNote
        for char_ransom in ransomNote:
            letters_in_ransom_Note[char_ransom] = (
                letters_in_ransom_Note.get(char_ransom, 0) + 1
            )
        # Decrement the count for each letter found in magazine
        for char_mag in magazine:
            if char_mag in letters_in_ransom_Note:
                letters_in_ransom_Note[char_mag] -= 1
        # Check if any letter's count is still positive
        for freq_letters in letters_in_ransom_Note.values():
            if freq_letters > 0:
                # If any letter's count is still positive, 
                # ransomNote cannot be constructed
                return False
        # If all letter counts are zero or negative,
        # ransomNote can be constructed
        return True
