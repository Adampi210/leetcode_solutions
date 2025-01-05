# Given an integer array nums and an integer val,
# remove all occurrences of val in nums in-place.
# The order of the elements may be changed.
# Then return the number of elements in nums which are not equal to val.

# Remove the desired value from nums array
def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    # Use list comprehension to remove all occurrences of val from nums
    # This is done in-place by using slicing
    # The [:] notation is used to reference the original list
    nums[:] = [x for x in nums if x != val]
    # Return the length of the modified list
    return len(nums)
