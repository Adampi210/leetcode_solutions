# Given a sorted array nums, remove the duplicates in-place 
# such that each element appears only once and return the new length.
# Do not allocate extra space for another array;
# you must do this by modifying the input array in-place with O(1) extra memory.

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Check for empty array
        if not nums:
            return 0
        # Initialize the count of unique elements
        total_diff = 1
        # Iterate through the array, starting from the second element
        for i in range(1, len(nums)):
            # If the current element is different from the previous one,
            # it is a unique element that should be kept
            if nums[i] != nums[i - 1]:
                nums[total_diff] = nums[i]
                total_diff += 1
        # Return the count of unique elements
        return total_diff
