T = int(input())


def sub_sum(n, idx, _sum):
    global cnt

    if n == N:
        if _sum == K:
            cnt += 1
        return

    if _sum >= K:
        return

    for i in range(idx, 12):
        sub_sum(n + 1, i + 1, _sum + A[i])


for tc in range(1, T + 1):
    N, K = map(int, input().split())

    A = list(range(1, 13))
    cnt = 0
    sub_sum(0, 0, 0)

    print(f'#{tc} {cnt}')


##### 비트 연산 (1차 풀이) #####
# T = int(input())
# 
# for tc in range(1, T + 1):
#     N, K = map(int, input().split())
# 
#     # 1~12
#     origin = list(range(1, 13))
#     # 부분 집합의 합을 저장할 리스트
#     sub_sum = []
#     for i in range(1 << 12):
#         sub = []  # 부분 집합
#         cnt = 0  # 부분 집합의 원소 수
#         for j in range(12):
#             if i & (1 << j):
#                 sub.append(origin[j])
#                 cnt += 1
#         if cnt == N:
#             sub_sum.append(sum(sub))
# 
#     print(f'#{tc} {sub_sum.count(K)}')
