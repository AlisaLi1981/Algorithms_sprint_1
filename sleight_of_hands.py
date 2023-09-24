# ID 91188691

def get_score(max_bottoms, matrix):
    numbers = '123456789' # Цифры, которые могут быть изображны на клавише.
    score = 0 # Переменная для сохранения счета. 
    for number in numbers:
        # Проверяем количество вхождений текущей цифры в строку matrix (клавиатуры).
        count = matrix.count(number)
        # Проверяем, что количество вхождений находится в нужном диапазоне.
        if max_bottoms * 2 >= count > 0:
            score += 1 # При выполнении условия увеличиваем счетчик.
    return score

if __name__ == '__main__':
    max_bottoms = int(input())
    matrix = f'{input()}{input()}{input()}{input()}'
    result = get_score(max_bottoms, matrix)
    print(result)

# Можно записать немного короче с помощью list comprehension и функции sum():
# def get_score(max_bottoms, matrix):
#    numbers = '123456789'
#    result = sum(
#        max_bottoms * 2 >= matrix.count(number) > 0 for number in numbers)
#    return result
#
#
# if __name__ == '__main__':
#    print(get_score(
#        int(input()), f'{input()}{input()}{input()}{input()}'))
