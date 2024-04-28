s, k = input().split()
k = int(k)
suffixes = [s[i:] for i in range(len(s))]
suffixes.sort()
print(suffixes[k - 1])
