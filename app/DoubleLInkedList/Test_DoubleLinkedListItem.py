import unittest
from DoubleLInkedListItem import DoubleLinkedListItem


class TestDoubleLInkedListItem(unittest.TestCase):

    def test_set_get(self):
        a = DoubleLinkedListItem()
        self.assertEqual(a.get(), None)  # start with None
        a.set(1)
        self.assertEqual(a.get(), 1)
        a.set(2)
        self.assertEqual(a.get(), 2)

    def test_init(self):
        a = DoubleLinkedListItem()
        self.assertEqual(a.prev(), None)  # start alone
        self.assertEqual(a.next(), None)  # start alone

    def test_set_next(self):
        a = DoubleLinkedListItem()
        b = DoubleLinkedListItem()
        c = DoubleLinkedListItem()
        a.set_next(b)  # set link
        self.assertEqual(a.next(), b)
        self.assertEqual(b.prev(), a)
        b.set_next(c)  # set 2nd link
        a.set_next(c)  # reset two link2 to one, b is alone now
        self.assertEqual(a.next(), c)
        self.assertEqual(c.prev(), a)
        self.assertEqual(b.next(), None)
        self.assertEqual(b.prev(), None)
        a.set_next(None)  # split chain
        self.assertEqual(a.next(), None)
        self.assertEqual(c.prev(), None)

    def test_set_prev(self):
        # symmetrically like test_set_next
        a = DoubleLinkedListItem()
        b = DoubleLinkedListItem()
        c = DoubleLinkedListItem()
        c.set_prev(b)
        self.assertEqual(c.prev(), b)
        self.assertEqual(b.next(), c)
        b.set_prev(a)
        c.set_prev(a)
        self.assertEqual(c.prev(), a)
        self.assertEqual(a.next(), c)
        self.assertEqual(b.next(), None)
        self.assertEqual(b.prev(), None)
        c.set_prev(None)
        self.assertEqual(c.prev(), None)
        self.assertEqual(a.next(), None)
