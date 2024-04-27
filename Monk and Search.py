from bisect import bisect_left, bisect_right

# Input the size of the array and the array itself
n = int(input())
arr = list(map(int, input().split()))

# Sort the array
arr.sort()

# Input the number of queries
q = int(input())

# Process each query
for _ in range(q):
    # Input the query parameters
    a, b = map(int, input().split())

    # Initialize count
    count = 0

    # Perform binary search based on the query type
    if a == 0:
        count = len(arr) - bisect_left(arr, b)
    else:
        count = len(arr) - bisect_right(arr, b)

    # Output the result
    print(count)
