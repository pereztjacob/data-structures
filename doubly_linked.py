class Node(object):

    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next

class ListOne(object):

    head = None
    tail = None

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

    def shift(self):

        if self.tail is None:
            raise Exception("empty list")
        
        node = self.tail

        if self.tail.prev is not None:
            self.tail.prev.next = None
        self.tail = self.tail = self.tail.prev

        if self.tail is None:
            self.head = None
        
        return node

s = ListOne()
s.add(31)
s.add(2)
s.add(3)
s.add(4)

s.display()
print("::::::::")
s.delete(31)
s.shift()
s.display()