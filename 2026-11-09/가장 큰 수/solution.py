def solution(numbers):
    # 1. numbers의 원소들을 문자열로 변환
    numbers = list(map(str, numbers))
    
    # 2. x * 3 기준으로 내림차순 정렬 (lambda 스펠링 수정)
    numbers.sort(key=lambda x: x * 3, reverse=True)
    
    # 3. 정렬된 문자열을 하나로 연결
    answer = ''.join(numbers)
    
    # 4. '000' 형태의 예외 처리 후 반환
    return '0' if answer[0] == '0' else answer