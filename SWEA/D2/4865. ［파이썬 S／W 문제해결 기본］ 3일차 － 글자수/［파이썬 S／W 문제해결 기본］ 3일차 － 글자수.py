T = int(input())

for tc in range(1, T+1):
    str1 = set(input())
    str2 = input()

    found = {}
    for s in str2:
        if s not in str1:
            continue
        
        if s not in found.keys():
            found[s] = 1
        else:
            found[s] += 1

    print(f'#{tc} {max(found.values())}')
