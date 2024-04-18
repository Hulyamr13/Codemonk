from collections import deque

# Function to perform spider selection
def spider_selection(n, x, a):
    # Initialize a queue to store spiders with their powers
    q = deque()
    for i in range(1, n + 1):
        q.append((a[i], i))

    # Initialize a list to store the positions of selected spiders
    selected_spiders = []

    k = x
    while x > 0:
        # Initialize variables to track maximum power and its position
        max_power = -1
        index = -1
        # Dequeue spiders and find the one with maximum power
        h = deque()
        for _ in range(k):
            if not q:
                break
            spider = q.popleft()
            h.append(spider)
            if spider[0] > max_power:
                max_power = spider[0]
                index = spider[1]

        # Store the position of the selected spider
        selected_spiders.append(index)

        # Decrease the power of remaining spiders and enqueue them back
        for _ in range(k):
            if not h:
                break
            spider = h.popleft()
            if spider[1] != index:
                num = spider[0]
                if num:
                    num -= 1
                q.append((num, spider[1]))

        x -= 1

    return selected_spiders

# Input processing
n, x = map(int, input().split())
a = [0] + list(map(int, input().split()))

# Perform spider selection and print the results
result = spider_selection(n, x, a)
print(*result)
