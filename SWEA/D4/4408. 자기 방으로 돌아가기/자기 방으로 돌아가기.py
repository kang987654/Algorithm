T = int(input())

for tc in range(1, T+1):
    N = int(input())
    rooms = [tuple(map(int, input().split())) for _ in range(N)]

    cnt = [0] * 200
    for i in range(N):
        s, e = rooms[i]
        left = min(s, e) // 2 if min(s, e) % 2 else min(s, e) // 2 - 1
        right = max(s, e) // 2 if max(s, e) % 2 else max(s, e) // 2 - 1

        for j in range(left, right+1):
            cnt[j] += 1

    print(f'#{tc} {max(cnt)}')
