class Node(object):

    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next

class ListOne(object):

    head = None
    tail = None
    size = 0

# //////////////////// FUNCTIONS//////////////////////

    def display(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

# ////////////////////// APPEND FUNCTIONS ///////////////////////

    def append(self, data):
        node = Node(data, None, None)
        if self.head is None:
            self.head = self.tail = node
        else:
            node.prev = self.tail
            node.next = None
            self.tail.next = node
            self.tail = node
        self.size += 1

    def appendleft(self, data):
        node = Node(data, None, None)
        current_node = self.head
        if self.head is None:
            self.head = node
        else:
            while node.data > current_node.data:
                current_node = current_node.next
            node.prev = current_node.prev
            node.next = current_node
            current_node.prev.next = node
            current_node.prev = node

        self.size += 1

s = ListOne()

s.append(1)
s.append(3)
s.append(5)
s.append(7)
s.append(9)
s.display()
s.appendleft(4)
s.display()