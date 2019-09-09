from Node import Node

class EmptyQueue(Exception):
    pass

class QueueIsFull(Exception):
    pass

class Queue(EmptyQueue, QueueIsFull):

    def __init__(self, size):
        self.top = None
        self.length = 0
        self.size = size

    def push(self, data):
        if self.length == self.size:
            raise QueueIsFull

        node = Node(data)
        if self.top == None:
            self.top = node
        else:
            current = self.top
            prev = current
            while current != None:
                prev = current
                current = current.getNext()
            prev.setNext(node)
        self.length += 1

    def pop(self):
        if self.length == 0:
            raise EmptyQueue

        data = self.top.getData()
        self.top = self.top.getNext()
        self.length -= 1
        return data

    def traverse(self):
        if self.length == 0:
            print('Queue is empty.')
        else:
            node = self.top
            nodes = []
            while node:
                nodes.append(node.getData())
                node = node.getNext()
            nodes = map(str, nodes)
            print(' -> '.join(nodes))




if __name__ == "__main__":
    s = Queue(10)

    try:
        s.pop()
    except EmptyQueue:
        print('EmptyQueue exception is raised as expected.')
    else:
        print('ERROR: EmptyQueue exception is not raised.')

    for i in range(1, 11):
        s.push(i)

    s.traverse()

    try:
        s.push(11)
    except QueueIsFull:
        print('QueueIsFull exception is raised as expected.')
    else:
        print('ERROR: QueueIsFull exception is not raised.')