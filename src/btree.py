class BTreeNode:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.children = []

class BTree:
    def __init__(self, t):
        self.root = BTreeNode(leaf=True)
        self.t = t 

    def search(self, key):
        """Search for a key in the B-Tree."""
        node = self.root
        while node:
            for i, k in enumerate(node.keys):
                if key == k:
                    return True
                elif key < k:
                    node = node.children[i]
                    break
            else:
                node = node.children[-1] if node.children else None
        return False

    def insert(self, key):
        """Insert key into the B-Tree."""
        self.root.keys.append(key)
        self.root.keys.sort()
