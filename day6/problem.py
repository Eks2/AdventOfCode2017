def redistribution_cycles_to_same_result(int_list):
    cycles = 0
    redistribution_history = []
    while int_list not in redistribution_history:
        last_int_list = int_list[:]
        int_list = redistribute_int_list_at_max(int_list)
        redistribution_history.append(last_int_list)
        cycles += 1
    infinite_cycle_length = cycles - redistribution_history.index(int_list)
    return cycles, infinite_cycle_length


def redistribute_int_list_at_index(int_list, index):
    value = int_list[index]
    int_list[index] = 0
    while value > 0:
        index += 1
        index %= len(int_list)
        int_list[index] = int_list[index] + 1
        value -= 1
    return int_list


def redistribute_int_list_at_max(int_list):
    return redistribute_int_list_at_index(int_list, int_list.index(max(int_list)))
