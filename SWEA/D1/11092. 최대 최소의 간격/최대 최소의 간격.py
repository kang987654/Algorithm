T = int(input())

for tc in range(1, T+1):
    N = int(input())
    num_stack = list(map(int, input().split()))

    max_num, min_num = 0, 11
    idx, max_idx, min_idx = N-1, N, N

    while num_stack:
        idx -= 1
        num = num_stack.pop()

        if num > max_num:
            max_idx = idx
            max_num = num

        if num <= min_num:
            min_idx = idx
            min_num = num

    print(f'#{tc} {abs(max_idx - min_idx)}')
