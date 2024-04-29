from functools import lru_cache

mod = 1000000009


@lru_cache(1024)
def ans(n):
    if n == 0:
        return 1
    if n == 1:
        return 10

    temp1 = ans(n // 2)
    temp2 = ans(n // 2 - 1)

    if (n & 1) == 0:
        return (temp1 * temp1 - temp2 * temp2) % mod
    else:
        temp3 = ans(n // 2 + 1)
        return (temp1 * (temp3 - temp2)) % mod


for t in range(int(input())):
    n = int(input())
    print(ans(n))
