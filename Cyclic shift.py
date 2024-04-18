def left_shift_by_one(input_string):
    return input_string[1:] + input_string[0]


def main():
    test_cases = int(input())
    for _ in range(test_cases):
        length_of_string, number_of_shifts = map(int, input().split())
        input_string = input().strip()
        max_string = ""
        displacement = 0
        periodicity = -1

        for i in range(length_of_string):
            if max_string < input_string:
                max_string = input_string
                displacement = i
            elif max_string == input_string:
                periodicity = i - displacement
                break
            input_string = left_shift_by_one(input_string)

        if periodicity == -1:
            print(displacement + (number_of_shifts - 1) * length_of_string)
        else:
            print(displacement + (number_of_shifts - 1) * periodicity)


if __name__ == "__main__":
    main()
