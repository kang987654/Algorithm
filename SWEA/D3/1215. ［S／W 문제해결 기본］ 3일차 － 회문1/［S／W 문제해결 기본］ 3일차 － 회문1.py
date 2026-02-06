def is_pal_row(i, j, _len):
    for n in range(_len // 2):
        if words[i][j + n] != words[i][(j+_len) - (n+1)]:
            return False
    return True


def is_pal_col(j, i, _len):
    for n in range(_len // 2):
        if words[j + n][i] != words[(j+_len) - (n+1)][i]:
            return False
    return True


for tc in range(1, 11):
    _len = int(input())
    words = [list(input()) for _ in range(8)]

    cnt = 0
    for i in range(8):
        for j in range((8 - _len) + 1):
            # 가로
            if is_pal_row(i, j, _len):
                cnt += 1
            # 세로
            if is_pal_col(j, i, _len):
                cnt += 1
    print(f'#{tc} {cnt}')
