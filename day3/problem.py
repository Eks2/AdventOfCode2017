import math
import numpy as np
import pandas as pd


def find_square_size_from_number(number):
    square_root = math.sqrt(number)
    square_size = math.ceil(square_root)

    if not square_size % 2:
        square_size += 1

    square_number = (square_size/2)-0.5
    return square_size, square_number


def find_steps_from_number(number):
    square_size, square_number = find_square_size_from_number(number)
    corner_value = square_size**2

    corner_location = np.array([square_number, -square_number])
    number_location = corner_location

    difference_from_corner_value = corner_value - number

    x_shift = min(difference_from_corner_value, square_size - 1)
    number_location = number_location - np.array([x_shift, 0])
    difference_from_corner_value -= x_shift

    y_shift = min(difference_from_corner_value, square_size - 1)
    number_location = number_location + np.array([0, y_shift])
    difference_from_corner_value -= y_shift

    x_shift = min(difference_from_corner_value, square_size - 1)
    number_location = number_location + np.array([x_shift, 0])
    difference_from_corner_value -= x_shift

    y_shift = min(difference_from_corner_value, square_size - 1)
    number_location = number_location - np.array([0, y_shift])

    return int(abs(number_location[0]) + abs(number_location[1]))


class SpiralMemory:

    def __init__(self):
        self.df = pd.DataFrame({'x' : [0], 'y' : [0], 'sum_value' : [1]})

    @property
    def current_index(self):
        return max(self.df.index)

    @property
    def current_count_number(self):
        return self.current_index + 1

    @property
    def current_pos(self):
        return np.array(self.df.loc[self.current_index][['x', 'y']])

    @property
    def square_size(self):
        num = math.ceil(math.sqrt(self.current_count_number))
        if num % 2 == 0:
            num += 1
        return num

    @property
    def bottom_right_count_number(self):
        return self.square_size ** 2

    @property
    def top_right_count_number(self):
        return self.square_size ** 2 - 3 * self.square_size + 3

    @property
    def bottom_left_count_number(self):
        return self.square_size ** 2 - 1 * self.square_size + 1

    @property
    def top_left_count_number(self):
        return self.square_size ** 2 - 2 * self.square_size + 2

    @property
    def layer_complete(self):
        square_size = self.square_size
        if square_size.is_integer() and square_size % 2 != 0:
            return True
        else:
            return False

    @property
    def current_direction(self):
        if self.current_count_number < self.top_right_count_number:
            return np.array([0, 1])
        elif self.current_count_number < self.top_left_count_number:
            return np.array([-1, 0])
        elif self.current_count_number < self.bottom_left_count_number:
            return np.array([0, -1])
        else:
            return np.array([1, 0])

    @property
    def sum_of_next_number(self):
        x, y = self.current_pos + self.current_direction
        return self.df.loc[(self.df.x >= x - 1) & (self.df.x <= x + 1) &
                           (self.df.y >= y - 1) & (self.df.y <= y + 1)].sum_value.sum()

    def perform_step(self):
        current_pos = self.current_pos + self.current_direction
        self.df.loc[self.current_index + 1] = {'x': current_pos[0], 'y': current_pos[1],
                                               'sum_value': self.sum_of_next_number}


def find_next_sum_value_in_spiral_memory(number):
    sm = SpiralMemory()
    while sm.sum_of_next_number < number:
        sm.perform_step()
    sm.perform_step()
    return sm.df.loc[sm.current_index].sum_value
