for tc in range(1, 11):
    N = int(input())
    gwalhos = input()

    gwalho_open = ['(', '[', '{', '<']
    gwalho_close = [')', ']', '}', '>']
    valid = 1

    g_stack = []
    for g in gwalhos:
        # 여는 괄호면 stack에 넣기
        if g in gwalho_open:
            g_stack.append(g)
        # 닫는 괄호일 때, g_stack에 값이 없거나, 짝이 다르면 무효 및 중단
        elif (not g_stack) or g_stack.pop() != gwalho_open[gwalho_close.index(g)] :
            valid = 0
            break
    # 짝이 없음 = 무효
    if g_stack:
        valid = 0

    print(f'#{tc} {valid}')
