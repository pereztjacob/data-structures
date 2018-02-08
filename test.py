import pytest
import unittest
from doubly_linked import ListOne

class MyTest(unittest.TestCase):

    def test_insert_1(self):
        l = ListOne()

        l.append(1)
        l.append(3)
        l.appendleft(2)

        self.assertEqual(l.head.next.data, 2)