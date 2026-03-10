T = int(input())


def check_win(p):
    cnt_lst = [0] * 10
    for c in p:
        cnt_lst[c] += 1

    for i in range(10):
        # run
        if i <= 7 and (cnt_lst[i] and cnt_lst[i+1] and cnt_lst[i+2]):
            return True
        # triplet
        if cnt_lst[i] >= 3:
            return True
    return False


for tc in range(1, T+1):
    deck = list(map(int, input().split()))

    p1, p2 = [], []
    win = 0
    for t in range(6):
        p1.append(deck[2*t])
        p2.append(deck[2*t+1])

        if t >= 2:
            # 이번 문제는 선공, 후공이 존재
            if check_win(p1):
                win = 1
                break
            if check_win(p2):
                win = 2
                break

    print(f'#{tc} {win}')
