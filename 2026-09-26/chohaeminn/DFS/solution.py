import sys
input = sys.stdin.readline


def solution(numbers, target):
    def dfs (idx, current_sum):
        if idx == len(numbers):
            if current_sum == target:
                return 1
            return 0

        plus = dfs(idx +1, current_sum + numbers[idx])
        minus = dfs(idx +1, current_sum - numbers[idx])

        return plus + minus

    return dfs(0,0)

numbers_input = input().strip().lstrip("\ufeff").strip("[]")
numbers = list(map(int, numbers_input.split(",")))
target = int(input())
print(solution(numbers, target))
