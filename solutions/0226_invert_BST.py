# Define the structure for a binary tree node
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val      # Value of the node
        self.left = left    # Left child pointer
        self.right = right  # Right child pointer

# Recursive approach to invert a binary search tree
class SolutionRecursive(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        # Base case: if the current node is None, return to the previous call
        if root is None:
            return None
        # First go to the left and right subtrees recursively until reaching the leaf nodes
        # This will return None when reaching the end of a branch
        self.invertTree(root.left)
        self.invertTree(root.right)
        # Then after reaching the leaf nodes, swap the left and right children of each node
        # For leaf nodes, this will just swap two None values
        # For non-leaf nodes, this will swap the actual child nodes
        temp = root.left
        root.left = root.right
        root.right = temp
        # Finally, return the current root
        # Only needed for the initial call to return the new root of the inverted tree
        # NOTE: This is a classic post-order traversal where we process the current node after its children
        return root

# Iterative approach to invert a binary search tree using a queue
from collections import deque

class SolutionIterative(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        # If the tree is empty, return None
        if root is None:
            return None
        # Initialize a queue for level-order traversal
        node_queue = deque()
        # Start with the root node
        node_queue.append(root)

        # Process nodes in the queue until it's empty
        while node_queue:
            # Dequeue the front node
            current_node = node_queue.popleft()
            # Swap its left and right children
            temp = current_node.left
            current_node.left = current_node.right
            current_node.right = temp
            # Enqueue the non-null children to continue the process
            # NOTE: This is level-order traversal (BFS) where we process nodes level by level
            if current_node.left is not None:
                node_queue.append(current_node.left)
            if current_node.right is not None:
                node_queue.append(current_node.right)
        # Finally, return the root of the inverted tree
        return root
