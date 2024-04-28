t = int(input())

for _ in range(t):
    n = int(input())
    marks = [0] * 1000001

    marks_list = list(map(int, input().split()))

    for mark in marks_list:
        marks[mark] += 1

    x = -1
    y = -1

    for i in range(1, 1000001):
        if marks[i] and x == -1:
            x = i
            y = i

        if marks[i] and marks[i] > marks[x]:
            x = i

        if marks[i] and marks[i] < marks[y]:
            y = i

    if abs(marks[x] - marks[y]) > 0:
        print(abs(marks[x] - marks[y]))
    else:
        print(-1)
