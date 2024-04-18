def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        A = list(map(int, input().split()))
        A.sort()
        ans = float('inf')
        for i in range(n - 1):
            ans = min(ans, A[i] ^ A[i + 1])
        print(ans)


if __name__ == "__main__":
    main()
