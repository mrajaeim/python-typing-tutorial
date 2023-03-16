from modules import Node, Parent

n1 = Node()
p = Parent([n1])

n1 = p.nodes[0]
n1.some_method(p)
