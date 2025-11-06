# Given an array of integers nums which is sorted in ascending order,
# and an integer target, write a function to search target in nums.
# If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

# KEY IDEAS:
# - Classic Binary Search Problem
# - Use two pointers to represent the current search space (start_idx and end_idx)
# - While the search space is valid (start_idx <= end_idx) search for the target
# - If not found, return -1
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Initialize the search space
        start_idx = 0
        end_idx = len(nums) - 1
        # Perform binary search while the search space is valid
        # I.e. start_idx <= end_idx
        while start_idx <= end_idx:
            # Calculate the middle index
            idx = (start_idx + end_idx) // 2
            # Check if the target is found
            if target == nums[idx]:
                return idx
            # Adjust the search space based on the comparison
            # If target is greater, search in the right half
            if target > nums[idx]:
                start_idx = idx + 1
            # If target is smaller, search in the left half
            else:
                end_idx = idx - 1
        # If the target is not found, return -1
        return -1
