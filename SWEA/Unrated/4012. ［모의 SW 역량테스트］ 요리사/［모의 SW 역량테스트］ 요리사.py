from itertools import combinations

def get_synergy(dish):
    synergy = 0

    for i in range(N//2):
        for j in range(N//2):
            synergy += S[dish[i]][dish[j]]
    
    return synergy


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]
    
    origin = list(range(N))
    diff_syn = []
    for dish1 in combinations(origin, N//2):
        dish2 = list(set(origin) - set(dish1))
        diff_syn.append(abs(get_synergy(dish1) - get_synergy(dish2)))

    print(f'#{tc} {min(diff_syn)}' )
