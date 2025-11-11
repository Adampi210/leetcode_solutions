# Given two binary strings a and b, return their sum as a binary string.

# KEY IDEA: Simulate binary addition from the least significant bit to the most significant bit,
# keeping track of carry, and build the result string in reverse order.
# NOTE: Solve problem in reverse - important idea!!!
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # Ensure a is the longer string
        if len(b) < len(a):
            # If not, run the function with swapped arguments
            return self.addBinary(b, a)
        # Initialize variables
        carry = 0   # Carry for binary addition
        i = -1      # Index to traverse the strings from the end
        output = [] # List to store the result bits
        # Add bits from both strings while both have bits left
        while len(a) + i >= 0:
            # Add corresponding bits and carry
            r = carry
            r += 1 if a[i] == "1" else 0
            r += 1 if b[i] == "1" else 0
            # Append the result bit (r % 2) to output
            output.append(str(r % 2))
            # Update carry (r // 2)
            carry = 0 if r < 2 else 1
            # Move to the next bit
            i -= 1
        # If a is exhausted, continue adding bits from b and carry
        while len(b) + i >= 0:
            # Add corresponding bit and carry
            r = carry
            r += 1 if b[i] == "1" else 0
            output.append(str(r % 2))
            # Update carry
            carry = 0 if r < 2 else 1
            # Move to the next bit
            i -= 1
        # If there's a remaining carry, append it
        if carry:
            output.append("1")
        # The output list is in reverse order, so reverse it and join to form the final string
        return "".join(output[::-1]) 
