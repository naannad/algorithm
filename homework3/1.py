# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        vals = []
        cur_vertex = head
        while cur_vertex is not None:
            vals.append(cur_vertex.val)
            cur_vertex = cur_vertex.next
        return vals == vals[::-1]
