for tc in range(1, 11):
    N, passwords = input().split()

    password = []
    for p in passwords:
        # password 가 비어있지 않으면서 마지막값과 p가 같다면
        if password and password[-1] == p:
            password.pop()
        else:
            password.append(p)

    print(f"#{tc} {''.join(password)}")
