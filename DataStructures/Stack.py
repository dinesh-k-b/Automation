from Node import Node

class EmptyStack(Exception):
    pass

class StackIsFull(Exception):
    pass

class Stack(EmptyStack, StackIsFull):

    def __init__(self, size):
        self.top = None
        self.length = 0
        self.size = size

    def push(self, data):
        if self.length == self.size:
            raise StackIsFull

        node = Node(data)
        node.setNext(self.top)
        self.top = node
        self.length += 1

    def pop(self):
        if self.length == 0:
            raise EmptyStack

        data = self.top.getData()
        self.top = self.top.getNext()
        self.length -= 1
        return data

    def traverse(self):
        if self.length == 0:
            print('Stack is empty.')
        else:
            node = self.top
            nodes = []
            while node:
                nodes.append(node.getData())
                node = node.getNext()
            nodes = map(str, nodes)
            print(' -> '.join(nodes))




if __name__ == "__main__":
    s = Stack(10)

    try:
        s.pop()
    except EmptyStack:
        print('EmptyStack exception is raised as expected.')
    else:
        print('ERROR: EmptyStack exception is not raised.')

    for i in range(1, 11):
        s.push(i)

    s.traverse()

    try:
        s.push(11)
    except StackIsFull:
        print('StackIsFull exception is raised as expected.')
    else:
        print('ERROR: StackIsFull exception is not raised.')