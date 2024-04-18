import math

MAX = 200011

a = [0] * (MAX + 1)
d = [0] * (MAX + 1)


def divisor(n):
    rn = int(math.sqrt(n))
    for i in range(1, rn + 1):
        if n % i == 0:
            if n == i * i:
                d[i] += 1
            else:
                d[i] += 1
                d[n // i] += 1


n = int(input())
arr = list(map(int, input().split()))
for num in arr:
    divisor(num)

t = int(input())
for _ in range(t):
    p, q = map(int, input().split())
    count = 0
    pq = p * q
    if q < p:
        p, q = q, p
    if q % p == 0:
        count = d[p]
    else:
        count = d[p] + d[q]
        if p < 1414:
            if pq < MAX:
                count -= d[pq]
    print(count)
