def make_postfix(infix):
    post = ''
    oper = []
    for i in infix:
        # 연산자
        if i in '+*':
            if oper:
                # +* 중 + 우선순위가 낮으므로 스택 pop하여 post에 추가하고 +만 추가
                if i == '+':
                    while oper:
                        post += oper.pop()
                    oper.append(i)
                # *일 때, + 우선순위가 낮으므로 스택에 그대로 추가
                elif oper[-1] == '+':
                    oper.append(i)
                else:
                    post += i
            else:
                oper.append(i)
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
