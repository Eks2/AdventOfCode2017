import re


def read_input_file(file_path):
    with open(file_path) as f:
        instructions = [re.findall('\S+', line) for line in f]
    return instructions


def create_registers_from_instructions(instructions):
    return Registers(set([i[0] for i in instructions]))


class Registers(object):
    def __init__(self, names):
        self.dict = {name: 0 for name in names}
        self.max_register_value = 0

    def perform_instruction(self, instruction):
        register_name = instruction[0]
        inc_or_dec = instruction[1]
        delta = int(instruction[2])
        condition_register_value = self.dict[instruction[4]]
        condition_is_true = eval(str(condition_register_value) + instruction[5] + instruction[6])
        if condition_is_true:
            if inc_or_dec == 'inc':
                self.dict[register_name] += delta
                self.max_register_value = max(self.max_register_value, self.dict[register_name])
            elif inc_or_dec == 'dec':
                self.dict[register_name] -= delta
            else:
                raise Exception()


def compute_registers_from_input_file(file_path):
    instructions = read_input_file(file_path)
    registers = create_registers_from_instructions(instructions)
    for i in instructions:
        registers.perform_instruction(i)
    return registers


def get_max_register_from_input_file(file_path):
    return max(compute_registers_from_input_file(file_path).dict.values())


def get_abs_max_register_from_input_file(file_path):
    return compute_registers_from_input_file(file_path).max_register_value
