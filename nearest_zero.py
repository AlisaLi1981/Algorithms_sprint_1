# ID 91251601

def count_zero_distance(n, street_numbers):
    zero_distance = [0] * n
    distance = 0
    first_index = None

    for i, number in enumerate(street_numbers):
        if number == 0:
            if first_index is not None:
                for j in range(first_index, i):
                    zero_distance[j] = min(j - first_index, i - j)
            else:
                for j in range(i):
                    zero_distance[j] = i - j
            first_index = i
            distance = 0
        else:
            distance += 1
            zero_distance[i] = distance

    return zero_distance

if __name__ == '__main__':
    n = int(input())
    street_numbers = [int(x) for x in input().split()]
    print(*count_zero_distance(n, street_numbers))
