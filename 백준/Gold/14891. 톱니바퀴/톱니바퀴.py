import sys
from collections import deque

gears = [deque(sys.stdin.readline().strip()) for _ in range(4)]
# N : 0, S : 1
idx_l, idx_r = -2, 2

K = int(sys.stdin.readline().strip())
for _ in range(K):
    gear_t, direction_o = map(int, sys.stdin.readline().strip().split())
    gear_t -= 1
    # 타겟 기어 회전
    origin_l, origin_r = gears[gear_t][idx_l], gears[gear_t][idx_r]
    if direction_o == 1:
        gears[gear_t].appendleft(gears[gear_t].pop())
    else:
        gears[gear_t].append(gears[gear_t].popleft())

    # 타겟 기어로부터 앞에 있는 것
    direction = direction_o * -1
    prev_l, prev_r = origin_l, origin_r
    for i in range(gear_t-1, -1, -1):
        now_l, now_r = gears[i][idx_l], gears[i][idx_r]
        if now_r != prev_l:
            if direction == 1:
                gears[i].appendleft(gears[i].pop())
            else:
                gears[i].append(gears[i].popleft())
            direction *= -1
            prev_l, prev_r = now_l, now_r
        else:
            break

    # 타겟 기어로부터 뒤에 있는 것
    direction = direction_o * -1
    prev_l, prev_r = origin_l, origin_r
    for i in range(gear_t+1, 4):
        now_l, now_r = gears[i][idx_l], gears[i][idx_r]
        if prev_r != now_l:
            if direction == 1:
                gears[i].appendleft(gears[i].pop())
            else:
                gears[i].append(gears[i].popleft())
            direction *= -1
            prev_l, prev_r = now_l, now_r
        else:
            break

score = 0
for i in range(4):
    score += int(gears[i][0]) * 2**i

print(score)
