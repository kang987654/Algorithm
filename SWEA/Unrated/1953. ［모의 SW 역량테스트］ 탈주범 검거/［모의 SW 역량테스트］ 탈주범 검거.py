T = int(input())

tunnel = {
    '1': [(-1, +0), (+1, +0), (+0, -1), (+0, +1)],
    '2': [(-1, +0), (+1, +0)                    ],
    '3': [                    (+0, -1), (+0, +1)],
    '4': [(-1, +0),                     (+0, +1)],
    '5': [          (+1, +0),           (+0, +1)],
    '6': [          (+1, +0), (+0, -1),         ],
    '7': [(-1, +0),           (+0, -1),         ]
}


def is_connected(now_r, now_c, next_r, next_c):
    # 터널 존재 여부
    if underground[next_r][next_c] == '0':
        return False

    # 터널 연결 여부
    for dr, dc in tunnel[underground[next_r][next_c]]:
        if next_r + dr == now_r and next_c + dc == now_c:
            return True
    return False


for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    underground = [list(input().split()) for _ in range(N)]

    distance = [[0] * M for _ in range(N)]  # ~= visited
    distance[R][C] = 1
    stack = [(R, C)]
    while stack:
        now_r, now_c = stack.pop(0)

        for dr, dc in tunnel[underground[now_r][now_c]]:
            next_r, next_c = now_r + dr, now_c + dc
            # 범위 안 / 터널 존재하며 연결 됨 / 방문한 적 없음
            if 0 <= next_r < N and 0 <= next_c < M and is_connected(now_r, now_c, next_r, next_c) and (not distance[next_r][next_c]):
                distance[next_r][next_c] = distance[now_r][now_c] + 1
                stack.append((next_r, next_c))

    answer = 0
    for i in range(N):
        for j in range(M):
            if 0 < distance[i][j] <= L:
                answer += 1

    print(f'#{tc} {answer}')
