def main():
    test = int(input())
    for _ in range(test):
        n, m = map(int, input().split())
        ans = -1
        for i in range(m):
            if (i * i) % m == n:
                ans = i
                break
        print(ans)


if __name__ == "__main__":
    main()
