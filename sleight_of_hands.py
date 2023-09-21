# ID 91006845

def get_score(max_bottoms, matrix, numbers='123456789'):
    return sum(
        max_bottoms * 2 >= matrix.count(number) > 0 for number in numbers)


if __name__ == '__main__':
    print(get_score(
        int(input()), f'{input()}{input()}{input()}{input()}'))
