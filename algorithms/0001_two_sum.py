# Given an array of integers and a target integer, return indices of the two numbers such that they add up to target.

def twoSum(nums, target):
    if_sum = dict()
    for i, num in enumerate(nums):
        if target - num in if_sum:
            return [if_sum[target - num], i]
        if_sum[num] = i
