# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False


# Буду использовать быстрый и медленный указатель, быстрый делает 2 шага, медленный 1 шаг, следовательно,
# после нескольких итераций, если есть цикл, то указатели в итоге совпадут.