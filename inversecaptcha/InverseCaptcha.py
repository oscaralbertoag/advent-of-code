def main():
    captcha_choice = input("Captcha 1 or 2?")
    file_path = input("Inverse captcha file path:")
    reverse_captcha_file = open(file_path, "r")
    captcha = reverse_captcha_file.read()
    reverse_captcha_file.close()
    if captcha_choice == 1:
        solution = solve_captcha([int(x) for x in captcha])
    else:
        solution = solve_captcha_2([int(x) for x in captcha])

    print("Solution: {}".format(solution))


def solve_captcha(captcha):
    captcha_length = len(captcha)
    captcha_sum = 0
    for x in range(0, captcha_length):
        current_digit = captcha[x]
        if x == captcha_length - 1:
            next_digit = captcha[0]
        else:
            next_digit = captcha[x + 1]

        if current_digit == next_digit:
            captcha_sum += current_digit

    return captcha_sum


def solve_captcha_2(captcha):
    captcha_length = len(captcha)
    step_size = captcha_length // 2
    captcha_sum = 0
    for x in range(0, captcha_length):
        current_digit = captcha[x]
        if x + step_size > captcha_length - 1:
            distance_from_end = captcha_length - 1 - x
            digit_ahead = captcha[step_size - distance_from_end - 1]  # Subtract one because array is zero-based
        else:
            digit_ahead = captcha[x + step_size]

        if current_digit == digit_ahead:
            captcha_sum += current_digit

    return captcha_sum


if __name__ == "__main__": main()
