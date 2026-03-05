import sys
from itertools import combinations

N = int(sys.stdin.readline())
S = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


# 능력치 구하기
def get_statscore(team):
    score = 0
    for p1 in team:
        for p2 in team:
            score += S[p1][p2]

    return score


min_diff = 1000  # max N//2 = 10, max Sij = 100
# 팀 나누기
members = set(range(N))
for team_s in combinations(members, N//2):
    team_l = tuple(members - set(team_s))

    # 능력치 차이 최소 구하기
    min_diff = min(abs(get_statscore(team_s) - get_statscore(team_l)), min_diff)

print(min_diff)
