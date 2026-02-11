T = int(input())

for tc in range(1, T+1):
    N = int(input())
    seq = list(input().split('0'))

    print(f'#{tc} {max(map(len, seq))}')
