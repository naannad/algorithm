#Сложность O(N)
# Задача так же полность решается по условиям задачи (математически)


class Solution:
    def getDescentPeriods(prices):

        result = 0 # счетчик
        l = 0 # счетчик для отрезков ( например, [3], [2], [1], [3,2,1])

        for i in range(len(prices)): # проходимся по каждому элементу
            l += 1 # добовляем в список хотя бы один отрезок
            if (i + 1 == len(prices)) or (prices[i] - 1 != prices[i + 1]):
                result += l * (l + 1) // 2
                l = 0 # перезаписываем переменную для записи нового отрезка

        return result

print(Solution.getDescentPeriods([3,2,1,4]))