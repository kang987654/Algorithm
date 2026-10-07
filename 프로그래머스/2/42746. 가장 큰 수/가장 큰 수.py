def solution(numbers):
    numbers = sorted(list(map(str, numbers)), key=lambda x:x*3, reverse=True)
    answer = ''.join(numbers)
    return answer if answer[0] != '0' else '0'