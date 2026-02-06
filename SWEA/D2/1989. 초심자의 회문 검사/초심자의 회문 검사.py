def is_pal(word):
    _len = len(word)
    for n in range(_len // 2):
        if word[n] != word[-(n+1)]:
            return 0
    return 1


T = int(input())

for tc in range(1, T+1):
    print(f'#{tc} {is_pal(input())}')
