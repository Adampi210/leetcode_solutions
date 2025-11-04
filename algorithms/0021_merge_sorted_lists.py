# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list.
# The list should be made by splicing together the nodes
# of the first two lists.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Initialize pointers for both lists
        p1 = list1
        p2 = list2

        # Dummy node to help with the merged list
        p_dummy = ListNode()
        # Pointer to the current node in the merged list
        p_current = p_dummy

        # Traverse both lists and append the smaller node to the merged list
        while p1 and p2:
            # Compare values and append the smaller one
            if p1.val < p2.val:
                # Append p1 to merged list
                p_current.next = p1
                # Move p1 to the next node
                p1 = p1.next
            else:
                # Append p2 to merged list
                p_current.next = p2
                # Move p2 to the next node
                p2 = p2.next
            # Move the current pointer to the newly added node
            p_current = p_current.next

        # If there are remaining nodes in either list, append them
        if p1:
            p_current.next = p1
        elif p2:
            p_current.next = p2

        # Return the merged list, which starts after the dummy node
        return p_dummy.next
