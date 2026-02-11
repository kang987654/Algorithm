T = int(input())

for tc in range(1, T + 1):
    forth = list(input().split())

    nums = []
    try:
        for f in forth:
            if f in '+-*/':
                b = nums.pop()
                a = nums.pop()
                if f == '+':
                    nums.append(a + b)
                if f == '-':
                    nums.append(a - b)
                if f == '*':
                    nums.append(a * b)
                if f == '/':
                    nums.append(a // b)
            elif f == '.':
                if len(nums) == 1:
                    print(f'#{tc} {nums.pop()}')
                else:
                    print(f'#{tc} error')
            else:
                nums.append(int(f))
    except IndexError:
        print(f'#{tc} error')
