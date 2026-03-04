T = int(input())

for tc in range(1, T+1):
    _len, hex_code = input().split()

    bin_code = ''
    for i in range(int(_len)):
        dec = int(hex_code[i], 16)	# 16진수(str)를 10진수(int)로
        _bin = bin(dec)	# 10진수(int)를 2진수(str)로

        # 포맷팅
        bin_code += '0'*(6-len(_bin)) + _bin[2:]

    print(f'#{tc} {bin_code}')
