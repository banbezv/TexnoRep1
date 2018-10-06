from DoubleLInkedListItem import DoubleLinkedListItem


class DoubleLinkedList(object):

    def __init__(self):
        self.__head = DoubleLinkedListItem() # dummy node
        self.__tail = self.__head
        self.__len = 0

    def push_front(self, value):
        # adding node before head
        new_head = DoubleLinkedListItem()
        new_head.set_next(self.__head)
        new_head.set(value)
        self.__head = new_head
        self.__len += 1

    def push_back(self, value):
        # making tail a natural node and adding a dummy node after it
        new_tail = DoubleLinkedListItem()
        self.__tail.set_next(new_tail)
        self.__tail.set(value)
        self.__tail = new_tail
        self.__len += 1

    def first_item(self):
        #
        if (self.__head is self.__tail):
            return None
        return self.__head

    def last_item(self):
        if (self.__head is self.__tail):
            return None
        return self.__tail.prev()

    def first(self):
        item = self.first_item()
        if (item is None):
            return None
        return item.get()

    def last(self):
        item = self.last_item()
        if (item is None):
            return None
        return item.get()

    def pop_front(self):
        if (self.__head is self.__tail):
            return None
        value = self.first_item().get()
        self.__head = self.__head.next()
        self.__len -= 1
        return value

    def pop_back(self):
        if (self.__head is self.__tail):
            return None
        value = self.last_item().get()
        self.__tail = self.__tail.prev()
        self.__tail.set(None)
        self.__len -= 1
        return value

    def len(self):
        return self.__len

    def contains(self, value):
        if (self.len() == 0):
            return False
        temp = self.first_item()
        while (temp is not self.__tail):
            if (temp.get() == value):
                return True
            temp = temp.next()
        return False

    def delete(self, item):
        if (self.len() == 0):
            return
        if (item is self.__head):
            self.pop_front()
            return
        temp = self.first_item().next()
        while (temp is not self.__tail):
            if (temp is item):
                temp.prev().set_next(temp.next())
                self.__len -= 1
                return
            temp = temp.next()
