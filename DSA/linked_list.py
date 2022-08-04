class Node:
    data = None
    next_node = None

    def __int__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s>" % self.data

