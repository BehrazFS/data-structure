class Linkedlist:
    def __init__(self):
        self.data = ""
        self.next = None


class Stack:
    def __init__(self):
        self.list_head = Linkedlist()

    def push(self, x):
        ll = Linkedlist()
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


my_str = input()
stack = Stack()
for i in range(len(my_str)):
    if my_str[i] == ')':
        temp = ""
        while stack.top() != '(':
            temp = stack.pop() + temp
        stack.pop()
        temp2 = ""
        while not stack.is_empty() and stack.top() in "0123456789":
            temp2 = stack.pop() + temp2
        temp *= int(temp2)
        stack.push(temp)
    else:
        stack.push(my_str[i])
output = ""
while not stack.is_empty():
    output = stack.pop() + output
print(output)