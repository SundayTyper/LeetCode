"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""

### Psudo logic
# loop through the first letter of all strings
# compare letter
# if the same then procceed 
# if different break and return answer/fail message
# find shortest word to reduce loops - order by lengths to avoid missing a string

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        response = ""
        shortestWord = min(strs, key=len)
        strs = sorted(strs, key=len)
        
        for pos in range(len(shortestWord)):
            char = shortestWord[pos]

            for word in strs[1:]:
                char2 = word[pos]
                if char != char2:
                    return response
            response = response + char
        return response