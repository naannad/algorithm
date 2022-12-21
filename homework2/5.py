class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [1] * n
        
        for i in range(1, n):       
            if prices[i - 1] - prices[i] == 1:
                dp[i] = dp[i - 1] + 1  # Находим длины последовательностей, каждый следующий элемент которог будет на 1 меньше предыдущего
        
        return sum(dp) # Для объединения всех вариантов подпоследовательностей нам надо сложить длины получившихся последовательностей

# Сложность - O(n)
