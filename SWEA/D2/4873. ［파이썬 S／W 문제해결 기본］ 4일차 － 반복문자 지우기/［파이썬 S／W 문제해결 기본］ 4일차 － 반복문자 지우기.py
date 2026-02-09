T = int(input())

for tc in range(1, T+1):
    s = input()

    s_stack = []
    for cur in s:
        # 비어있다면, 이전 문자와 다르다면
        if (not s_stack) or cur != s_stack[-1]:
            s_stack.append(cur)
        else:
            s_stack.pop()

    print(f'#{tc} {len(s_stack)}')
