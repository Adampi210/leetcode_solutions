# Given the head of a singly linked list, 
# reverse the list, and return the reversed list.

# Key ideas:
# Use recursion to reverse the linked list.
# Base case: if the list is empty or has one node, return head.
# Recursive case: First note that we have to always propagate the new head
# Since that's the only way to get the new head back up the call stack.
# Now to reverse the list
# First, NOTE: head.next still points to the next node in the original list
# So head.next.next is the next node's next pointer in the original list.
# So setting head.next.next = head means the next node now points back to head
# (current node). As such this reverses the link between head and head.next.
# However, now there is a cycle since head still points to head.next.
# So we need to set head.next = None to break that cycle.
# We keep doing this recursively until we reach the starting node
# And since we always propagate the new head back up,
# we get the fully reversed list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Edge case: if the list is empty return None
        if head is None:
            return None
        # Base case: if there's only one node (left), return head
        if head.next is None:
            return head
        # Recursive case: reverse the rest of the list
        # First, go deeper into the list 
        # and get the new head of the list when going back up
        list_head = self.reverseList(head.next)
        # Now reverse the link between head and head.next
        # First, make head.next point back to head (to reverse the link)
        head.next.next = head
        # Then break the cycle by setting head.next to None
        head.next = None
        # Finally, return the new head of the reversed list
        return list_head
