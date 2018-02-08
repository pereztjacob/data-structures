import pytest
import unittest
from priorityq import ListOne

class MyTest(unittest.TestCase):

    def test_insert_1(self):
        l = ListOne()

        l.append(1, 4)
        l.append(2, 3)
        l.append(4, 1)
        l.appendleft(3, 2)

        self.assertEqual(l.head.next.next.priority, 3)