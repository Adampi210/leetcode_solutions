# Given an array of integers and a target integer, return indices of the two numbers such that they add up to target.

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Dictionary to store numbers and their indices
        seen_map = {}
        for i, num in enumerate(nums):
            # If the complement (target - num) exists in the map, return the indices
            if target - num in seen_map:
                return (seen_map[target - num], i)
            # Otherwise, add the current number and its index to the map
            seen_map[num] = i
    