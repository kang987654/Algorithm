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


def find_pal_len():
    for _len in range(100, 0, -1):
        for i in range(100):
            for j in range((100 - _len) + 1):
                # 가로
                if is_pal_row(i, j, _len):
                    return _len
                # 세로
                if is_pal_col(j, i, _len):
                    return _len
    return 0


for _ in range(10):
    tc = int(input())
    words = [list(input()) for _ in range(100)]

    print(f'#{tc} {find_pal_len()}')
