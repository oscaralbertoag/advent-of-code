def main():
    file_path = input("Enter path containing puzzle input: ")
    algorithm_selection = input("Use checksum 1 or 2? ")
    puzzle_input = open(file_path, "r")
    input_lines = puzzle_input.readlines()
    lines_no_whitespace = []
    for line in input_lines:
        lines_no_whitespace.append(line.split())

    if algorithm_selection == 1:
        solution = calculate_checksum(lines_no_whitespace)
    else:
        solution = calculate_checksum_2(lines_no_whitespace)

    print("Solution: {}".format(solution))


def calculate_checksum(input_lines):
    checksum = 0
    for line in input_lines:
        sorted_line = sorted([int(x) for x in line])
        last = sorted_line[-1]
        first = sorted_line[0]
        difference = last - first
        checksum += difference if difference > 0 else 0
    return checksum


def calculate_checksum_2(input_lines):
    checksum = 0
    for line in input_lines:
        sorted_line = sorted([int(x) for x in line])

        for x in range(0, len(sorted_line) - 1):
            found_remainder_zero = False
            for y in range(x + 1, len(sorted_line)):
                divisor = sorted_line[x]
                dividend = sorted_line[y]
                if dividend % divisor == 0:
                    checksum += dividend // divisor
                    found_remainder_zero = True
                    break
            if found_remainder_zero:
                break

    return checksum


if __name__ == "__main__": main()
