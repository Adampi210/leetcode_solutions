# Given a binary tree, determine if it is height-balanced.

# Key ideas:
# A height-balanced binary tree is defined as a binary tree in which
# the depth of the two subtrees of every node never differs by more than one.
# It's easy to get a height of each subtree using recursion.
# The challenge is to check the balance condition at each node efficiently.
# To solve this: combine height calculation and balance checking in one recursive function.
# If we find any subtree that is unbalanced, we propagate that information up
# (using -1 as a sentinel value for unbalanced).
# Otherwise, we return the height of the subtree.
# Which is 1 + max height of left and right subtrees.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    # Main function to check if the tree is balanced
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        # Call the helper function and check if it returns -1 (unbalanced) or not
        return self.checkHeightBalance(root) != -1

    # Helper function to check height and balance
    def checkHeightBalance(self, root):
        # Base case: an empty tree is balanced and has height 0
        if root is None:
            return 0
        # Recursively get the height of left and right subtrees
        left_height = self.checkHeightBalance(root.left)
        right_height = self.checkHeightBalance(root.right)
        # If either subtree is unbalanced, propagate -1 upwards
        if left_height == -1 or right_height == -1:
            return -1
        # If the current node is unbalanced, return -1
        # The current node is unbalanced if the height difference 
        # of its subtrees is more than 1
        if left_height - right_height < -1 or left_height - right_height > 1:
            return -1
        # If balanced, return the height of the subtree rooted at this node
        return 1 + max(left_height, right_height)
