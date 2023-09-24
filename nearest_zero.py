# ID 91191536

def count_zero_distance(street_numbers):
    n = len(street_numbers)
    zero_distance = [0] * n  # Список расстояний доближайшего нуля

    nearest_zero = float('-inf') # Переменная для отслеживания индекса ближайшего нуля
    # Проход в цикле слева направо для получения расстояния до ближайшего нуля слева.
    for i in range(n):
        if street_numbers[i] == '0':
            nearest_zero = i # Если текущий элемент 0, обновляем переменную nearest_zero.
        zero_distance[i] = i - nearest_zero # Вычисление расстояния до ближайшего нуля слева.

    nearest_zero = float('inf') # Переменная для отслеживания индекса ближайшего нуля
    # Проход в цикле справа налево для получения расстояния до ближайшего нуля справа.
    for i in range(n - 1, -1, -1):
        if street_numbers[i] == '0':
            nearest_zero = i  # Если текущий элемент 0, обновляем переменную nearest_zero.
        zero_distance[i] = min(zero_distance[i], nearest_zero - i) # Вычисление расстояния до ближайшего нуля справа.

    return zero_distance

if __name__ == '__main__':
    input()
    print(*count_zero_distance(input().split()))

# Изначальный вариант и его модификации содержали вложеный цикл, из-за чего превышали лимит времени, хоть и решали задачу:
# def count_zero_distance(street_numbers):
#    zero_distance = []
#    zeros = []
#    n = len(street_numbers)
#
#    for position, number in enumerate(street_numbers):
#        if number == '0':
#            zeros.append(position)
#
#    for i in range(n):
#        min_distance = n
#        for j in zeros:
#            print(min_distance)
#            distance = abs(i - j)
#            if distance < min_distance:
#                min_distance = distance
#        zero_distance.append(min_distance)
#
#    return zero_distance

# if __name__ == '__main__':
#    input()
#    print(*count_zero_distance(input().split()))
