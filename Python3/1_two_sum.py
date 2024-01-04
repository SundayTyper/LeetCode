"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

### Psudo logic

# for each item in array
# take target and subtract item
# check if answer is in array
# return index of item and answer

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        output = []
        temp = nums.copy()

        for i in nums:
            answer = target - i
            temp.pop(0) # remove tested items to reduce computational load. Resolve error case of target = 2i

            if answer in temp:
                start = nums.index(i)
                end = nums.index(answer,start + 1) #start searching from occurance 1 to avoid duplicate indexes
                output.append(start)
                output.append(end)

                return output

        return "No solution found"