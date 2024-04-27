def binary_search(arr, key):
    low, high = 0, len(arr) - 1
    while low < high:
        mid = (low + high) // 2
        if arr[mid] > key:
            high = mid
        else:
            low = mid + 1
    if arr[low] > key:
        return low
    return -1

def can_use_special_wand():
    minimum = aux[-1]
    for i in range(1, n):
        index = binary_search(st[i], minimum)
        if index == -1:
            return False
        else:
            minimum = st[i][index]
    return True

n = int(input())
st = [[] for _ in range(n)]
size = [0] * n
aux = []

for i in range(n):
    size[i], *st[i] = map(int, input().split())

for val in st[0]:
    if not aux or val < aux[-1]:
        aux.append(val)
    else:
        aux.append(aux[-1])

q = int(input())
for _ in range(q):
    v, *args = map(int, input().split())
    if v == 1:
        k, h = args
        k -= 1
        st[k].append(h)
        if k == 0:
            if not aux or h < aux[-1]:
                aux.append(h)
            else:
                aux.append(aux[-1])
    elif v == 0:
        k = args[0] - 1
        size[k] -= 1
        if k == 0:
            aux.pop()
    else:
        if can_use_special_wand():
            print("YES")
        else:
            print("NO")
