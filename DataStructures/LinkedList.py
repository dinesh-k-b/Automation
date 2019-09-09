import Node

class LinkedList(object):

    def __init__(self):
        self.top = None
        self.length = 0

    def addAtStart(self, data):
        node = Node(data)
        node.setNext(self.top)
        self.top = node
        self.length += 1

    