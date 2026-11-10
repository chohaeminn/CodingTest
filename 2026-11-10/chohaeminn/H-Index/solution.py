def solution(citations):
    citations.sort(reverse=True)
    for i, citation in enumerate(citations):
        if citation < i + 1:
            return i  # <- 이 i는 for문 내부이므로 사용 가능!

    # for문이 다 끝나고 밖으로 나오면
    # i라는 변수는 사라져서 더 이상 존재하지 않습니다!
    return i  # ❌ NameError: name 'i' is not defined 에러 발생!