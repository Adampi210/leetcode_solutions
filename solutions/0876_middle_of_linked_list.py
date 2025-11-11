# Given the head of a singly linked list, 
# return the middle node of the linked list.
# If there are two middle nodes, 
# return the second middle node.

# KEY IDEA: Use two pointers, one moving twice as fast as the other.
# If the fast pointer reaches the end, the slow pointer will have 
# moved half the distance, thus being at the middle node.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Finds the middle node of a singly linked list
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Use two pointers, one moving twice as fast as the other
        pointer_half = head # First pointer, moves one step at a time
        pointer_end = head  # Second pointer, moves two steps at a time
        # When the fast pointer reaches the end, the slow pointer will be at the middle
        while pointer_end is not None and pointer_end.next is not None:
            # Move the pointers forward
            pointer_half = pointer_half.next
            pointer_end = pointer_end.next.next
        # Return the middle node, which is where the slow pointer is
        return pointer_half
