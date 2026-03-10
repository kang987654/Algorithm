from itertools import combinations

T = int(input())


def synergy(lst):
    syn = 0
    for i in range(len(lst)-1):
        for j in range(i+1, len(lst)):
            syn += S[lst[i]][lst[j]] + S[lst[j]][lst[i]]
    return syn


for tc in range(1, T+1):
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]

    whole = list(range(N))
    min_diff = float('inf')
    for c in combinations(whole, N//2):
        p1 = list(c)
        p2 = list(set(whole) - set(c))

        min_diff = min(abs(synergy(p1) - synergy(p2)), min_diff)

    print(f'#{tc} {min_diff}')
