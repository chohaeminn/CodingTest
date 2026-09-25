import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().strip())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
house_count = 0


def dfs(y, x):
    global house_count

    visited[y][x] = True
    house_count += 1

    for dy, dx in directions:
        ny = y + dy
        nx = x + dx

        if 0 <= ny < n and 0 <= nx < n:
            if graph[ny][nx] == 1 and not visited[ny][nx]:
                dfs(ny, nx)


complex_sizes = []

for y in range(n):
    for x in range(n):
        if graph[y][x] == 1 and not visited[y][x]:
            house_count = 0
            dfs(y, x)
            complex_sizes.append(house_count)


complex_sizes.sort()

print(len(complex_sizes))

for size in complex_sizes:
    print(size)
