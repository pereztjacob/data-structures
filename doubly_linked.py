class Node(object):

    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next

class ListOne(object):

    head = None
    tail = None
    size = 0

# //////////////////// PEEK FUNCTIONS//////////////////////

    def peekleft(self):
        if self.head is not None:
            print(self.head.data)
        else:
            raise Exception('List empty')

    def peek(self):
        if self.tail is not None:
            print(self.tail.data)
        else:
            raise Exception('List empty')

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
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.size += 1

# ///////////////////// REMOVE FUNCTIONS ///////////////////////

    def pop(self):
        if self.tail is None:
            raise Exception("List empty")
        
        node = self.tail

        if self.tail.prev is not None:
            self.tail.prev.next = None
        self.tail = self.tail = self.tail.prev

        if self.tail is None:
            self.head = None
        
        self.size -= 1
        return node

    def popleft(self):
        if self.head is None:
            return None
        else:
            node = self.head
            self.head = self.head.next
            self.size -= 1
            return node


s = ListOne()

s.append(3)
s.appendleft(2)
s.append(4)
s.appendleft(1)
s.peekleft()
s.peek()
s.pop()
s.popleft()
s.peekleft()
s.peek()