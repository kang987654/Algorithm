T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    
    N, M = len(str1), len(str2)
    found = 0
    for i in range(M - N + 1):
        if str1 == str2[i:i+N]:
            found = 1
            
    print(f'#{tc} {found}')
