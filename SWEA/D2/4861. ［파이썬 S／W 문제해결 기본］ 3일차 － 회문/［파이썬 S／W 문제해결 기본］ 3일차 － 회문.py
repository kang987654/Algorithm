def is_pal(word, _len):
    for n in range(_len // 2):
        if word[n] != word[-(n+1)]:
            return False
    return True


def find_pal(N, M):
    _len = M
    for i in range(N):
        for j in range((N - M)+1):
            # 가로
            hori = words[i][j:j + M]
            if is_pal(hori, M):
                return ''.join(hori)
            # 세로
            vert = [words[k][i] for k in range(j, j + M)]
            if is_pal(vert, M):
                return ''.join(vert)


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    words = [list(input()) for _ in range(N)]

    pal = find_pal(N, M)

    print(f'#{tc} {pal}')
