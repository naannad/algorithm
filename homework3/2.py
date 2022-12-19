# Definition for singly-linked list.
#class ListNode:
#    def __init__(self, val=0, next=None):
#        self.val = val
#        self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        res = 0 # счет начинаем с нуля

        while head:
            res = res * 2 + head.val # берем значение умножаем его на два, прибавляем значение след. элмемента итд
            head = head.next # меняем знаение head, чтобы на каждой след. итерации, значение менялось на след.

        return res


# Просто перебираем наш связнный список, преобразовывая его в десятичную систему
# Берем значение умножаем его на два, прибавляем значение след элмемента итд
# Сложность равна О(N)
