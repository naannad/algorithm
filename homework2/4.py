#Сложность O(N)
# Объяснение в задаче очень подробное, поэтому задача понятна
# Решается полность по условиям из задачи


class Solution:
    def maxProfit(prices):
        counter = 0 # счетчик для общей прибыли

        for i in range(1, len(prices)): #проходимся со второго элемента по всему списку
            if prices[i] - prices[i - 1] > 0: # если разность чисел больше 0(если прибыль в плюс)
                counter += (prices[i] - prices[i - 1]) # заносим в счетчик

        return counter


print(Solution.maxProfit([1,2,3,4,5]))