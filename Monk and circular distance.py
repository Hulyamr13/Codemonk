from math import sqrt
from bisect import bisect_right

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# Calculate the Euclidean distance for each point and store it in sqrt_arr
sqrt_arr = [sqrt(x ** 2 + y ** 2) for x, y in arr]

# Sort the distances
sqrt_arr.sort()

q = int(input())
for _ in range(q):
    element = int(input())
    # Use bisect_right to find the count of points within the given radius
    count = bisect_right(sqrt_arr, element)
    print(count)
