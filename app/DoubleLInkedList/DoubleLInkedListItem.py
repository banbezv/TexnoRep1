class DoubleLinkedListItem(object):

    def __init__(self, value=None):
        self.__next = None
        self.__prev = None
        self.__elem = value

    def set(self, value):
        self.__elem = value

    def get(self):
        return self.__elem

    def next(self):
        return self.__next

    def prev(self):
        return self.__prev

    def set_next(self, ref):
        if (self.next() is not None):
            self.next().__prev = None
        if (ref is not None and ref.prev() is not None):
            ref.prev().__next = None
        self.__next = ref
        if (ref is not None):
            ref.__prev = self

    def set_prev(self, ref):
        if (self.prev() is not None):
            self.prev().__next = None
        if (ref is not None and ref.next() is not None):
            ref.next().__prev = None
        self.__prev = ref
        if (ref is not None):
            ref.__next = self

    def __str__(self):
        ls = ["{"]
        if (self.__prev is None):
            ls.append("N/A")
        else:
            ls.append(str(self.prev().get()))
        ls.append("->[")
        ls.append(str(self.get()))
        ls.append("]->")
        if (self.__next is None):
            ls.append("N/A")
        else:
            ls.append(str(self.next().get()))
        ls.append("}")
        return "".join(ls)
