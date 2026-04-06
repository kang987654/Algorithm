T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    partners = []
    for i in range(0, len(arr), 2):
        partners.append(set([arr[i], arr[i+1]]))

    teams = []
    for p in range(len(partners)):
        matched = False
        for t in range(len(teams)):
            if partners[p] & teams[t]:
                teams[t] = partners[p] | teams[t]
                matched = True
        if not matched:
            teams.append(partners[p])

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
