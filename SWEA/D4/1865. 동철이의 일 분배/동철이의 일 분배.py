T = int(input())


def get_work(i, this_work):
    global max_work

    # 종결 조건
    if i == N:
        max_work = this_work
        return

    for j in range(N):
        if not visited[j]:
            next_work = this_work * P[i][j]*0.01
            # 가지 치기
            if next_work <= max_work:
                continue
            # 백트래킹
            visited[j] = True
            get_work(i+1, next_work)
            visited[j] = False


for tc in range(1, T+1):
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]

    visited = [False] * N
    # 최소 조건을 max 값으로 임시 지정
    max_work = 1
    for p in map(min, P):
        max_work *= p * 0.01
    get_work(0, 1)

    print(f'#{tc} {max_work * 100:.6f}')

##### 완전 탐색 (시간초과) #####
# from itertools import permutations
#
# T = int(input())
#
# for tc in range(1, T+1):
#     N = int(input())
#     P = [list(map(int, input().split())) for _ in range(N)]
#
#     max_work = 0
#     for j in permutations(range(N)):
#         this_work = 1
#         for i in range(N):
#             this_work *= P[i][j[i]] * 0.01
#         max_work = max(this_work, max_work)
#
#     print(f'#{tc} {max_work * 100:.6f}')
