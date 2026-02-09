T = int(input())

for tc in range(1, T+1):
    s = input()

    valid = 1
    s_stack = []
    for cur in s:
        # (, { 일 경우에만 스택에 저장
        if cur == '(' or cur == '{':
            s_stack.append(cur)
        # ), } 일 경우, 비어있는지, 이전에 알맞게 나왔는지 확인
        elif cur == ')':
            if (not s_stack) or s_stack.pop() != '(':
                valid = 0
                break
        elif cur == '}':
            if (not s_stack) or s_stack.pop() != '{':
                valid = 0
                break
    # 순회가 끝난 뒤, 스택에 남아 있다면 짝x
    if s_stack:
        valid = 0

    print(f'#{tc} {valid}')
