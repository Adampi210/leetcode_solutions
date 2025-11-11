# Given an integer array nums,
# return true if any value appears at least twice in the array,
# and return false if every element is distinct.

# KEY IDEA: Use a set to track seen numbers.
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Use a set to track seen numbers
        set_nums = set()
        # Iterate through the numbers
        for num in nums:
            # If the number is already in the set, return True
            # (since a duplicate is found)
            if num in set_nums:
                return True
            # Otherwise, add the number to the set
            else:
                set_nums.add(num)
        # If no duplicates were found, return False
        return False
