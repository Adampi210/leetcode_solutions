# Given the head of a linked list,
# remove the nth node from the end
# of the list and return its head

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Simple: Keep track of 2 pointers shifted by n, then remove the n-th node from the back 
# when the first pointer reaches the end of the list
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        Removes the Nth node from the end of the list and returns the head of the modified list.
        """
        # Create a pointer to the head
        ptr_head = ListNode(0)
        ptr_head.next = head

        # Initialize two pointers to head pointer
        ptr_0 = ptr_head
        ptr_1 = ptr_head

        # Move first ahead by n + 1 steps to create the gap
        for _ in range(n + 1):
            if ptr_0 is not None:
                ptr_0 = ptr_0.next
            else:
                # If n is larger than the length of the list, return the head as is
                return ptr_head

        # Move both pointers until first reaches the end
        while ptr_0 is not None:
            ptr_0 = ptr_0.next
            ptr_1 = ptr_1.next

        # ptr_1.next is the node to remove
        node_to_remove = ptr_1.next
        ptr_1.next = ptr_1.next.next if ptr_1.next else None

        # Optional: Clear the removed node's next pointer
        if node_to_remove:
            node_to_remove.next = None

        # Return the new head
        return ptr_head.next
