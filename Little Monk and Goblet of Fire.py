from collections import deque

# Function to simulate the process
def process_queries(q):
    lane = deque()
    school = [deque() for _ in range(5)]
    results = []
    for _ in range(q):
        query = input().split()
        if query[0] == 'D':
            results.append((lane[0], school[lane[0]].popleft()))
            if not school[lane[0]]:
                lane.popleft()
        else:
            x, y = map(int, query[1:])
            school[x].append(y)
            if x not in lane:
                lane.append(x)
    return results

# Read the number of queries
q = int(input())

# Process the queries and print the results
for result in process_queries(q):
    print(result[0], result[1])
