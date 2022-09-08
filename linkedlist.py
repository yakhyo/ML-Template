class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return "Node({})".format(self.data)



def LinkedList:

    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(elem)
                node = node.next

    def __repr__(self):
        nodes = []
        node = self.head
        while node:
            nodes.append(node.data)
            node = node.next
        nodes.append("Node")
        return "->".join([str(node) for node in nodes])
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

