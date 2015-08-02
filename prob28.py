"""
project euler problem 28
"""
from itertools import cycle
from operator import gt, lt, add, sub

# pylint: disable=R0903


class Up(object):
    """
    base class for movements generating a spiral
    """
    def __init__(self):
        self.max = 0
        self.index = 1
        self.operation = add
        self.extent = gt

    def move(self, pos):
        """
        move up one
        """
        new_pos = list(pos)
        new_pos[self.index] = self.operation(pos[self.index], 1)
        change_direction = False
        if self.extent(new_pos[self.index], self.max):
            self.max = new_pos[self.index]
            change_direction = True
        return new_pos, change_direction


class Down(Up):
    """
    move down
    """
    def __init__(self):
        super(Down, self).__init__()
        self.operation = sub
        self.extent = lt


class Right(Up):
    """
    move right
    """
    def __init__(self):
        super(Right, self).__init__()
        self.index = 0
        self.operation = add
        self.extent = gt


class Left(Right):
    """
    move left
    """
    def __init__(self):
        super(Left, self).__init__()
        self.operation = sub
        self.extent = lt


def gen_spiral(num):
    """
    generate spiral coordinates for num points
    """
    order = (Right(), Down(), Left(), Up())
    cycle_order = cycle(order)
    operation = cycle_order.next()
    pos = [0, 0]
    pos_list = []
    count = 0
    for i in range(1, num+1):
        pos_list.append(pos)
        if abs(pos[0]) == abs(pos[1]):
            count += i
        pos, change = operation.move(pos)
        if change:
            operation = cycle_order.next()
    return pos_list, count

print gen_spiral(1001**2)[1]
