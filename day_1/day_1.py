import os


def solve_captcha(captcha, length=1):
    result = 0
    for index in range(0, len(captcha)):
        if captcha[index] == captcha[index - length]:
            result += int(captcha[index])

    return result


if __name__ == '__main__':
    print(os.getcwd())
    with open('day_1/input') as data:
        captcha = data.readline()
        print(solve_captcha(captcha))
        print(solve_captcha(captcha, int(len(captcha) / 2)))