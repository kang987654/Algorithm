T = int(input())

for tc in range(1, T+1):
    N = int(input())
    speed, distance = 0, 0

    for _ in range(N):
        temp = input()
        if temp == '0':		# 0일 경우 가속도가 주어지지 않음
            acc = 0
        else:
            state, acc = map(int, temp.split())
            if state == 2:	# 감속
                acc *= -1
        
        speed += acc
        if speed < 0:		# 제약사항 3번
            speed = 0
        distance += speed

    print(f'#{tc} {distance}')
