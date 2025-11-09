# Implement a first in first out (FIFO) queue using only two stacks. 
# The implemented queue should support all the functions of a normal queue
# (push, peek, pop, and empty).

# Implement the MyQueue class:
# void push(int x) Pushes element x to the back of the queue.
# int pop() Removes the element from the front of the queue and returns it.
# int peek() Returns the element at the front of the queue.
# boolean empty() Returns true if the queue is empty, false otherwise.

# Notes:
# You must use only standard operations of a stack, 
#   - only push to top, peek/pop from top, size, and is empty are valid.
#   - Depending on your language, the stack may not be supported natively. Can use a list 

# Key ideas: Use 2 stacks, one for input and one for output.
# NOTE: Amortized O(1) time for each operation.
# NOTE: First note that if we pop all elements from one stack and put it onto the other, we reverse the order
# So that way we can get the first element by popping from the second stack.
# NOTE: Doing that every time is inefficient
# NOTE: ONLY transfer elements from in_stack to out_stack when out_stack is empty.
# This way each element is moved at most twice (once in, once out).
# Time complexity: O(1) amortized for each operation.
# (pushing onto in_stack is O(1), popping from out_stack is O(1), 
# only O(n) when transferring elements, but that happens only once per n operations)

class MyQueue(object):
    def __init__(self):
        # Initialize two stacks, in_stack and out_stack
        self.in_stack = []  # Stack to handle incoming elements
        self.out_stack = [] # Stack to handle outgoing elements
        return None

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        # Push element x onto in_stack (simple O(1) operation)
        self.in_stack.append(x)
        return None

    def pop(self):
        """
        :rtype: int
        """
        # If out_stack is empty, transfer all elements from in_stack to out_stack
        if len(self.out_stack) == 0:
            # Keep popping from in_stack and pushing onto out_stack
            # Until in_stack is empty
            while len(self.in_stack) > 0:
                temp = self.in_stack.pop()
                self.out_stack.append(temp)
        # Pop the top element from out_stack, which is the front of the queue
        first_val = self.out_stack.pop()
        return first_val

    def peek(self):
        """
        :rtype: int
        """
        # If out_stack is empty, transfer all elements from in_stack to out_stack
        # This ensures the front of the queue is on top of out_stack
        if len(self.out_stack) == 0:
            while len(self.in_stack) > 0:
                temp = self.in_stack.pop()
                self.out_stack.append(temp)
        # The top element of out_stack is the front of the queue
        # NOTE: Most of the time, this is O(1) since we only transfer when out_stack is empty
        first_val = self.out_stack[-1]
        return first_val

    def empty(self):
        """
        :rtype: bool
        """
        # The queue is empty if both in_stack and out_stack are empty
        return len(self.in_stack) + len(self.out_stack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
