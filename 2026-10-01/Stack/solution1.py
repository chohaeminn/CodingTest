def solution(s):
    stack = []
    
    for char in s:
        if char == '(':
            stack.append('(')
        else:  # char == ')'
            # 닫는 괄호가 나왔는데 스택이 비어있다면 짝이 안 맞음
            if not stack:
                return False
            stack.pop()
            
    # 순회를 다 마쳤는데 스택에 괄호가 남아있으면 False, 비어있으면 True
    return len(stack) == 0