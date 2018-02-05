class Node:

    def __init__(self,data,next):
        self.data = data
        self.next = next

class Linked_List:

    head = None
    tail = None
    size = 0

    def display(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def push(self, data):
        node = Node(data, None)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.size += 1
                
    def append(self,data):
        node = Node(data,None)
        if self.head is None:
            self.head = self.tail = node
        else:
            current_node = self.head
            while current_node is not None:
                if current_node.next is None:
                    current_node.next = node
                    break
                else:
                    current_node = current_node.next
        self.size += 1

    def pop(self):
        if self.head is None:
            return None
        else:
            node = self.head
            self.head = self.head.next
            self.size -= 1
            return node

    def remove(self, node_value):
        current_node = self.head
        previous_node = None
        while current_node is not None:
            if current_node.data == node_value:
                if previous_node is not None:
                    previous_node.next = current_node.next
                else:
                    self.head = current_node.next

            previous_node = current_node
            current_node = current_node.next
            self.size -= 1

    def _size(self):
        print(self.size)

s = Linked_List()
s.push(1)
s.push(3)
s.push(5)
s.pop()
s.append(7)
s.display()
s._size()

