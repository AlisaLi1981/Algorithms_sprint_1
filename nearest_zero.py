# ID 91235448

from typing import Optional


def count_zero_distance(n, street_numbers):
    zero_distance = [None] * n
    nearest_zero: Optional[int] = None

    for i, number in enumerate(street_numbers):
        if number == 0:
            nearest_zero = i
        if nearest_zero is not None:
            zero_distance[i] = i - nearest_zero

    nearest_zero = None
    for i, number in reversed(list(enumerate(street_numbers))):
        if number == 0:
            nearest_zero = i
        if nearest_zero is not None:
            if zero_distance[i] is None or nearest_zero - i < zero_distance[i]:
                zero_distance[i] = nearest_zero - i

    return zero_distance

if __name__ == '__main__':
    n = int(input())
    street_numbers = [int(x) for x in input().split()]
    print(*count_zero_distance(n, street_numbers))
