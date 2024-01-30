class LinkedListNode:
    def __init__(self, data=None, next_element=None):
        self.data = data
        self.next = next_element


class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        return str(self)

    def __str__(self):
        # for printing O(n)
        head2 = self.head
        return_str = "["
        while head2 is not None:
            return_str += str(head2.data) + ("," if head2.next is not None else "")
            head2 = head2.next
        return_str += "]"
        return return_str

    def __iter__(self):
        cur_node = self.head
        while cur_node:
            yield cur_node.data
            cur_node = cur_node.next

    def __contains__(self, item):
        return self.find(item) is not None

    def __len__(self):
        return self.get_count()

    def make_from_str(self, the_str):
        the_str = the_str[1:-1]
        the_str += ","
        # to create from input O(n)
        head2 = LinkedListNode()
        head3 = head2
        j = 0
        for i in range(len(the_str)):
            if the_str[i] == ',':
                head2.next = LinkedListNode()
                head2.next.data = the_str[j:i]
                j = i + 1
                head2 = head2.next
        head3 = head3.next
        self.head = head3

    def get_count(self):
        head2 = self.head
        count = 0
        while head2 is not None:
            count += 1
            head2 = head2.next
        return count

    def __reverse(self, lln):
        if lln is None or lln.next is None:
            return lln
        reversed_list = self.__reverse(lln.next)
        lln.next.next = lln
        lln.next = None
        return reversed_list

    def reverse(self):
        self.head = self.__reverse(self.head)

    def insert_at_start(self, x):
        if self.head is None:
            self.head = LinkedListNode(x)
        else:
            self.head = LinkedListNode(x, self.head)

    def remove_head(self):
        if self.head is None:
            return None
        else:
            ret = self.head.data
            self.head = self.head.next
            return ret

    def remove_all(self, x):
        if self.head is None:
            return None
        ret = None
        while self.head.data == x:
            ret = self.head.data
            self.head = self.head.next
        head2 = self.head
        while head2.next is not None:
            if head2.next.data == x:
                ret = head2.next.data
                head2.next = head2.next.next
            else:
                head2 = head2.next
        return ret

    def remove(self, x):
        if self.head is None:
            return None
        if self.head.data == x:
            ret = self.head.data
            self.head = self.head.next
            return ret
        head2 = self.head
        while head2.next is not None:
            if head2.next.data == x:
                ret = head2.next.data
                head2.next = head2.next.next
                return ret
            head2 = head2.next
        return None

    def __getitem__(self, index: int):
        length = self.get_count()
        if index < 0:
            index = length + index
        if index < 0 or index >= length:
            raise IndexError
        i = index
        head2 = self.head
        while i > 0:
            head2 = head2.next
            i -= 1
        return head2.data

    def __setitem__(self, index: int, value):
        length = self.get_count()
        if index < 0:
            index = length + index
        if index < 0 or index >= length:
            raise IndexError
        i = index
        head2 = self.head
        while i > 0:
            head2 = head2.next
            i -= 1
        head2.data = value

    def find(self, item):
        head2 = self.head
        while head2 is not None:
            if head2.data == item:
                return head2
            head2 = head2.next
        return None
