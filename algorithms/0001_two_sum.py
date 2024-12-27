# Given an array of integers and a target integer, return indices of the two numbers such that they add up to target.

def twoSum(nums, target):
    if_sum = dict()
    # Go over all numbers in the list
    for i, num in enumerate(nums):
        # If the compliment of the current number is in the dictionary, return the indices
        if target - num in if_sum:
            return [if_sum[target - num], i]
        # Otherwise, add the number to the dictionary
        if_sum[num] = i
