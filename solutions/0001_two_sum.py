# Given an array of integers and a target integer, 
# return indices of the two numbers such that they add up to target.

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Dictionary to store numbers and their indices
        num_map = {}
        # Iterate through the list of numbers
        for i, num in enumerate(nums):
            # Check if the complement (target - num) exists in the dictionary
            if target - num in num_map:
                return (num_map[target - num], i)
            # Store the number and its index in the dictionary
            num_map[num] = i
