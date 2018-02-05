class Node(object):

    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next

class ListOne(object):

    head = None
    tail = None
    size = 0

    def display(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def add(self, data):
        node = Node(data, None, None)
        if self.head is None:
            self.head = self.tail = node
        else:
            node.prev = self.tail
            node.next = None
            self.tail.next = node
            self.tail = node
        self.size += 1

    def delete(self, node_value):
        current_node = self.head
        while current_node is not None:
            if current_node.data == node_value:
                if current_node.prev is not None:
                    current_node.prev.next = current_node.next
                    current_node.next.prev = current_node.prev
                else:
                    self.head = current_node.next
                    current_node.next.prev = None

            current_node = current_node.next
            self.size -= 1

    def shift(self):

        if self.tail is None:
            raise Exception("empty list")
        
        node = self.tail

        if self.tail.prev is not None:
            self.tail.prev.next = None
        self.tail = self.tail = self.tail.prev

        if self.tail is None:
            self.head = None
        
        self.size -= 1
        return node

    def push(self, data):
        node = Node(data, None, None)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.size += 1

    def pop(self):
        if self.head is None:
            return None
        else:
            node = self.head
            self.head = self.head.next
            self.size -= 1
            return node


s = ListOne()

# s.add(1)
# s.display()
# s.push(2)
# s.display()
# s.add(3)
# s.display()
# s.delete(1)
# s.display()
# s.pop()
# s.display()
# s.shift()
# s.display()

# //////////////////////////// STACK ///////////////////////////////

s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(5)
s.display()
s.shift()
s.shift()
s.shift()
s.display()

# //////////////////////////// QUEUE ///////////////////////////////

# s.add(1)
# s.add(2)
# s.add(3)
# s.add(4)
# s.add(5)
# s.display()
# s.pop()
# s.pop()
# s.pop()
# s.display()