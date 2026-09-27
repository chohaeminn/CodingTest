from collections import deque
import sys

input = sys.stdin.readline

def solution():
    n, m = map(int, input().split())
    
    # 띄어쓰기로 구분된 맵을 입력받는 경우
    board = [list(map(int, input().split())) for _ in range(n)]
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue = deque([(0, 0)])
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == 1:
                    board[nx][ny] = board[x][y] + 1
                    queue.append((nx, ny))
                    
    answer = board[n-1][m-1]
    return answer if answer > 1 else -1

if __name__ == "__main__":
    print(solution())