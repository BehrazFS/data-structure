import os
import random


class LinkedListNode:
    def __init__(self, data=None, next_element=None):
        self.data = data
        self.next = next_element


class LinkedListNodeTwoWay:
    def __init__(self, data=None, next_element=None, previous=None):
        self.data = data
        self.next = next_element
        self.previous = previous


# class GeneralLinkedListNode:
#     def __init__(self, data=None, next_element=None, previous=None, down=None):
#         self.data = data
#         self.next = next_element
#         self.previous = previous
#         self.down = down
#
#
# class GeneralLinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        # for printing O(n)
        head2 = self.head
        return_str = ""
        while head2 is not None:
            return_str += str(head2.data) + ("," if head2.next is not None else "")
            head2 = head2.next
        return return_str

    def __str__(self):
        # for printing O(n)
        head2 = self.head
        return_str = ""
        while head2 is not None:
            return_str += str(head2.data) + ("," if head2.next is not None else "")
            head2 = head2.next
        return return_str

    def __contains__(self, item):
        return self.find(item, is_package=isinstance(item, Package)) is not None

    def make_from_str(self, the_str):
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

    def find(self, item, is_package=False):
        if is_package:
            head2 = self.head
            while head2 is not None:
                if head2.data.compare(item) == 0:
                    return head2.data
                head2 = head2.next
            return None
        else:
            head2 = self.head
            while head2 is not None:
                if head2.data == item:
                    return head2.data
                head2 = head2.next
            return None


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


class Array:
    def __init__(self, n):
        self.size = n
        self.list = [None for i in range(n)]


class ArrayList:
    def __init__(self):
        self.filled = 0
        self.size = 1
        self.list = [None for i in range(self.size)]
        self.changed = True

    def __repr__(self):
        return str(self.list)

    def __str__(self):
        return str(self.list)

    def __contains__(self, item):
        return self.find(item, is_package=isinstance(item, Package)) >= 0

    def __merge_sort(self, start, end):
        if start >= end:
            return
        mid = (start + end) // 2
        self.__merge_sort(start, mid)
        self.__merge_sort(mid + 1, end)
        self.__merge(start, end)

    def __merge(self, start, end):
        mid = (start + end) // 2
        i = start
        j = mid + 1
        arr = ArrayList()
        while i <= mid and j <= end:
            if self.list[i] <= self.list[j]:
                arr.add(self.list[i])
                i += 1
            else:
                arr.add(self.list[j])
                j += 1
        while i <= mid:
            arr.add(self.list[i])
            i += 1
        while j <= end:
            arr.add(self.list[j])
            j += 1
        for k in range(start, end + 1):
            self.list[k] = arr.list[k - start]

    def __merge_sort_package(self, start, end):
        if start >= end:
            return
        mid = (start + end) // 2
        self.__merge_sort_package(start, mid)
        self.__merge_sort_package(mid + 1, end)
        self.__merge_package(start, end)

    def __merge_package(self, start, end):
        mid = (start + end) // 2
        i = start
        j = mid + 1
        arr = ArrayList()
        while i <= mid and j <= end:
            if self.list[i].compare(self.list[j]) <= 0:
                arr.add(self.list[i])
                i += 1
            else:
                arr.add(self.list[j])
                j += 1
        while i <= mid:
            arr.add(self.list[i])
            i += 1
        while j <= end:
            arr.add(self.list[j])
            j += 1
        for k in range(start, end + 1):
            self.list[k] = arr.list[k - start]

    def sort(self, is_package=False):
        if is_package:
            self.__merge_sort_package(0, self.filled - 1)
        else:
            self.__merge_sort(0, self.filled - 1)

    def __binary_search_package(self, start, end, item):
        if start <= end:
            mid = (start + end) // 2
            if self.list[mid].compare(item) == 0:
                return mid
            elif self.list[mid].compare(item) == 1:
                return self.__binary_search_package(start, mid - 1, item)
            elif self.list[mid].compare(item) == -1:
                return self.__binary_search_package(mid + 1, end, item)
        else:
            return -1

    def __binary_search(self, start, end, item):
        if start <= end:
            mid = (start + end) // 2
            if self.list[mid] == item:
                return mid
            elif self.list[mid] > item:
                return self.__binary_search(start, mid - 1, item)
            elif self.list[mid] < item:
                return self.__binary_search(mid + 1, end, item)
        else:
            return -1

    def find(self, item, is_package=False):
        if self.changed:
            self.changed = False
            self.sort(is_package=is_package)
        if is_package:
            return self.__binary_search_package(0, self.filled - 1, item)
        else:
            return self.__binary_search(0, self.filled - 1, item)

    def add(self, element, index=None):
        self.changed = True
        if index is None:
            index = self.filled
        elif index >= self.filled:
            raise IndexError
        self.filled += 1
        if self.filled >= 0.75 * self.size:
            copylist = [None for i in range(2 * self.size)]
            for i in range(self.size):
                copylist[i] = self.list[i]
            self.size *= 2
            self.list = copylist
        if self.list[index] is not None:
            self.filled -= 1
        self.list[index] = element

    def get(self, i, j=None):
        if i >= self.filled or (j is not None and j >= i):
            raise IndexError
        if j is None:
            return self.list[i]
        else:
            return self.list[i:j]

    def __getitem__(self, item):
        return self.list[item]

    def remove_last(self):
        if self.filled == 0:
            raise "nothing to remove"
        self.filled -= 1
        if self.filled <= 0.25 * self.size:
            copylist = [None for i in range(self.size // 2)]
            for i in range(self.size // 2):
                copylist[i] = self.list[i]
            self.size //= 2
            self.list = copylist
        self.list[self.filled] = None


class Package:
    def __init__(self, name="nameless", sender="nobody", receiver="nobody", distance=0, code=-1):
        self.name = name
        self.sender = sender
        self.receiver = receiver
        self.distance = distance
        self.code = code
        self.state = Stack()

    def __lt__(self, other):
        return self.distance < other.distance

    def __le__(self, other):
        return self.distance <= other.distance

    def __gt__(self, other):
        return self.distance > other.distance

    def __ge__(self, other):
        return self.distance >= other.distance

    def __eq__(self, other):
        return self.distance == other.distance

    def __ne__(self, other):
        return self.distance != other.distance

    def compare(self, other):
        if self.code > other.code:
            return 1
        elif self.code < other.code:
            return -1
        else:
            return 0

    def __repr__(self):
        return f"[name : {self.name}, sender : {self.sender}, receiver : {self.receiver}, distance : {self.distance}, " \
               f"code : {self.code}]\n"

    def __str__(self):
        return f"[name : {self.name}, sender : {self.sender}, receiver : {self.receiver}, distance : {self.distance}, " \
               f"code : {self.code}]\n"


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        # for printing O(n)
        head2 = self.head
        return_str = ""
        while head2 is not None:
            return_str += str(head2.data) + ("," if head2.next is not None else "")
            head2 = head2.next
        return return_str

    def __str__(self):
        # for printing O(n)
        head2 = self.head
        return_str = ""
        while head2 is not None:
            return_str += str(head2.data) + ("," if head2.next is not None else "")
            head2 = head2.next
        return return_str

    def enqueue(self, x):
        if not self.is_empty():
            self.head = LinkedListNodeTwoWay(x, self.head)
            self.head.next.previous = self.head
        else:
            self.head = LinkedListNodeTwoWay(x)
            self.tail = self.head

    def dequeue(self):
        if not self.is_empty() and self.tail.previous is not None:
            temp = self.tail
            self.tail = self.tail.previous
            self.tail.next = None
            return temp.data
        elif not self.is_empty():
            data = self.tail.data
            self.head = None
            self.tail = None
            return data
        else:
            raise "Queue is empty"

    def front(self):
        if not self.is_empty():
            return self.tail.data

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def delete(self, item, is_package=False):
        if is_package:
            if not self.is_empty():
                if self.head.data.compare(item) == 0:
                    self.head = self.head.next
                    return True
                if self.tail.data.compare(item) == 0:
                    self.tail = self.tail.previous
                    self.tail.next = None
                    return True
                head2 = self.head
                while head2.next is not None:
                    if head2.next.data.compare(item) == 0:
                        head2.next = head2.next.next
                        head2.next.previous = head2
                        return True
                    head2 = head2.next
                return False
            else:
                return False
        else:
            if not self.is_empty():
                if self.head.data == item:
                    self.head = self.head.next
                    return True
                if self.tail.data == item:
                    self.tail = self.tail.previous
                    self.tail.next = None
                    return True
                head2 = self.head
                while head2.next is not None:
                    if head2.next.data == item:
                        head2.next = head2.next.next
                        head2.next.previous = head2
                        return True
                    head2 = head2.next
                return False
            else:
                return False


class MinHeap:
    def __init__(self):
        self.array = ArrayList()

    def __repr__(self):
        return str(self.array)

    def __str__(self):
        return str(self.array)

    def insert(self, x):
        self.array.add(x)
        k = self.array.filled - 1
        while (k - 1) // 2 >= 0 and self.array[k] < self.array[(k - 1) // 2]:
            temp = self.array[k]
            self.array.add(self.array[(k - 1) // 2], k)
            self.array.add(temp, (k - 1) // 2)
            k = (k - 1) // 2

    def remove_root(self):
        data = self.array[0]
        s = self.array.filled - 1
        self.array.add(self.array[s], 0)
        self.array.remove_last()
        s = self.array.filled - 1
        k = 0
        while True:
            if s < 2 * k + 1 and s < 2 * k + 2:
                break
            a = self.array[2 * k + 1]
            if 2 * k + 1 <= s < 2 * k + 2:
                if a < self.array[k]:
                    temp = self.array[k]
                    self.array.add(a, k)
                    self.array.add(temp, 2 * k + 1)
                break
            b = self.array[2 * k + 2]
            if a <= b and a < self.array[k]:
                temp = self.array[k]
                self.array.add(a, k)
                self.array.add(temp, 2 * k + 1)
                k = 2 * k + 1
            elif b < a and b < self.array[k]:
                temp = self.array[k]
                self.array.add(b, k)
                self.array.add(temp, 2 * k + 2)
                k = 2 * k + 2
            else:
                break
        return data

    def remove(self, item, is_package=False):
        data = None
        k2 = 0
        for i in range(self.array.filled):
            if is_package:
                if self.array[i].compare(item) == 0:
                    data = self.array[i]
                    k2 = i
                    break
            else:
                if self.array[i] == item:
                    data = self.array[i]
                    k2 = i
                    break
        if data is not None:
            s = self.array.filled - 1
            self.array.add(self.array[s], k2)
            self.array.remove_last()
            if k2 == s:
                return data
            s = self.array.filled - 1
            k = k2
            while (k - 1) // 2 >= 0 and self.array[k] < self.array[(k - 1) // 2]:
                temp = self.array[k]
                self.array.add(self.array[(k - 1) // 2], k)
                self.array.add(temp, (k - 1) // 2)
                k = (k - 1) // 2
            k = k2
            while True:
                if s < 2 * k + 1 and s < 2 * k + 2:
                    break
                a = self.array[2 * k + 1]
                if 2 * k + 1 <= s < 2 * k + 2:
                    if a < self.array[k]:
                        temp = self.array[k]
                        self.array.add(a, k)
                        self.array.add(temp, 2 * k + 1)
                    break
                b = self.array[2 * k + 2]
                if a <= b and a < self.array[k]:
                    temp = self.array[k]
                    self.array.add(a, k)
                    self.array.add(temp, 2 * k + 1)
                    k = 2 * k + 1
                elif b < a and b < self.array[k]:
                    temp = self.array[k]
                    self.array.add(b, k)
                    self.array.add(temp, 2 * k + 2)
                    k = 2 * k + 2
                else:
                    break
        return data

    def get_root(self):
        return self.array[0]


class MaxHeap:
    def __init__(self):
        self.array = ArrayList()

    def __repr__(self):
        return str(self.array)

    def __str__(self):
        return str(self.array)

    def insert(self, x):
        self.array.add(x)
        k = self.array.filled - 1
        while (k - 1) // 2 >= 0 and self.array[k] > self.array[(k - 1) // 2]:
            temp = self.array[k]
            self.array.add(self.array[(k - 1) // 2], k)
            self.array.add(temp, (k - 1) // 2)
            k = (k - 1) // 2

    def remove_root(self):
        data = self.array[0]
        s = self.array.filled - 1
        self.array.add(self.array[s], 0)
        self.array.remove_last()
        s = self.array.filled - 1
        k = 0
        while True:
            if s < 2 * k + 1 and s < 2 * k + 2:
                break
            a = self.array[2 * k + 1]
            if 2 * k + 1 <= s < 2 * k + 2:
                if a > self.array[k]:
                    temp = self.array[k]
                    self.array.add(a, k)
                    self.array.add(temp, 2 * k + 1)
                break
            b = self.array[2 * k + 2]
            if a >= b and a > self.array[k]:
                temp = self.array[k]
                self.array.add(a, k)
                self.array.add(temp, 2 * k + 1)
                k = 2 * k + 1
            elif b > a and b > self.array[k]:
                temp = self.array[k]
                self.array.add(b, k)
                self.array.add(temp, 2 * k + 2)
                k = 2 * k + 2
            else:
                break
        return data

    def remove(self, item, is_package=False):
        data = None
        k2 = 0
        for i in range(self.array.filled):
            if is_package:
                if self.array[i].compare(item) == 0:
                    data = self.array[i]
                    k2 = i
                    break
            else:
                if self.array[i] == item:
                    data = self.array[i]
                    k2 = i
                    break
        if data is not None:
            s = self.array.filled - 1
            self.array.add(self.array[s], k2)
            self.array.remove_last()
            if k2 == s:
                return data
            s = self.array.filled - 1
            k = k2
            while (k - 1) // 2 >= 0 and self.array[k] > self.array[(k - 1) // 2]:
                temp = self.array[k]
                self.array.add(self.array[(k - 1) // 2], k)
                self.array.add(temp, (k - 1) // 2)
                k = (k - 1) // 2
            k = k2
            while True:
                if s < 2 * k + 1 and s < 2 * k + 2:
                    break
                a = self.array[2 * k + 1]
                if 2 * k + 1 <= s < 2 * k + 2:
                    if a > self.array[k]:
                        temp = self.array[k]
                        self.array.add(a, k)
                        self.array.add(temp, 2 * k + 1)
                    break
                b = self.array[2 * k + 2]
                if a >= b and a > self.array[k]:
                    temp = self.array[k]
                    self.array.add(a, k)
                    self.array.add(temp, 2 * k + 1)
                    k = 2 * k + 1
                elif b > a and b > self.array[k]:
                    temp = self.array[k]
                    self.array.add(b, k)
                    self.array.add(temp, 2 * k + 2)
                    k = 2 * k + 2
                else:
                    break
        return data

    def get_root(self):
        return self.array[0]


try:
    codes = ArrayList()
    Q = Queue()
    MiH = MinHeap()
    MaH = MaxHeap()
    list_archive = LinkedList()
    array_archive = ArrayList()
    low = 100000
    high = 999999
    # low = 0
    # high = 5
    exited = False
    while not exited:
        menu = """   Menu:
        [1]:Receive new package
        [2]:Send package
        [3]:Register New Status
        [4]:Track the status of the shipment
        [5]:Archive of Packages
        [6]:Exit
        [7]:Clear console"""
        print(menu)
        choice = input("   action : ")
        if choice == "1":
            name = input("name : ")
            sender = input("sender : ")
            receiver = input("receiver : ")
            distance = int(input("distance : "))
            if codes.filled == high - low + 1:
                print("reached maximum number of packages")
                break
            code = random.randint(low, high)
            while code in codes:
                code = random.randint(low, high)
            codes.add(code)
            package = Package(name, sender, receiver, distance, code)
            Q.enqueue(package)
            MiH.insert(package)
            MaH.insert(package)
            list_archive.insert_at_start(package)
            array_archive.add(package)
        elif choice == "2":
            priority = input("    [1]:first in\n    [2]:minimum distance\n    [3]:maximum distance\n   action : ")
            if Q.is_empty():
                print("nothing to send")
            else:
                if priority == "1":
                    var = Q.front()
                    print("   ", Q.front())
                    ans = input("    [1]:send package\n    [2]:cancel\n   action : ")
                    if ans == "1":
                        print("   package sent")
                        Q.dequeue()
                        MiH.remove(var, is_package=True)
                        MaH.remove(var, is_package=True)
                    elif ans == "2":
                        print("   canceled")
                    else:
                        print("   invalid action")
                elif priority == "2":
                    var = MiH.get_root()
                    print("   ", MiH.get_root())
                    ans = input("    [1]:send package\n    [2]:cancel\n   action : ")
                    if ans == "1":
                        print("   package sent")
                        Q.delete(var, is_package=True)
                        MiH.remove_root()
                        MaH.remove(var, is_package=True)
                    elif ans == "2":
                        print("   canceled")
                    else:
                        print("   invalid action")
                elif priority == "3":
                    var = MaH.get_root()
                    print("   ", MaH.get_root())
                    ans = input("    [1]:send package\n    [2]:cancel\n   action : ")
                    if ans == "1":
                        print("   package sent")
                        Q.delete(var, is_package=True)
                        MiH.remove(var, is_package=True)
                        MaH.remove_root()
                    elif ans == "2":
                        print("   canceled")
                    else:
                        print("   invalid action")
                else:
                    print("   invalid action")
        elif choice == "3":
            p_code = int(input("code : "))
            state = input("state : ")
            ans = input("    [1]:ArrayList search\n    [2]:LinkedList search\n   action : ")
            if ans == "1":
                x = Package(code=p_code)
                n = array_archive.find(x, is_package=True)
                if n == -1:
                    print("   Package not found")
                else:
                    if array_archive[n].state.top() != "delivered":
                        array_archive[n].state.push(state)
                    else:
                        print("   Package already delivered")
            elif ans == "2":
                x = Package(code=p_code)
                x = list_archive.find(x, is_package=True)
                if x is None:
                    print("   Package not found")
                else:
                    if x.state.top() != "delivered":
                        x.state.push(state)
                    else:
                        print("   Package already delivered")
            else:
                print("   invalid action")
        elif choice == "4":
            p_code = int(input("code : "))
            ans = input("    [1]:ArrayList search\n    [2]:LinkedList search\n   action : ")
            if ans == "1":
                x = Package(code=p_code)
                n = array_archive.find(x, is_package=True)
                if n == -1:
                    print("   Package not found")
                else:
                    print(array_archive[n].state)
            elif ans == "2":
                x = Package(code=p_code)
                x = list_archive.find(x, is_package=True)
                if x is None:
                    print("   Package not found")
                else:
                    print(x.state)
            else:
                print("   invalid action")
        elif choice == "5":
            ans = input("    [1]:ArrayList archive\n    [2]:LinkedList archive\n   action : ")
            if ans == "1":
                print(array_archive)
            elif ans == "2":
                print(list_archive)
            else:
                print("   invalid action")
        elif choice == "6":
            exited = True
        elif choice == "7":
            os.system("cls")
        else:
            print("   invalid action")
except Exception as ex:
    print("something went wrong", "\n", ex)
