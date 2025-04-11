from graphviz import Digraph

def export_tree_to_graphviz(node, dot=None, tree_type="BST"):
    if dot is None:
        dot = Digraph(comment=f'{tree_type} Tree')
    if node:
        dot.node(str(id(node)), str(node.key))
        if node.left:
            dot.node(str(id(node.left)), str(node.left.key))
            dot.edge(str(id(node)), str(id(node.left)))
            export_tree_to_graphviz(node.left, dot, tree_type)
        if node.right:
            dot.node(str(id(node.right)), str(node.right.key))
            dot.edge(str(id(node)), str(id(node.right)))
            export_tree_to_graphviz(node.right, dot, tree_type)
    return dot