n, x = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = n

while start <= end:
    mid = start + (end - start) // 2
    s = 0
    for i in range(mid):
        s += arr[i]
        if s > x:
            break

    if s <= x:
        for i in range(mid, n):
            s -= arr[i - mid]
            s += arr[i]
            if s > x:
                break

    if s > x:
        end = mid - 1
    else:
        ans = mid
        start = mid + 1

print(ans)
