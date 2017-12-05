def main():
    file_path = input("Enter path containing puzzle input:")
    puzzle_input = open(file_path, "r")
    input_lines = puzzle_input.readlines()
    lines_no_whitespace = []
    for line in input_lines:
        lines_no_whitespace.append(line.split())
    print("Solution: {}".format(calculate_checksum(lines_no_whitespace)))


def calculate_checksum(input_lines):
    checksum = 0
    for line in input_lines:
        sorted_line = sorted([int(x) for x in line])
        last = sorted_line[-1]
        first = sorted_line[0]
        difference = last - first
        checksum += difference if difference > 0 else 0
    return checksum


if __name__ == "__main__": main()