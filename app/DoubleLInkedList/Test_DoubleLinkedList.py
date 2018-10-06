import unittest
from DoubleLInkedListItem import DoubleLinkedListItem
from DoubleLinkedList import DoubleLinkedList


class TestDoubleLinkedList(unittest.TestCase):

    def test_init(self):
        # empty list
        a = DoubleLinkedList()
        self.assertEqual(a.len(), 0)
        self.assertEqual(a.first_item(), None)
        self.assertEqual(a.last_item(), None)

    def test_push_to_empty_list(self):
        # pushing to back/front
        for PushFunc in [DoubleLinkedList.push_back,
                         DoubleLinkedList.push_front]:
            a = DoubleLinkedList()
            PushFunc(a, 1)
            self.assertEqual(a.len(), 1)
            self.assertEqual(a.first(), 1)
            self.assertEqual(a.last(), 1)

    def test_first_last(self):
        # empty list
        a = DoubleLinkedList()
        self.assertEqual(a.first(), None)
        self.assertEqual(a.last(), None)
        self.assertEqual(a.first_item(), None)
        self.assertEqual(a.last_item(), None)
        # one-element list
        a.push_front(2)
        self.assertEqual(a.first(), 2)
        self.assertEqual(a.last(), 2)
        self.assertEqual(a.first_item().get(), 2)
        self.assertEqual(a.last_item().get(), 2)
        # grater than one-element list
        a.push_front(1)
        self.assertEqual(a.first(), 1)
        self.assertEqual(a.last(), 2)
        self.assertEqual(a.first_item().get(), 1)
        self.assertEqual(a.last_item().get(), 2)
        # poping list to make it empty
        for i in range(3):
            a.pop_back()
        # empty list
        self.assertEqual(a.first(), None)
        self.assertEqual(a.last(), None)
        self.assertEqual(a.first_item(), None)
        self.assertEqual(a.last_item(), None)

    def test_pop_from_oneelement_list(self):
        # pushing to front/bck, poping from front/back
        for PushFunc in [DoubleLinkedList.push_back,
                         DoubleLinkedList.push_front]:
            for PopFunc in [DoubleLinkedList.pop_back,
                            DoubleLinkedList.pop_front]:
                # one-element list
                a = DoubleLinkedList()
                PushFunc(a, 1)
                PopFunc(a)
                self.assertEqual(a.len(), 0)
                self.assertEqual(a.first_item(), None)
                self.assertEqual(a.last_item(), None)

    def test_pop_from_push_to_empty_list(self):
        # pushing to front/bck, poping from front/back
        for PushFunc in [DoubleLinkedList.push_back,
                         DoubleLinkedList.push_front]:
            for PopFunc in [DoubleLinkedList.pop_back,
                            DoubleLinkedList.pop_front]:
                # frist, pop from empty list
                a = DoubleLinkedList()
                self.assertEqual(PopFunc(a), None)
                self.assertEqual(a.len(), 0)
                self.assertEqual(a.first_item(), None)
                self.assertEqual(a.last_item(), None)
                # pushing to poped once empty list
                PushFunc(a, 1)
                self.assertEqual(a.len(), 1)
                self.assertEqual(a.first(), 1)
                self.assertEqual(a.last(), 1)

    def test_sequential_push_pop(self):
        # pushing to front/back, poping from front/back
        for PushFunc, PushReverse in [[DoubleLinkedList.push_back, False],
                                      [DoubleLinkedList.push_front, True]]:
            for PopFunc, PopReverse in [[DoubleLinkedList.pop_back, True],
                                        [DoubleLinkedList.pop_front, False]]:
                # pushing a sequence
                a = DoubleLinkedList()
                # the ways of pushing/poping make it possible to have different
                # ordering in pushed and poped sequences
                range1 = range(10)
                if (PushReverse):
                    range1 = reversed(range1)
                range2 = range(10)
                if (PopReverse):
                    range2 = reversed(range2)
                size = 0
                for i in range1:
                    PushFunc(a, i)
                    size += 1
                    self.assertEqual(a.len(), size)
                # poping the same sequence
                for i in range2:
                    self.assertEqual(PopFunc(a), i)
                    size -= 1
                    self.assertEqual(a.len(), size)

    def test_contains(self):
        # check existence of any element in empty list
        a = DoubleLinkedList()
        self.assertEqual(a.contains(0), False)
        # trying to find right element in one-element list
        a.push_front(0)
        self.assertEqual(a.contains(0), True)
        # trying to find false element in one-element list
        self.assertEqual(a.contains(1), False)
        # creating sequence from 0 to 9 in list
        a = DoubleLinkedList()
        for i in range(10):
            a.push_front(i)
        # check numbers from -10 to -1 for inclusion to the list
        for i in range(-10, 0):
            self.assertEqual(a.contains(i), False)
        # check numbers from 0 to 9 for inclusion to the list
        for i in range(10):
            self.assertEqual(a.contains(i), True)
        # check numbers from 10 to 19 for inclusion to the list
        for i in range(10, 20):
            self.assertEqual(a.contains(i), False)

    def is_empty_and_alive(self, check):
        # check empty
        self.assertEqual(check.len(), 0)
        # check workability
        check.push_front(1)
        check.push_back(2)
        self.assertEqual(check.pop_front(), 1)
        self.assertEqual(check.pop_front(), 2)
        self.assertEqual(check.len(), 0)

    def test_delete(self):
        # trying to delete something from empty list
        a = DoubleLinkedList()
        a.delete(DoubleLinkedListItem())
        self.assertEqual(a.len(), 0)
        # check for further workability
        self.is_empty_and_alive(a)
        # trying to delete nonexistent element from one-element list
        a = DoubleLinkedList()
        a.push_back(1)
        a.delete(DoubleLinkedListItem())
        self.assertEqual(a.pop_front(), 1)
        # check for further workability
        self.is_empty_and_alive(a)
        # deleting the only element from the list
        a = DoubleLinkedList()
        a.push_back(1)
        it = a.first_item()
        a.delete(it)
        # check for further workability
        self.is_empty_and_alive(a)
        # Deleting of the middle part of the list:
        a = DoubleLinkedList()
        # creating list
        for i in range(20):
            a.push_back(i)
        it = a.first_item()
        # getting  start item for deletion
        for i in range(5):
            it = it.next()
        # the deletion itself
        for i in range(5, 15):
            next = it.next()
            a.delete(it)
            it = next
        # check the deletion of middle part
        self.assertEqual(a.len(), 10)
        for i in range(0, 5):
            self.assertEqual(a.pop_front(), i)
        for i in range(15, 20):
            self.assertEqual(a.pop_front(), i)
