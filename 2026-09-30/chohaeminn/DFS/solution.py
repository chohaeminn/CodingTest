'''
1. 문제 유형:
       - 그래프 탐색 / 오일러 경로(Eulerian Path) - 스택을 활용한 반복문 DFS
       
    2. 유형을 떠올리는 기준:
       - "모든 항공권(간선)을 빠짐없이 정확히 한 번씩 모두 사용해야 한다"는 조건이 주어질 때
       -> 오일러
       - 가능한 경로가 여러 개일 때 알파벳 순서가 앞서는 경로를 먼저 찾아야 할 때
       
    3. 풀이 팁 & 주의사항:
       - 파이썬은 기본 재귀 깊이 제한(약 1,000번)이 있으므로, 티켓 수가 최대 10,000개인 이 문제에서
         재귀 DFS를 쓰면 'RecursionError'가 발생합니다. 반드시 'while 반복문 + 스택'으로 구현해야 합니다.
       - 알파벳 순서 정렬 트릭: 스택의 pop()은 가장 마지막 원소를 꺼내므로(LIFO), 
         목적지 리스트를 미리 내림차순(reverse=True)으로 정렬해 두어야 pop할 때 알파벳 순(오름차순)으로 나옵니다.
         
    4. 자료구조 선택:
       - defaultdict(list): 존재하지 않는 출발지 키에 접근할 때 KeyError를 방지하고, 
         바로 .append()를 쓸 수 있어 코드가 깔끔해집니다.
       - list (stack): 현재 위치를 추적(`stack[-1]`)하고 막다른 길에서 되돌아오는(백트래킹) 용도.
       - list (path): 막다른 길에 부딪힌 공항부터 거꾸로 기록하여 최종 경로를 완성하는 용도.
       
    5. 복잡도:
       - 시간 복잡도: O(E log E) (여기서 E는 티켓 개수 / 정렬 과정이 병목 구간)
       - 공간 복잡도: O(E) (인접 리스트와 스택/경로 리스트 저장 비용)
'''

from collections import defaultdict

def solution(tickets):
    routes = defaultdict(list)

    for start, end in sorted(tickets, reverse = True):
        routes[start].append(end)

    stack = ['ICN']
    path = []

    while stack:
        current = stack[-1]

        if routes[current]:
            stack.append(routes[current].pop())
        else:
            path.append(stack.pop())

    return path[::-1]