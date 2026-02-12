def make_postfix(infix):
    post = ''
    oper = []
    for i in infix:
        # 연산자
        if i == '(':
            oper.append(i)
        elif i == '+':
            while oper and oper[-1] != '(':
                post += oper.pop()
            oper.append(i)
        elif i == '*':
            while oper and oper[-1] not in '(+':
                post += oper.pop()
            oper.append(i)
        elif i == ')':
            while oper:
                o = oper.pop()
                if o == '(':
                    break
                post += o
        # 피연산자
        else:
            post += i
    # 연산자 스택에 남아있는 것 후위에 넣기
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
        elif p == '*':
            b = nums.pop()
            a = nums.pop()
            nums.append(a*b)
        else:
            nums.append(int(p))
    return nums.pop()


for tc in range(1, 11):
    _len = int(input())
    cal = input()

    post = make_postfix(cal)
    print(f'#{tc} {cal_postfix(post)}')
