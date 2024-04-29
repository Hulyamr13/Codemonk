n, m, g = map(int, input().split())
rain_times = list(map(int, input().split()))
drying_times = list(map(int, input().split()))

# Calculate the maximum gap between consecutive rain times
max_gap = max(rain_times[i + 1] - rain_times[i] for i in range(n - 1))

# Count the number of clothes that can be collected before the next rain
count = sum(1 for drying_time in drying_times if drying_time <= max_gap)

print(count)
