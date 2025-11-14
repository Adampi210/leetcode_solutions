# Given an integer array nums, 
# find the subarray with the largest sum, and return its sum.

# Key idea: Kadane's Algorithm
# We iterate through the array, keeping track of the maximum subarray sum 
# ending at the current position.
# HOW? This is the best part:
# Suppose we're at a new number: num
# There are only 2 choices to get the best subarray ending at num:
# 1. Either we add num to the previous best subarray sum (curr_max + num) 
# (if it's beneficial, i.e. num makes the subarray larger)
# 2. Or we start a new subarray from num (just num)
# Then we keep track of largest curr_max we've seen so far (global_max).
# And return that at the end.
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Initialize curr_max and global_max to the first element
        curr_max = nums[0]
        global_max = nums[0]
        # Iterate through the array starting from the second element
        for num in nums[1:]:
            # Update curr_max to be the maximum of (curr_max + num) and num
            # This decides whether to extend the current subarray or start a new one
            # If curr_max + num is larger, we extend the subarray
            # If num is larger, we start a new subarray from num
            # (Think about it that way: 
            # if curr_max is negative, adding it to num would only decrease num,)
            # so we start fresh from num
            # Otherwsise, we continue the existing subarray
            # Because adding it to num would increase num
            curr_max = max(curr_max + num, num)
            # Update global_max if the current curr_max is greater
            if curr_max > global_max:
                global_max = curr_max
        # At the end, global_max contains the largest subarray sum
        return global_max
