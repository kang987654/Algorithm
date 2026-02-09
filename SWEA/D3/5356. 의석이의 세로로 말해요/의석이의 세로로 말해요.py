T = int(input())

for tc in range(1, T + 1):
    magnets = [list(input()) for _ in range(5)]

    lens = list(map(len, magnets))

    print(f'#{tc}', end=' ')
    for c in range(max(lens)):
        for r in range(5):
            if c < lens[r]:
                print(magnets[r][c], end='')
    print()
