from series.series import diff_series, fibonacci
from traverse.traverse import pre_order, in_order, post_order
from tree.tree import Node, Queue

"""
1. add series to full_queue
2. make an empty_queue, which has tree nodes as objects
3. add full queue's first element to empty_queue as a tree node
4. while empty_queue not empty
4. dequeue empty_queue and add it to tree
5. and dequeue two elements from full_queue
6. make them left and right child of tree and add children to empty_queue
"""
series = fibonacci(10000)
full_queue = Queue()
for val in series:
    full_queue.enqueue(val)

empty_queue = Queue()
root = full_queue.dequeue()
first_node = Node(None, root.get_value())
tree_root = first_node
empty_queue.enqueue(tree_root)
while not empty_queue.is_empty():
    the_node = empty_queue.dequeue().get_value()

    if not full_queue.is_empty():
        left = full_queue.dequeue()
        the_node.add_left_child(left.get_value())
        empty_queue.enqueue(the_node.left)

    if not full_queue.is_empty():
        right = full_queue.dequeue()
        the_node.add_right_child(right.get_value())
        empty_queue.enqueue(the_node.right)

print "Pre-order depth first:"
pre_order(tree_root)
print "In-order depth first:"
in_order(tree_root)
print "Post-order depth first:"
post_order(tree_root)
