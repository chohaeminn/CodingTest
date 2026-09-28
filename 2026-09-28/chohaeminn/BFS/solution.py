def solution(n, computers):
    answer = 0
    visited = [False] * n

    def dfs(current):
        visited[current] = True
        for j in range(n):
            if computers[current][j] == 1 and not visited[j]:
                dfs(j)

        for i in range(n):
            if not visited[i]:
                dfs[i]
            answer += 1
    return answer

    