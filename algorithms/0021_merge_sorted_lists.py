# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. 
# The list should be made by splicing together the nodes 
# of the first two lists.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# For merging the sorted lists
def mergeTwoLists(list1, list2):
    """
    :type list1: Optional[ListNode]
    :type list2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    # If both lists are empty, return None
    if list1 is None and list2 is None:
        return None

    # Initialize new list and set a head to that list's head
    list_new = ListNode()
    ln_head = list_new

    # While either list1 or list2 is not empty 
    # add the smaller value to the new list
    while list1 or list2:
        # If list1 is empty, add list2's value to the new list
        if list1 is None:
            ln_temp = ListNode(list2.val, None)
            list_new.next = ln_temp
            list2 = list2.next
        # If list2 is empty, add list1's value to the new list
        elif list2 is None:
            ln_temp = ListNode(list1.val, None)
            list_new.next = ln_temp
            list1 = list1.next
        # If both lists are not empty, add the smaller value to the new list
        else:
            if list1.val <= list2.val:
                ln_temp = ListNode(list1.val, None)
                list_new.next = ln_temp
                list1 = list1.next
            else:
                ln_temp = ListNode(list2.val, None)
                list_new.next = ln_temp
                list2 = list2.next
        list_new = list_new.next
    # Return the head of the new list (need to use next to set it to the actual head)
    return ln_head.next
