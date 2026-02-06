T = int(input())

for tc in range(1, T+1):
    tc, N = input().split()
    words = list(input().split())

    num_lst = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

    print(tc)
    for num in num_lst:
        print(*([num] * words.count(num)), end=' ')
    print()
