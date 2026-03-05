import sys

N, M = map(int, sys.stdin.readline().split())
r_robot, c_robot, d = map(int, sys.stdin.readline().split())
room = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# d =  북  동  남  서
dr = [-1, +0, +1, +0]
dc = [+0, +1, +0, -1]

cleaned = 0
can_clean = True
r_now, c_now, d_now = r_robot, c_robot, d
while can_clean:
    # 1번
    if room[r_now][c_now] == 0:
        room[r_now][c_now] = 2
        cleaned += 1

    # 3번
    can_clean = False
    for i in range(1, 5):
        d_next = (d_now - i) % 4
        r_next, c_next = r_now + dr[d_next], c_now + dc[d_next]
        if 0 <= r_next < N and 0 <= c_next < M and room[r_next][c_next] == 0:
            can_clean = True
            r_now, c_now, d_now = r_next, c_next, d_next
            break

    # 2번
    if not can_clean:
        r_next, c_next = r_now - dr[d_now], c_now - dc[d_now]
        if 0 <= r_next < N and 0 <= c_next < M and room[r_next][c_next] != 1:
            can_clean = True
            r_now, c_now = r_next, c_next

print(cleaned)
