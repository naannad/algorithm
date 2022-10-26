# Делаю перебор каждого камня с драгоценным
# Сравнивая, проверяю, совпадает ли камень с драгоценным,
# Если да, добавляю в счетчик
# Сложность равна О(N)

def numJewelsInStones(jewels: str, stones: str):
    counter = 0 # количество совпадений камней и драгоценных
    jewels = list(jewels) # делаем из строки список, чтобы сравнивать каждый элемент
    for i in stones: # проходимся по всем элементам камня
        if i in jewels: # если в драгоценных есть камень
            counter += 1 # добавляем сопадение в счетчик
    return counter # возвращаю счетчик
print(numJewelsInStones("aA", "aAAbbbb"))