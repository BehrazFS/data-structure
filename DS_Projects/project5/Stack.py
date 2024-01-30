from LinkedList import LinkedListNode


class Stack:
    def __init__(self):
        self.list_head = None

    def __repr__(self):
        # for printing O(n)
        head2 = self.list_head
        return_str = "["
        while head2 is not None:
            return_str += str(head2.data) + ("," if head2.next is not None else "")
            head2 = head2.next
        return return_str + "]"

    def __str__(self):
        # for printing O(n)
        head2 = self.list_head
        return_str = "["
        while head2 is not None:
            return_str += str(head2.data) + ("," if head2.next is not None else "")
            head2 = head2.next
        return return_str + "]"

    def push(self, x):
        ll = LinkedListNode()
        ll.data = x
        ll.next = self.list_head
        self.list_head = ll

    def pop(self):
        if not self.is_empty():
            to_pop = self.top()
            self.list_head = self.list_head.next
            return to_pop

    def top(self):
        if not self.is_empty():
            return self.list_head.data

    def is_empty(self):
        if self.list_head is None:
            return True
        else:
            return False
