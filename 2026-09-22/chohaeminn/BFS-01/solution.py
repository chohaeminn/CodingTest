'''
- 그래프 탐색: 어떤 것들이 연속해서 이어질 떄 모두 확인하는 방법
    - Graph: Vertex(어떤 것) + Edge(이어지는 것)

- BFS 시간복잡도: O(V + E)
- 자료구조: Queue(선입선출)

문제: 어떤 도화지에 그림 그려져 있을 때 그 그림의 개수와 그 그림 중 넓이가 가장 넓은 것의 넓이를 출력해라
단 그림이란 것은 1로 연결된 것을 한 그림이라고 정의하자. 가로나 세로로 연결된 것은 연결이 된 것이고 대각선으로 연결이 된 것은 떨어진 그림이다. 그림의 넓이란 그림에 포함된 1의 개수이다.

입력: 
- 첫째 줄에 도화지의 세로 크기 N과 가로 크기 M이 주어진다. (1 ≤ N, M ≤ 500)
- 둘째 줄부터 N+1개의 줄에 그림의 정보가 주어진다. (단 그림의 정보는 0과 1이 공백을 두고 주어지며, 0은 색칠이 안된 부분, 1은 색칠이 된 부분을 의미한다)

출력: 첫째 줄에는 그림의 개수, 둘 째 줄에는 그 중 가장 넓은 그림의 넓이를 출력핼
(단 그림이 하나도 없는 경우에는 가장 넓은 그림의 넓이는 0이다.)

'''

'''
1. 아이디어
- 2중 FOR ==> 그래프 값 1 && 방문 X -> BFS 시작
- BFS 돌면서 그림 개수 +1, 최대값 갱신

2. 시간 복잡도

- V = N * M(500*500), E = 4 * V(4*500*500)
- O(V+E) = O(V + 4V) = O(5V) = O(V)
- V+E : 5 * 250000 = 100만 < 2억

3. 자료구조
- 그래프 전체 지도: INT P[501][501]
- 방문 : BOOL VISITED[501][501]
- Queue: BFS를 위한 Queue


'''

import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
chk = [[False] * m for _ in range(n)]

cnt = 0
maxv = 0

def bfs(x,y):
    q = deque([(x,y)])
    area = 1
    while q:
        x,y = q.popleft()
        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx,ny = x+dx,y+dy
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 1 and not chk[nx][ny]:
                q.append((nx,ny))
                chk[nx][ny] = True
                area += 1
    return area

for j in range(n):
    for k in range(m):
        if board[j][k] == 1 and not chk[j][k]:
            # BFS 시작, 그림 개수 +1, 최대값 갱신
            chk[j][k] = True
            cnt += 1
            maxv = max(maxv, bfs(j,k))

print(cnt)
print(maxv)
