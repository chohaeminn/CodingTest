'''
1. 조건, 제한 사항:
    - 조건: 숫자 반복되면 제거 -> stack 사용
    - 제한: arr < 1,000,000 -> O(n) 시간 복잡도 필요, 2중 for문 사용 X
2. 스택 손으로 써보기
    - i, num -> enumnerate 사용 or
    - num[-1]과 num 비교
3. 특이 case
    - [1,2,3,4,5] -> [1,2,3,4,5] (중복 없음)
    - [1,1,1,1,1] -> [1] (중복 모두 제거)
    - [1] -> [1] (중복 없음)
4. 놓친 부분
    - 비어있을 때는 무조건 append -> if not answer
5. 복잡도
    - 시간 복잡도: O(n)-> for문 1번만 사용
    - 공간 복잡도: O(n)
'''
answer = []

def solution(arr):
    for num in arr:
        if not answer or answer[-1] != num:
            answer.append(num)
    return answer