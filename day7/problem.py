import re
from collections import Counter


class Tower(object):
    def __init__(self, *args):
        self.name = args[0][0]
        self.weight = int(args[0][1])
        self.children_names = args[0][2:]
        self.children = []

    def add_to_stack(self, tower):
        for child_tower in self.child_generator():
            if tower.name in child_tower.children_names:
                child_tower.add(tower)
                return

    def add(self, tower):
        self.children.append(tower)

    def get_sum_of_weights(self):
        weight = 0
        for child in self.child_generator():
            weight += child.weight
        return weight

    def get_all_children_names(self):
        names = []
        for i in self.child_generator():
            names += i.children_names
        return names

    def child_generator(self):
        yield self
        for child in self.children:
            for grandchild in child.child_generator():
                yield grandchild


def read_towers_from_file(file_path):
    towers = []
    with open(file_path) as f:
        for line in f:
            args = re.findall('\w+', line)
            towers.append(Tower(args))
    return towers


def build_tower_stack_from_list(towers):
    i = 0
    while len(towers) > 1:
        tower = towers[i]
        for another_tower in towers:
            if tower.name in another_tower.get_all_children_names():
                another_tower.add_to_stack(tower)
                del towers[i]
                continue
        i += 1
        i %= len(towers)
    return towers[0]


def build_tower_stack_from_file(file_path):
    towers = read_towers_from_file(file_path)
    return build_tower_stack_from_list(towers)


def find_last_broken_tower(file_path):
    tower = build_tower_stack_from_file(file_path)
    broken_tower_weight = 99999999999
    for child in tower.child_generator():
        grandchild_weights = [grandchild.get_sum_of_weights() for grandchild in child.children]
        if len(set(grandchild_weights)) > 1:
            counter = Counter(grandchild_weights)
            odd_one_out = min(counter, key=counter.get)
            broken_tower_index = grandchild_weights.index(odd_one_out)
            broken_tower_weight = min(broken_tower_weight, child.children[broken_tower_index].get_sum_of_weights())
            correct_tower_weight = child.children[(broken_tower_index + 1) % len(child.children)].get_sum_of_weights()
            print child.children[broken_tower_index].weight - 6
