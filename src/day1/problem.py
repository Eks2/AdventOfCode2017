import re


def captcha_solver(input_string):
    pattern = re.compile(r'(\w)\1+')
    total_sum = 0

    for match in pattern.finditer(input_string):
        string = match.group()
        integer = int(string[0])
        my_sum = integer*(len(string) - 1)
        total_sum += my_sum

    # Still need to check the first and last characters manually!
    if input_string[0] == input_string[-1]:
        total_sum += int(input_string[0])

    return total_sum


def lookahead_captcha_solver(input_string, lookahead=1):
    my_sum = 0
    for i, char in enumerate(input_string):
        if char == input_string[(lookahead + i) % len(input_string)]:
            my_sum += int(char)
    return my_sum


def half_list_lookahead_captcha_solver(input_string):
    lookahead_captcha_solver(input_string, len(input_string)/2)
