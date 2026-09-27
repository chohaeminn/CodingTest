from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    # 이동할 네 방향 정의 (상, 하, 좌, 우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue = deque([(0, 0)])
    
    while queue:
        x, y = queue.popleft()
        
        # 현재 위치에서 네 방향으로 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 맵을 벗어나지 않고
            if 0 <= nx < n and 0 <= ny < m:
                # 벽이 아니고 처음 방문하는 칸인 경우 (값이 1인 경우)
                if maps[nx][ny] == 1:
                    # 최단 거리 갱신 (이전 거리 + 1)
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx, ny))
                    
    # 상대 팀 진영(우측 하단)의 값을 확인
    answer = maps[n-1][m-1]
    
    # 값이 여전히 1이라면 도달하지 못한 것임 (-1 리턴)
    return answer if answer > 1 else -1