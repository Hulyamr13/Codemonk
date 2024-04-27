n = int(input())
strings = []
for _ in range(n):
    strings.append(input().strip())

niceness_values = []
for i in range(n):
    count = sum(1 for j in range(i) if strings[j] < strings[i])
    niceness_values.append(count)

for value in niceness_values:
    print(value)
