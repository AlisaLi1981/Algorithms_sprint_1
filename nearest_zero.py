# ID 91002906

def count_zero_distance(street_numbers):
    zeros = [position for position, element in enumerate(
        street_numbers) if element == '0']
    street_length = len(street_numbers)
    result = [0] * street_length
    first, last = zeros[0], zeros[-1]
    result[:first] = [first - position for position in range(first)]
    for left, right in zip(zeros, zeros[1:]):
        result[left + 1:right] = [
            min(position - left, right - position) for position in range(
                left + 1, right)]
    result[last + 1:] = [
        position - last for position in range(last + 1, street_length)]
    return result


if __name__ == '__main__':
    input()
    print(*count_zero_distance(input().split()))
