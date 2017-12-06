def file_input_steps_to_exit(file_path, strange=False):
    with open(file_path) as f:
        lines = [int(i.replace('\n', '')) for i in f.readlines()]
        return steps_to_exit(lines, strange)


def steps_to_exit(int_list, strange=False):
    steps = 0
    pos = 0
    int_list_len = len(int_list)
    while pos < int_list_len:
        int_value = int_list[pos]
        if strange and int_value >= 3:
            int_list[pos] = int_value - 1
        else:
            int_list[pos] = int_value + 1
        pos += int_value
        steps += 1
    return steps
