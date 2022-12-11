# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head):
        fast = head
        slow = head # оба указателя в начале

        # ищем середину
        while fast and fast.next: # мы будем продолжать идти, пока не будет либо на последнем узле, либо он достиг нуля
            fast = fast.next.next # обновляется дважды
            slow = slow.next

        # переворачиваем второую половину списка
        prev = None # предыдущий равен нулю
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        # проверка на палиндром
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True


# Решаю с помощью указателей first and slow. Нахожу середину списка
# Указатели начинаются с начала, таким образом first идет на два шага вперед,
# когда slow на один. Когда быстрый указатель достигает конца списка, медленный
# должен быть где то около середины. Затем переворачиваем вторую половину списка,
# для того, чтобы сравнить с первой и узнать палиндром ли это
# сложность О(1)