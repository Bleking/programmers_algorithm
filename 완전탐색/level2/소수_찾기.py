# 프로그래머스 완전탐색 level 2 소수 찾기

from itertools import permutations

def solution(numbers):
    answer = []
    for n in range(1, len(numbers) + 1):
        perm = permutations(numbers, n)
        
        for p in perm:
            num = ''.join(p)
            
            if isPrime(int(num)):
                answer.append(int(num))
                
    return len(set(answer))


def isPrime(number):
    if number <= 1:
        return False

  # 에라스토테네스의 체 방식 이
    for i in range(2, number):
        if number % i == 0:
            return False

    return True
