""" 
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # make empty lsit
        # make node tracker
        # take item 1 on each list and compare
        # smaller number adds to answer list
        # if equal add both
        # move selected list to next item 
        # move node tracker +1 
        # repeat
        # if a list empty, add other lsit

        solutionList = ListNode()
        solutionchar = solutionList

        while list1 and list2:
            if list1.val <= list2.val:
                solutionchar.next = list1
                list1 = list1.next
            else:
                solutionchar.next = list2
                list2 = list2.next
            solutionchar = solutionchar.next

        solutionchar.next = list1 or list2

        return solutionList.next

