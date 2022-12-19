# Definition for singly-linked list.
#class ListNode:
#    def __init__(self, val=0, next=None):
#        self.val = val
#        self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        def getDecimalValue(self, head: ListNode) -> int:
        h_list = head #переменная равная тесткейсу
        score = '' #вводим переменную куда будем записывать данные из списка в строке
        while h_list:
            score += str(h_list.val) #прибавляем каждый итый элемент строкой в переменную для записи
            h_list = h_list.next
        return(int(score,2)) #возвращаем наше число в десятичной СС
