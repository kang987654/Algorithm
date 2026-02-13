for _ in range(10):
    tc = input()
    password = list(map(int, input().split()))

    making = True
    while making:
        for i in range(1, 6):
            p = password.pop(0) - i
            if p <= 0:
                password.append(0)
                making = False
                break
            password.append(p)

    print(f'#{tc}', *password)
