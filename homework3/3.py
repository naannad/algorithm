# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q, ans = [root], []
        while len(q): # пока сущ "очередь"
            qlen, row = len(q), 0
            for i in range(qlen):
                curr = q.pop(0)
                row += curr.val
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            ans.append(row/qlen)
        return ans


# Здесь идет речь об уровнях в двоичном дереве, поэтому используем подход поиска в ширину, а затем среднее значение,
# буду брать каждую строку, суммировать значение строки, затем делить на длину строки (для ср значения),
# помещая каждое значение в массив