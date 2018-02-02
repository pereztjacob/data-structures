class Node:

    def __init__(self,data,next):
        self.data = data
        self.next = next

class Linked_List:

    head = None
    tail = None

    def display(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

# ////////////////////////////////////////////////////////////////////////////////////////////////////

    def push(self, data):
                
# ///////////////////////////////////////////////////////////////////////////////////

    def append(self,data):
        node = Node(data,None)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

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

s = Linked_List()
s.push(1)
s.push(3)
s.push(5)
s.display()