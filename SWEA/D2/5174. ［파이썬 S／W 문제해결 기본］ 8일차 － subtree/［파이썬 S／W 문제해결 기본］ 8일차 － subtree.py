T = int(input())

for tc in range(1, T+1):
    E, N = map(int, input().split())
    nums = list(map(int, input().split()))

    # 문제에서 주어진 구조
    par = list(range(E+2))
    ch1 = [0] * (E + 2)
    ch2 = [0] * (E + 2)

    for i in range(E):
        p, c = nums[i*2], nums[i*2 + 1]

        if ch1[p] == 0:
            ch1[p] = c
        elif ch2[p] == 0:
            ch2[p] = c

    # 노드 N을 루트로 하는 서브 트리에 속한 노드의 개수
    stack = [N]
    cnt = 0
    while stack:
        now = stack.pop()
        cnt += 1

        if ch1[now] != 0:
            stack.append(ch1[now])
        if ch2[now] != 0:
            stack.append(ch2[now])

    print(f'#{tc} {cnt}')
