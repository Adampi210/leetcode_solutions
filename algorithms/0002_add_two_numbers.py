# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
# This was the initial solution, which is not optimal (but is still O(N) time complexity)
# Beats around 21% of submissions
def addTwoNumbers_slower_but_still_ON(l1, l2):
    """
    :type l1: Optional[ListNode]
    :type l2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    l1_head = l1
    num_1 = 0
    multip_10 = 1
    # Get the number from the first linked list
    while l1_head != None:
        num_1 += l1_head.val * multip_10
        l1_head = l1_head.next
        multip_10 *= 10

    l2_head = l2
    num_2 = 0
    multip_10 = 1
    # Get the number from the second linked list
    while l2_head != None:
        num_2 += l2_head.val * multip_10
        l2_head = l2_head.next
        multip_10 *= 10

    # Add the two numbers
    num_sum = num_1 + num_2
    l_sum = ListNode(num_sum % 10, None)
    num_sum //= 10
    l_sum_head = l_sum
    while num_sum > 0:
        a = ListNode(num_sum % 10, None)
        l_sum_head.next = a
        l_sum_head = l_sum_head.next
        num_sum //= 10
    return l_sum

# This is the more optimal solution, which is O(N) time complexity
# Beats around 91% of submissions
def addTwoNumbers_faster(l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        l_sum = ListNode()
        l_sum_head = l_sum
        carry = 0
        # Keep going until both linked lists are empty and there is no carry
        while l1 or l2 or carry:
            total = carry
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            # If the total is greater than 9, we need to carry over the 1
            if total > 9:
                carry = 1
                total %= 10
            # Otherwise, we don't need to carry over
            else:
                carry = 0
            a = ListNode(total, None)
            l_sum.next = a
            l_sum = l_sum.next
        return l_sum_head.next
        

        