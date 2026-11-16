from itertools import permutations

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0
            return False
    return True

def solution(numbers):
    candidates = set()

    for length in range(1, len(numbers) + 1):
        for p in permutations(numbers, length):
            num = int("".join(p))
            candidates.add(num)

    answer = sum(1 for num in candidates if is_prime(num))
    return answer
