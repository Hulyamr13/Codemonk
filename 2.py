def count_inversions(matrix):
    n = len(matrix)
    inversions = 0
    for i in range(n):
        for j in range(n):
            for x in range(i, n):
                for y in range(j, n):
                    if matrix[i][j] > matrix[x][y]:
                        inversions += 1
    return inversions


def main():
    test_cases = int(input())
    for _ in range(test_cases):
        size = int(input())
        matrix = []
        for _ in range(size):
            row = list(map(int, input().split()))
            matrix.append(row)
        inversions = count_inversions(matrix)
        print(inversions)


if __name__ == "__main__":
    main()
