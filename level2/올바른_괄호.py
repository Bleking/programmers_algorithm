# 프로그래머스 스택/큐 올바른 괄호

def solution(s):
    stack = []
    
    for i in s:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if len(stack) != 0:
                stack.pop()
            elif len(stack) == 0:
                return False
    
    if len(stack) > 0:
        return False

    return True
