import re


class Tower(object):
    def __init__(self, *args):
        self.name = args[0][0]
        self.weight = args[0][1]
        self.children_names = args[0][2:]
        self.children = []

    def add(self, tower):
        self.children.append(tower)

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


def build_tower_stack_from_file(file_path):
    towers = read_towers_from_file(file_path)
    i = 0
    while len(towers) > 1:
        tower = towers[i]
        for another_tower in towers:
            if tower.name in another_tower.get_all_children_names():
                another_tower.add(tower)
                del towers[i]
                continue
        i += 1
        i %= len(towers)
    return towers[0]
