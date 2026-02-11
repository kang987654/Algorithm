def make_postfix(infix):
    post = ''
    oper = []
    for i in infix:
        if i == '+':
            # 연산자가 스택에 있으면 우선순위 고려 post 입력,
            # but + 밖에 없음
            if oper:
                post += oper.pop()
            oper.append(i)
        else:
            post += i
    while oper:
        post += oper.pop()

    return post


def cal_postfix(post):
    nums = []
    for p in post:
        if p == '+':
            b = nums.pop()
            a = nums.pop()
            nums.append(a+b)
        else:
            nums.append(int(p))
    return nums.pop()


for tc in range(1, 11):
    _len = int(input())
    cal = input()

    post = make_postfix(cal)
    print(f'#{tc} {cal_postfix(post)}')
