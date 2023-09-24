# ID 91221206

def get_score(max_bottoms, matrix):
    numbers = '123456789'
    score = 0 
    for number in numbers:        
        count = matrix.count(number)        
        if max_bottoms * 2 >= count > 0:
            score += 1
    return score

if __name__ == '__main__':
    max_bottoms = int(input())
    matrix = f'{input()}{input()}{input()}{input()}'
    print(get_score(max_bottoms, matrix))
  
