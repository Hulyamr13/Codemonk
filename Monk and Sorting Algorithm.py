N = int(input())
arr = list(map(int, input().split()))


def custom_sort(x):
    # Функцията връща като ключ за сортиране
    # остатъка при деление на i и j за всяко число в масива
    return (x / i) % j


max_arr = max(arr)
i = 1
j = 10 ** 5

while max_arr:
    arr.sort(key=custom_sort)
    print(' '.join(map(str, arr)))
    i *= j
    max_arr //= j
