from models.bst_node import BSTNode


class BSTree:
    def insert(self, root, key):
        if not root:
            return BSTNode(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        return root
    def max_depth(self, node):
        if not node:
            return 0
        return 1 +max(self.max_depth(node.left), self.max_depth(node.right))

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
        return self.in_order(node.left) +[node.key] + self.in_order(node.right) if node else []

    def pre_order(self, node):
        return [node.key] + self.pre_order(node.left) + self.pre_order(node.right) if node else []
    def post_order_delete(self, node):
        if not node:
            return []
        deleted = self.post_order_delete(node.left) + self.post_order_delete(node.right)
        deleted.append(node.key)
        return deleted
    def dsw_balance(self, root):
        def tree_to_vine(root):
            tail = dummy = BSTNode(None)
            dummy.right = root
            while tail.right:
                if tail.right.left:
                    tmp = tail.right.left
                    tail.right.left = tmp.right
                    tmp.right = tail.right
                    tail.right = tmp
                else:
                    tail = tail.right
            return dummy
        def vine_to_tree(dummy, size):
            leaves = size + 1 - 2 ** (size.bit_length() - 1)
            compress(dummy, leaves)
            size = size - leaves
            while size > 1:
                compress(dummy, size // 2)
                size = size // 2
        def compress(dummy, count):
            scanner = dummy
            for _ in range(count):
                child = scanner.right
                if not child:
                    break
                grandchild = child.right
                scanner.right = grandchild
                child.right = grandchild.left
                grandchild.left = child
                scanner = grandchild
        dummy = tree_to_vine(root)
        size = 0
        tmp = dummy.right
        while tmp:
            size += 1
            tmp = tmp.right
        vine_to_tree(dummy, size)
        return dummy.right