# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps.
# In how many distinct ways can you climb to the top?

# Key insight: This is a classic dynamic programming problem
# The number of ways to reach step n is the sum of the ways to reach
# step n-1 and step n-2
# because from step n-1, you can take 1 step to reach n
# and from step n-2, you can take 2 steps to reach n
# NOW, there are various ways to solve this problem
# Recursively or iteratively with a queue will work, BUT
# they will take too much time, since they involve repeated calculations
# Instead, use Memoization
# NOTE: Instead of going top-down, we can go bottom-up
# Start from the base cases and build up to n
# To reach step 1, there is 1 way (1 step)
# To reach step 2, there are 2 ways (1+1 steps or 2 steps)
# To reach step 3, we can reach it from step 2 (1 step) or step 1 (2 steps)
# So total ways to reach step 3 is ways(2) + ways(1) = 2 + 1 = 3
# To reach step 4, we can reach it from step 3 (1 step) or step 2 (2 steps)
# So total ways to reach step 4 is ways(3) + ways(2) = 3 + 2 = 5
# So we can keep track of the last two computed values and build up to n
# NOTE: This is a Fibonacci sequence problem in disguise
# The number of ways to reach step n is the nth Fibonacci number
# NOTE: This solution has O(N) time complexity and O(1) space complexity

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # If there is 1 step, there is 1 way to climb
        if n == 1:
            return 1
        # If there are 2 steps, there are 2 ways to climb
        possible_ways_prev, possible_ways_curr = 1, 2
        # Start from step 3 and build up to step n
        counter = 2
        # Iteratively compute the number of ways to reach each step
        while counter < n:
            # The number of ways to reach the current step
            # is the sum of the ways to reach the two previous steps
            # Update the previous two values for the next iteration
            possible_ways_temp = possible_ways_prev + possible_ways_curr
            possible_ways_prev = possible_ways_curr
            possible_ways_curr = possible_ways_temp
            # Increment the counter
            counter += 1
        # Return the number of ways to reach step n
        return possible_ways_curr
