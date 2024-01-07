"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.
""" 

class Solution:
    def isValid(self, s: str) -> bool:
        
        # fail if string is odd number length
        # create answer stack to track open/closed brackets
        # define dictionary pairs for closing brackets - this lets me check brackets are closing in order
        # track brackets open, fail if first bracket is a close
        # finally confirm open bracket list is empty

        if len(s)%2 == 1:
            return False

        openStack = []

        closingBrackets = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }
        
        for char in s:

            if char in '([{':
                openStack.append(char)

            elif len(openStack) == 0:
                return False

            elif closingBrackets[char] != openStack[-1]:
                return False

            else:
                openStack.pop()

        if len(openStack) == 0:
            return True
        else:
            return False

