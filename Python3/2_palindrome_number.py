""".
Given an integer x, return true if x is a palindrome, and false otherwise.
"""

### Psudo logic

# Convert to string, reverse and compare

class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        #convert to string and reverse
        xString = str(x)
        revxString = str(xString [::-1])

        #compare and return
        if xString != revxString:
            return False
        else:
            return True