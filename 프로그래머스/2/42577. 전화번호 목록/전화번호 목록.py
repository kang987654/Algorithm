def solution(phone_book):
    root = {}
    answer = True

    phone_book.sort(key=len)
    for p in phone_book:
        next_s = root
        for s in p:
            if '*' in next_s:
                return False

            if s in next_s:
                next_s = next_s[s]
            else:
                next_s[s] = {}
                next_s = next_s[s]
        next_s['*'] = True
    return answer