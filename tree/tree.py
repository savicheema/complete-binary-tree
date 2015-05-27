import math, random

class Node():
    value = None
    parent = None
    left = None
    right = None
    def __init__(self, parent=None, value=None):
        if value:
            self.value = value
        else:
            base_random = random.random()
            multiplier_random = random.random()*100
            self.value = math.floor(base_random*multiplier_random)
        if parent:
            self.parent = parent
        return None

    def add_left_child(self, value=None):
        node = Node(self, value)
        self.left = node
        return self.left

    def add_right_child(self, value=None):
        node = Node(self, value)
        self.right = node
        return self.right

    def parent_value(self):
        if self.parent:
            return self.parent.value
        else:
            return None

    def left_child(self):
        if self.left:
            return self.left.value
        else:
            return None

    def right_child(self):
        if self.right:
            return self.right.value
        else:
            return None


class Obj():
    value = None
    link = None

    def __init__(self, value=None):
        self.value = value
        return None

    def get_value(self):
        return self.value

    def get_next(self):
        return self.link

    def set_next(self, value):
        obj = Obj(value)
        self.link = obj
        return obj

class Queue():
    first = None
    last = None

    def __init__(self, value=None):
        if value:
            obj = Obj(value)
            self.first = obj
            self.last = obj
        return None

    def enqueue(self, value):
        obj = Obj(value)
        if not self.first or not self.last:
            self.first = obj
            self.last = obj
        else:
            self.last.link = obj
            self.last = obj
        return obj

    def dequeue(self):
        if not self.first or not self.last:
            raise ValueError
        else:
            pop = self.first
            self.first = self.first.get_next()
        return pop

    def traverse(self):
        node = self.first
        result = []
        while node is not None:
            value = node.get_value()
            node = node.get_next()
            result.append(value)
        return result

    def is_empty(self):
        if not self.first:
            return True
        else:
            return False
# print(__name__)
if __name__ == '__main__':
    root = Node()
    left = root.add_left_child()
    right = root.add_right_child()
    print"parent", ("value: {}".format(root.value), "parent: {}".format(root.parent_value()), "left: {}".format(root.left_child()), "right: {}".format(root.right_child()))
    print"left", ("value: {}".format(left.value), "parent: {}".format(left.parent_value()), "left: {}".format(left.left_child()), "right: {}".format(left.right_child()))
    print"right", ("value: {}".format(right.value), "parent: {}".format(right.parent_value()), "left: {}".format(right.left_child()), "right: {}".format(right.right_child()))

    queue = Queue()
    queue.enqueue(5)
    queue.enqueue(1)
    queue.enqueue(7)
    queue.enqueue(3)
    queue.enqueue(8)
    queue.enqueue(7)
    queue.enqueue(4)
    queue.enqueue(2)
    queue.enqueue(8)
    queue.enqueue(4)
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    first = queue.traverse()
    for val in first:
        print val
