class Node:
    def __init__(self, data:int):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data})"




a = Node()

b = Node("salom")
