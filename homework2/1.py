# Первое, что пришло в голову это метод перебора и поиск единиц.
# Сложность O(N**2)


class Solution:
    def countSquares(matrix) -> int:
        counter = 0 # счетчик для квадратов
        for i in range(len(matrix)): # проходимся по списку списков
            for j in range(len(matrix[0])): # проходимся по каждому элементу списка списков
                if matrix[i][j] == 1 and i > 0 and j > 0: # если элемент матрицы явл единицой и след выполняются
                    matrix[i][j] = min(matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1]) + 1

                counter += matrix[i][j] # если условия нам не подходят +

        return counter

    print(countSquares([
        [0, 1, 1, 1],
        [1, 1, 1, 1],
        [0, 1, 1, 1]
    ]))