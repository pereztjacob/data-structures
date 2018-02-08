class Node(object):

    def __init__(self, priority, prev, next, data):
        self.priority = priority
        self.prev = prev
        self.next = next
        self.data = data

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

    def append(self, priority, data):
        node = Node(priority, None, None, data)
        if self.head is None:
            self.head = self.tail = node
        else:
            node.prev = self.tail
            node.next = None
            self.tail.next = node
            self.tail = node
        self.size += 1

    def appendleft(self, priority, data):
        node = Node(priority, None, None, data)
        current_node = self.head
        if self.head is None:
            self.head = node
        else:
            while node.priority > current_node.priority:
                current_node = current_node.next
            node.prev = current_node.prev
            node.next = current_node
            current_node.prev.next = node
            current_node.prev = node

        self.size += 1

s = ListOne()

s.append(1, 4)
s.append(2, 3)
s.append(4, 1)
s.appendleft(3, 2)
s.display()