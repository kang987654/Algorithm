T = int(input())

# 문제 조건
_0 = '0001101'
_1 = '0011001'
_2 = '0010011'
_3 = '0111101'
_4 = '0100011'
_5 = '0110001'
_6 = '0101111'
_7 = '0111011'
_8 = '0110111'
_9 = '0001011'


# 암호코드가 포함된 배열 읽기
def get_code(codes):
    for line in codes:
        if line.rstrip('0'):
            return line.rstrip('0')[-56:]


# 유효성 검사 및 유효 코드의 값 계산
def get_validcode(code_num):
    num_v = 0
    for i in range(8):
        if (i+1) % 2:   # 홀수 자리
            num_v += 3 * code_num[i]
        else:   # 짝수 자리
            num_v += code_num[i]

    if num_v % 10:  # 잘못된 암호코드
        return 0
    else:   # 올바른 코드
        return sum(code_num)


for tc in range(1, T+1):
    N, M = map(int, input().split())
    codes = [input() for _ in range(N)]

    code = get_code(codes)
    code_num = []
    for i in range(8):
        if code[7*i: 7*i + 7] == _0:
            code_num.append(0)
        if code[7*i: 7*i + 7] == _1:
            code_num.append(1)
        if code[7*i: 7*i + 7] == _2:
            code_num.append(2)
        if code[7*i: 7*i + 7] == _3:
            code_num.append(3)
        if code[7*i: 7*i + 7] == _4:
            code_num.append(4)
        if code[7*i: 7*i + 7] == _5:
            code_num.append(5)
        if code[7*i: 7*i + 7] == _6:
            code_num.append(6)
        if code[7*i: 7*i + 7] == _7:
            code_num.append(7)
        if code[7*i: 7*i + 7] == _8:
            code_num.append(8)
        if code[7*i: 7*i + 7] == _9:
            code_num.append(9)

    print(f'#{tc} {get_validcode(code_num)}')
