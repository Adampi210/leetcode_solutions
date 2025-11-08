# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

# Key insight: Classic binary search problem
# We need to find the first occurrence of a "bad version"
# We can do this by checking the middle version
# If it's bad, we know the first bad version is at or before it
# If it's good, we know the first bad version is after it
# Only difference: if it is bad, it could be the first bad version
# So cannot exclude it from the search space
class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Initialize the search space, which is from version 1 to version n
        start_idx, end_idx = 1, n
        # Binary search loop
        while start_idx < end_idx:
            # Find the middle version to check
            ver_num = start_idx + (end_idx - start_idx) // 2
            # Check if the middle version is bad
            if isBadVersion(ver_num):
                # If it is bad, the first bad version is at or before ver_num
                # So we move the end index to ver_num
                end_idx = ver_num
            else:
                # If it is good, the first bad version is after ver_num
                # So we move the start index to ver_num + 1
                start_idx = ver_num + 1
        # When start_idx meets end_idx, we have found the first bad version
        return start_idx
        