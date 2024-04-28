def max_common_prefix_length(s, x, y):
    p = 0
    while x < len(s) and y < len(s) and s[x] == s[y]:
        p += 1
        x += 1
        y += 1
    return p


def count_matching_substrings(s, p, l, r):
    prefix = s[:p]
    count = 0
    for i in range(l - 1, r):
        for j in range(i, r):
            if s[i:j + 1] == prefix:
                count += 1
    return count


def main():
    n, q = map(int, input().split())
    s = input().strip()

    for _ in range(q):
        query = input().split()
        if query[0] == '1':
            s += query[1]
        elif query[0] == '2':
            x, y = map(int, query[1:])
            print(max_common_prefix_length(s, x - 1, y - 1))
        elif query[0] == '3':
            p, l, r = map(int, query[1:])
            print(count_matching_substrings(s, p, l, r))


if __name__ == "__main__":
    main()
