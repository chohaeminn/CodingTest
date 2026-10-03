from collections import deque


def solution(priorities, location):
  # (우선순위, 원래 인덱스) 형태로 큐 생성
  queue = deque([(p, i) for i, p in enumerate(priorities)])
  answer = 0

  while queue:
    current = queue.popleft()

    if any(current[0] < q[0] for q in queue):
      queue.append(current)  
    else:
      answer += 1  
      if current[1] == location: 
        return answer