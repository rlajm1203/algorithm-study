def solution(n):
    ans = 0
    while n != 0:

        if n % 2 == 1:
            n -= 1
            ans += 1
            continue

        if n % 2 == 0:
            n /= 2
            continue

    return ans