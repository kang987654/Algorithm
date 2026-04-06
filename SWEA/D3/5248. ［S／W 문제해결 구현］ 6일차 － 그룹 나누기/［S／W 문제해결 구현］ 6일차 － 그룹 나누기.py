T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    # 두 사람의 출석 번호를 종이에 적어 제출
    partners = []
    for i in range(0, len(arr), 2):
        partners.append(set([arr[i], arr[i+1]]))

    # 한 사람이 여러 장의 종이를 제출하거나 여러 사람이 한 사람을 지목한 경우 모두 같은 조
    teams = []
    for p in range(len(partners)):
        matched = False
        for t in range(len(teams)):
            if partners[p] & teams[t]:
                teams[t] = partners[p] | teams[t]
                matched = True
        if not matched:
            teams.append(partners[p])

    # 1번-2번, 3번-4번, 2-3번이 같은 조가 되고 싶다고 하면, 1-2-3-4번이 같은 조
    results = []
    while teams:
        team = teams.pop()

        matched = False
        for t in range(len(teams)):
            if team & teams[t]:
                teams[t] = team | teams[t]
                matched = True
        if not matched:
            results.append(team)

    # 번호를 적지도 않고 다른 사람에게 지목되지도 않은 사람은 단독으로 조를 구성
    members = list(range(1, N+1))
    for member in members:
        matched = False
        for result in results:
            if member in result:
                matched = True
                break
        if not matched:
            results.append(set([member]))

    print(f'#{tc} {len(results)}')
