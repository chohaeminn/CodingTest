import heapq

def solution(scoville, k):
    heapq.heapify(scoville)
    answer = 0

    while scoville[0] < k:
        if len(scoville) < 2:
            return -1

        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)

        new_scoville = first + (second * 2)
        heapq.heappush(scoville, new_scoville)

        answer += 1

    return answer