T = int(input())

for tc in range(1, T+1):
    dp = float(input())

    bin_code = ''
    idx = -1
    while dp:
        if idx <= -13:
            bin_code = 'overflow'
            break

        if dp - (2 ** idx) >= 0:
            bin_code += '1'
            dp -= 2 ** idx
            idx -= 1
        else:
            bin_code += '0'
            idx -= 1

    print(f'#{tc} {bin_code}')
