# Given two sorted arrays nums1 and nums2 of size m and n respectively,
# return the median of the two sorted arrays.

# KEY IDEAS:
# - Re-frame the Problem from Finding a Value to Finding a Structure
#   - The real goal is to find the perfect partition (the "cut" or "split")
#     that divides the entire system into two correct halves
# - Use Constraints to Reduce Variables
#   - Create a fixed relationship: i + j = (m+n+1)//2. This locks j to i (j becomes k - i)
#     The problem collapses from finding i and j to just finding i
# - Binary Search on the Structure, Not the Value.
# - Create an O(1) Check

# SOLUTION:
# - First NOTE: we're looking for the median, which is the middle value in a sorted list.
# - The median will divide the combined sorted list into two halves of equal length (or within 1 element for odd lengths).
# - Let's call these left half and right half.
# - Both arrays contain elements from the left half and right half.
# - Define: index i divides nums1 into elements in the left half and the right half
# - Define: index j divides nums2 into elements in the left half and the right half
# - NOTE: REFORMULATE the problem in terms of i and j:
#   - We're not looking for the median anymore
#   - We're looking for the way to split nums1 and nums2 into left and right halves such that:
#     1) The number of elements in the left half is equal (or within 1 element) to the number of elements in the right half
#     2) All elements in the left half must be less than or equal to all elements in the right half
# - To achieve that NOTICE:
#   - The first condition can be expressed as: i + j == (m + n + 1) // 2
#   (since i + j == length of left half and (m + n + 1) // 2 gives the correct split for both even and odd lengths)
#   - The second condition can be expressed as: nums1[i - 1] <= nums2[j] and nums2[j - 1] <= nums1[i]
#   (since nums1[i - 1] and nums2[j - 1] are the largest elements in the left half,
#   and nums1[i] and nums2[j] are the smallest elements in the right half)
#   (Also note that nums1[i - 1] <= nums1[i] is always true, so we must compare across arrays)
#   (And when we do that, we ensure that all elements in the left half are less than or equal to all elements in the right half)
# - NOTE: Since j == (m + n + 1) // 2 - i (derived from the first condition), we're only looking for i
# - NOTE: The search space for i is from 0 to m (length of nums1) and nums1 is sorted
# - NOTE: So we can use binary search to find the correct i
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # Get the lengths of both arrays
        m = len(nums1)
        n = len(nums2)

        # Always run the binary search on the smaller array
        # If nums1 is longer than nums2, swap them and run the function again
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)

        # Define the initial search space, the index 
        low, high = 0, m

        # Binary search loop
        while True:
            # First, the i is in the middle of the current search space
            i = (low + high) // 2
            # Then, j is derived from i based on the first condition
            j = (m + n + 1) // 2 - i

            # Now, get the boundary elements around the partition for both arrays
            # Need these to check the second condition, the median will be found iff
            # leftMax1 <= rightMin2 and leftMax2 <= rightMin1 (inter array comparisons)
            # NOTE: Handle edge cases where i or j is 0 or at the end of the array
            # If i == 0, it means there are no elements in the left half from nums1,
            # so we set leftMax1 to -infinity to ensure the condition always holds
            # Similarly for other boundary cases
            leftMax1 = -float("inf") if (i == 0) else nums1[i - 1]
            rightMin1 = float("inf") if (i == m) else nums1[i]
            leftMax2 = -float("inf") if (j == 0) else nums2[j - 1]
            rightMin2 = float("inf") if (j == n) else nums2[j]

            # Now check the second condition
            # if leftMax1 > rightMin2, it means we have too many elements from nums1 in the left half
            # so we need to move i to the left (decrease i)
            if leftMax1 > rightMin2:
                high = i - 1
            # if leftMax2 > rightMin1, it means we have too few elements from nums1 in the left half
            # so we need to move i to the right (increase i)
            elif rightMin1 < leftMax2:
                low = i + 1
            # If both conditions are satisfied, we have found the correct partition
            else:
                break
        # Finally, calculate the median based on the total length being odd or even
        # If odd, the median is the max of the left halves
        if (m + n) % 2 == 1:
            return max(leftMax1, leftMax2)
        # If even, the median is the average of the max of the left halves and the min of the right halves
        else:
            return (max(leftMax1, leftMax2) + min(rightMin1, rightMin2)) / 2.0
