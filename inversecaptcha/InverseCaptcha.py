def main():
    file_path = input("Inverse captcha file path:")
    reverse_captcha_file = open(file_path, "r")
    captcha = reverse_captcha_file.read()
    reverse_captcha_file.close()
    print("Solution: {}".format(solve_captcha([int(x) for x in captcha])))


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


if __name__ == "__main__": main()
