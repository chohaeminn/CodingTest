from collections import defaultdict

def solution(clothes):  # 파라미터 이름을 일치시킴
    clothes_map = defaultdict(int)
    
    for name, kind in clothes:
        clothes_map[kind] += 1  # 괄호 대신 대괄호 사용 ([kind])
        
    answer = 1
    
    for kind in clothes_map:
        answer *= (clothes_map[kind] + 1)  # 경우의 수를 누적해야 하므로 곱하기(*=) 사용
        
    return answer - 1