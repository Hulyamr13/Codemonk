def rotate_array(arr, k):
    n = len(arr)
    k = k % n
    return arr[-k:] + arr[:-k]


def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))
        rotated_arr = rotate_array(arr, k)
        print(*rotated_arr)


if __name__ == "__main__":
    main()
