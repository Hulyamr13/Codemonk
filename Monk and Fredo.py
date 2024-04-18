import math

def extendedEuclid(A, B):
    global g, x, y
    if B == 0:
        g = A
        x = 1
        y = 0
    else:
        extendedEuclid(B, A % B)
        temp = x
        x = y
        y = temp - (A // B) * y

def main():
    q = int(input())
    for _ in range(q):
        a, b, d = map(int, input().split())
        extendedEuclid(a, b)
        if d % g != 0:
            print(0)
            continue
        k1 = math.ceil(-x * (d / b))
        k2 = math.floor(y * (d / a))
        if k1 <= k2:
            print(k2 - k1 + 1)
        else:
            print(0)

if __name__ == "__main__":
    main()
