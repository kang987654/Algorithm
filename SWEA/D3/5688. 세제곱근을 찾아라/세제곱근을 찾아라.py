T = int(input())

tri_n = [x**3 for x in range(10**6 + 1)]

for tc in range(1, T+1):
    N = int(input())

    i = -1
    if N in tri_n:
        i = tri_n.index(N)

    print(f'#{tc} {i}')
