from models.avl_node import AVLNode


class AVLTree:
    def insert_balanced(self, sorted_list):
        if not sorted_list:
            return None
        mid = len(sorted_list) // 2
        root =AVLNode(sorted_list[mid])
        root.left =self.insert_balanced(sorted_list[:mid])
        root.right =self.insert_balanced(sorted_list[mid+1:])
        root.height = 1+ max(self.get_height(root.left),
                             self.get_height(root.right))
        return root



    def get_height(self, node):
        return node.height if node else 0
    def max_depth(self, node):
        if not node:
            return 0
        return 1 + max(self.max_depth(node.left), self.max_depth(node.right))
    def find_min_path(self, node):
        path = []
        while node:
            path.append(node.key)
            node = node.left
        return path
    def find_max_path(self, node):
        path = []
        while node:
            path.append(node.key)
            node = node.right
        return path
    def in_order(self, node):
        return self.in_order(node.left) +[node.key] +self.in_order(node.right) if node else []
    def pre_order(self, node):
        return [node.key] + self.pre_order(node.left) +self.pre_order(node.right) if node else []
    def post_order_delete(self, node):
        if not node:
            return []
        deleted = self.post_order_delete(node.left) +self.post_order_delete(node.right)
        deleted.append(node.key)
        return deleted