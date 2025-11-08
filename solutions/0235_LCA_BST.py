# Given a binary search tree (BST), 
# find the lowest common ancestor (LCA) node of two given nodes in the BST.

# According to the definition of LCA on Wikipedia: 
# “The lowest common ancestor is defined between two 
# nodes p and q as the lowest node in T that has both p and q as descendants 
# (where we allow a node to be a descendant of itself).”

# Key insight: In a BST, for any node:
# - All values in the left subtree are less than the node's value
# - All values in the right subtree are greater than the node's value
# Therefore, we can determine the position of p and q relative to the current node
# If both p and q are less than the current node, LCA must be in the left subtree
# If both p and q are greater than the current node, LCA must be in the right subtree
# If p is on one side and q is on the other, we've found the LCA
# (because then either one of the nodes is the current node
# or the nodes are in different subtrees of the current node)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # Initialize the current node as the root
        current_node = root
        # Traverse the tree
        while True:
            # Decide the direction to move based on the values of p and q
            if current_node.val < p.val and current_node.val < q.val:
                # Both p and q are greater than current_node
                # Move to the right subtree
                current_node = current_node.right
            elif current_node.val > p.val and current_node.val > q.val:
                # Both p and q are less than current_node
                # Move to the left subtree
                current_node = current_node.left
            else:
                # We have found the split point
                # This is the lowest common ancestor
                # This is either because one of p or q is the current node
                # Or p and q are in different subtrees of current_node
                break
        # Return the lowest common ancestor node
        return current_node
