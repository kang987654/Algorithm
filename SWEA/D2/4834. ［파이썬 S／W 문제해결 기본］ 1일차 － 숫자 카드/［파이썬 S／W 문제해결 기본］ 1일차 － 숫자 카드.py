T = int(input())
 
for tc in range(1, T+1):
    N = int(input())
    cards = list(map(int, input().strip()))
 
	# 숫자별 count 리스트
    cnt_list = [0] * 10
    for num in cards:
        cnt_list[num] += 1
     
    # 카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력
    for i in range(9, -1, -1):
        if cnt_list[i] == max(cnt_list):
            print(f'#{tc} {i} {cnt_list[i]}')
            break