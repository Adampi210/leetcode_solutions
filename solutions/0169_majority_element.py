# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. 
# You may assume that the majority element always exists in the array.

# KEY IDEA: Boyer-Moore Voting Algorithm
# NOTE: It is trivial to do this with a hash map counting occurrences, but it uses O(n) space.
# Instead, use the Boyer-Moore Voting Algorithm to find the majority element in O(n) time and O(1) space.

# Boyer-Moore Voting Algorithm:
# - Works by maintaining a candidate element and a count.
# - Iterate through the array:
#  - If the count is zero, set the current element as the candidate and set count to 1.
#  - If the current element is the same as the candidate, increment the count.
#  - If the current element is different, decrement the count.
# Eventually, the candidate will be the majority element, since it appears more than n/2 times.
# So long as there is a majority element, it will survive the counting process.
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Boyer-Moore Voting Algorithm
        # Initialize candidate and count
        candidate_num = 0
        candidate_count = 0
        # Iterate through the array
        for num in nums:
            # If count is zero, set current element as candidate
            # and set count to 1
            if candidate_count == 0:
                candidate_num = num
                candidate_count += 1
            # Otherwise, compare current element with candidate
            else:
                # If they are the same, increment count
                if num == candidate_num:
                    candidate_count += 1
                # If they are different, decrement count
                else:
                    candidate_count -= 1
        # Return the candidate as the majority element
        return candidate_num
