T = int(input())


def hoare_partition(left, right):
    mid = (left + right) // 2
    pivot = a[mid]
    a[left], a[mid] = a[mid], a[left]   # pivot 을 맨 왼쪽으로 치워두기
    i = left + 1    # 왼쪽 포인터
    j = right       # 오른 포인터

    # 두 포인터가 교차할 때까지
    while i <= j:
        # i를 pivot 보다 큰 값이 나올 때까지 >>
        while i <= j and a[i] <= pivot:
            i += 1
        # j를 pivot 보다 작은 값이 나올 때까지 <<
        while i <= j and a[j] >= pivot:
            j -= 1
        # 위의 결과가 교차하지 않는다면
        if i < j:
            a[i], a[j] = a[j], a[i]

    a[left], a[j] = a[j], a[left]       # pivot 위치 확정
    return j


def quick_sort(left, right):
    if left < right:
        pivot = hoare_partition(left, right)
        quick_sort(left, pivot-1)
        quick_sort(pivot+1, right)


for tc in range(1, T+1):
    N = int(input())
    a = list(map(int, input().split()))

    quick_sort(0, len(a)-1)

    print(f'#{tc} {a[N//2]}')
