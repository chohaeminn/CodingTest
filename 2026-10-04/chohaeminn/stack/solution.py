def solution(prices):
    answer = [0] * len(prices)
    stack = []  # 아직 가격이 떨어지지 않은 인덱스들을 저장

    for i, price in enumerate(prices):
        # 1. 현재 가격이 이전 가격보다 떨어졌다면, 스택에서 꺼내며 기간 계산
        while stack and prices[stack[-1]] > price:
            j = stack.pop()
            answer[j] = i - j  # (현재 인덱스) - (가격이 떨어진 시점의 인덱스)

        # 2. 현재 인덱스를 스택에 추가
        stack.append(i)

    # 3. 끝까지 가격이 떨어지지 않은 원소들 처리
    while stack:
        j = stack.pop()
        answer[j] = len(prices) - 1 - j

    return answer