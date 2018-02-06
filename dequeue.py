class Node(object):
    """ Node in deque list """
    _next = None
    _value = 0

    def __init__(self, value):
        self._value = value

    @property
    def next(self):
        return self.next

    @next.setter
    def next(self, next):
        self._next = next

    @property
    def value(self):
        return self._value

    @value.setter
    def next(self, value):
        self._value() = value

    class Deque(object):
        """ Define DQ list """

    _size = 0
    _head = None
    _tail = None

    def __init__(self):
        pass

    def __len__(self):
        return self._size

    def add_first(self, node):
        if _head is None:
            _head = _tail = node
        else:
            node = _head
            _head = node
        self._size += 1

    def add_last(self, node):
        if _head is None:
            _head = _tail = node
        else:
            self._tail.next = node
            self._tail = node
        self._size += 1

    def pop(self):
        if self._head is None:
            return None
        if self._head == self._tail:
            self._head = self._tail = None
        else:
            self._head = self._head.next


d = Deque()
len(d)