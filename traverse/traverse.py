from tree.tree import Node

def pre_order(node):
    if node.value:
        print node.value
    else:
        return None
    if node.left:
        pre_order(node.left)
    if node.right:
        pre_order(node.right)
    return None

def in_order(node):
    if node.left:
        in_order(node.left)
    if node.value:
        print node.value
    else:
        return None
    if node.right:
        in_order(node.right)
    return None

def post_order(node):
    if node.left:
        post_order(node.left)
    if node.right:
        post_order(node.right)
    if node.value:
        print node.value
    return None

if __name__ == "__main__":
    root = Node(None, "F")
    B = root.add_left_child("B")
    A = B.add_left_child("A")
    D = B.add_right_child("D")
    C = D.add_left_child("C")
    E = D.add_right_child("E")
    G = root.add_right_child("G")
    I = G.add_right_child("I")
    H = I.add_left_child("H")
    print "Pre-order depth first:"
    pre_order(root)
    print "In-order depth first:"
    in_order(root)
    print "Post-order depth first:"
    post_order(root)
