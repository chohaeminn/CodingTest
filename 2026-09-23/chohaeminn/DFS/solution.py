'''
bfs, dfs

dfs: 깊이 우선 탐색: 자식이 우선순위인 자료구조, stack이라는 자료구조와 맞다

이번 시간에는 stack이 아니라 재귀함수를 써서 쓸거다.

그래프 탐색: bfs가 더 낫다. 코드가 더 깔끔하다

bfs는 재귀함수를 쓰기 위해 한다 -> 백트래킹


재귀함수
	자기자신을 다시 호출하는 함수
	재귀하무가 종료되는 시점 반드시 명시
	재귀함수의 깊이가 너무 깊어지면 stack overflow
	dfs,백트래킹 사용
아이디어
	시작점에 연결된 vertex 찾기
	연결된 vertex를 계속해서 찾음 (끝날 때까지)
	더 이상 연결된 vertex 없을 경우 다음
시간 복잡도?
	알고리즘이 얼마나 오래 걸리는지
	dfs: o(v+e)
자료구조
	검색할 그래프: 2차원 배열
	방문여부 확인: 2차원 배열 (재방문 금지)

백준 2667

1.아이디어
- 2중 for문, 값 1 && 방문 x -> dfs
- dfs를 통해 찾은 값을 저장 후 정렬해서 출력

2. 시간 복잡도
- dfs o(v+e)
- v,e : n^2, 4n^2
- v+e: 5n^2 ~= 523 >> 가능

3. 자료구조
- 그래프 저장:  int[][]
- 방문 여부: bool[][]
- 결과값: int[]

'''

import sys
input  = sys.stdin.readline

N= int(input())
map = [list (map(int, input().strip())) for _ in range(N)]
chk = [[False] * N for _ in range(N)]
result = []
each = 0

dy = [0,1,0,-1]
dx = [1,0,-1,0]

def dfs(y,x):
global each
	each += 1
	for k in range(4):
		ny = y + dy[k]
		nx = x + dx[k]
		if 0<=ny<N and 0<nx<N:
			if map[ny][nx] == 1 and chk[ny][nx] == False:
				chk[ny][nx] = True
				dfs(ny, nx)	

for  j in range(N):
	for i in range (N):
		if map[j][i] ==1 and chk[j][i] == False
		chk[j][i] = True
		#방문 체크 표시
		#DFS로 크기 구하기
		# 크기를 결과 리스트에 넣기
		
		each = 0
		dfs(j,i)
		result.append(each)
		
result.sort()
print(len()result)

for i in result:
	print(i)


