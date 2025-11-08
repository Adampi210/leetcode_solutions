# Given head, the head of a linked list, determine if the linked list
# has a cycle in it. There is a cycle in a linked list
# if there is some node in the list that can be
# reached again by continuously following the next pointer.
# Return true if there is a cycle in the linked list. Otherwise, return false.

# KEY IDEA: Use 2 pointers (Floyd's Tortoise and Hare algorithm)
# One pointer (slow) moves 1 step at a time
# The other pointer (fast) moves 2 steps at a time
# If there is a cycle, the fast pointer will eventually meet the slow pointer
# Since the relative speed between the two pointers is 1 step per move
# So if there is a cycle, they will meet within n moves (where n is the number of nodes in the cycle)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from collections import deque

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # Initialize fast and slow pointers to the head of the linked list
        fast_pointer = head
        slow_pointer = head
        # Traverse the linked list with both pointers
        # Keep moving until the fast pointer reaches the end of the list
        # (i.e., fast_pointer is None or fast_pointer.next is None)
        while fast_pointer and fast_pointer.next:
            # Move the fast pointer 2 steps and the slow pointer 1 step
            fast_pointer = fast_pointer.next.next
            slow_pointer = slow_pointer.next
            # Check if the fast pointer has caught up to the slow pointer
            if fast_pointer == slow_pointer:
                # If they meet, there is a cycle in the linked list
                return True
        # If we reach the end of the list without the pointers meeting
        # then there is no cycle
        return False
