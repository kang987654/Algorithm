T = 10
 
for tc in range(1, T+1):
    dump = int(input())
    b_list = list(map(int, input().split()))
 
    # 주어진 dump 횟수만큼 반복
    while dump > 0:
        dump -= 1
 
        # 제일 높은 곳 -1
        b_list[b_list.index(max(b_list))] -= 1
        # 제일 낮은 곳 +1
        b_list[b_list.index(min(b_list))] += 1
 
        # 작업 끝!
        if min(b_list) == int(sum(b_list)/len(b_list)):
            break
 
    # 최고점과 최저점의 높이 차 출력
    print(f'#{tc} {max(b_list) - min(b_list)}')