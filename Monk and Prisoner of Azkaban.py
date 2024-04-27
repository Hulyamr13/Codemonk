front = [0] * 1000001
back = [0] * 1000001
arr = [0] * 1000001

stack = []

n = int(input())
arr[1:n + 1] = map(int, input().split())

for i in range(1, n + 1):
    while stack and arr[stack[-1]] < arr[i]:
        front[stack[-1]] = i
        stack.pop()
    stack.append(i)

while stack:
    front[stack[-1]] = -1
    stack.pop()

for i in range(n, 0, -1):
    while stack and arr[stack[-1]] < arr[i]:
        back[stack[-1]] = i
        stack.pop()
    stack.append(i)

while stack:
    back[stack[-1]] = -1
    stack.pop()

for i in range(1, n + 1):
    print(front[i] + back[i], end=" ")
print()
