T = int(input())

for tc in range(1, T+1):
    batch = input()

    piece = 0
    sticks = 0

    for i in range(len(batch)):
        # 막대기일지도 모르니까 sticks+1
        if batch[i] == '(':
            sticks += 1

        else:   # b == ')'
            sticks -= 1
            # laser cut
            if batch[i-1] == '(':
                piece += sticks
            # stick end
            else:
                piece += 1

    print(f'#{tc} {piece}')
