import tkinter
from tkinter import scrolledtext


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
        # ans = False
        # for i in self.list:
        #     if (i is not None) and i == item:
        #         ans = True
        #         break
        # return ans
        return self.find(item) >= 0

    def __iter__(self):
        return iter(self.list)

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

    def sort(self):
        self.__merge_sort(0, self.filled - 1)

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

    def find(self, item):
        if self.changed:
            self.changed = False
            self.sort()
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


def unique(array):
    arr = ArrayList()
    for i in array:
        if (i is not None) and (i not in arr):
            arr.add(i)
    return arr


def is_number(string):
    ret = True
    for i in string:
        if i not in "01234567889":
            ret = False
            break
    return ret


class Book:
    def __init__(self, name="nameless", writer="nobody", price=-1):
        self.name = name
        self.writer = writer
        self.price = price

    def __lt__(self, other):
        return self.price < other

    def __le__(self, other):
        return self.price <= other

    def __gt__(self, other):
        return self.price > other

    def __ge__(self, other):
        return self.price >= other

    def __eq__(self, other):
        return self.name == other

    def __ne__(self, other):
        pass

    def __repr__(self):
        return f"[name : {self.name}, writer : {self.writer}, price : {self.price}$]\n"

    def __str__(self):
        return f"[name : {self.name}, writer : {self.writer}, price : {self.price}$]\n"


class TrieNode:
    def __init__(self, data="", is_word=False):
        self.data = data
        self.children = [None for i in range(len(" abcdefghijklmnopqrstuvwxyz"))]
        self.is_word = is_word


def value_of(val):
    s = " abcdefghijklmnopqrstuvwxyz"
    for i in range(len(s)):
        if val == s[i]:
            return i
    return -1


def reverse(string):
    return string[::-1]


class Trie:
    def __init__(self, all_finder=False):
        self.head = TrieNode()
        self.all_finder = all_finder

    def preorder(self, node):
        ret = ""
        head2 = node
        if head2 is None:
            return ""
        ret += head2.data
        ret += "\n"
        for i in head2.children:
            if i is not None:
                ret += self.preorder(i) + "\n"
        return ret

    def __repr__(self):
        return self.preorder(self.head)

    def __str__(self):
        return self.preorder(self.head)

    def complete(self, node, value, array):
        head2 = node
        if head2 is None:
            return
        else:
            has_child = True
            while len(value) > 0 and has_child:
                has_child = False
                for i in head2.children:
                    if (i is not None) and value[0] == i.data[-1]:
                        head2 = i
                        value = value[1:]
                        has_child = True
                        break
            if head2.is_word and len(value) == 0:
                array.add(head2.data)
            for i in head2.children:
                if i is not None and (has_child if not self.all_finder else True):
                    self.complete(i, value, array)

    def insert(self, value):
        head2 = self.head
        to_insert = ""
        if head2 is None:
            return
        else:
            has_child = True
            while len(value) > 0 and has_child:
                has_child = False
                for i in head2.children:
                    if (i is not None) and value[0] == i.data[-1]:
                        head2 = i
                        to_insert += value[0]
                        value = value[1:]
                        has_child = True
                        break
            if len(value) == 0:
                head2.is_word = True
            if len(value) > 0:
                for i in value:
                    head2.children[value_of(i)] = TrieNode(to_insert + i, False)
                    to_insert += i
                    head2 = head2.children[value_of(i)]
                head2.is_word = True

    def delete(self, value):
        head2 = self.head
        if head2 is None:
            return
        else:
            has_child = True
            while len(value) > 0 and has_child:
                has_child = False
                for i in head2.children:
                    if (i is not None) and value[0] == i.data[-1]:
                        head2 = i
                        value = value[1:]
                        has_child = True
                        break
            if len(value) == 0:
                head2.is_word = False

    def clear(self):
        self.head = TrieNode()


class Node:
    def __init__(self, data=None, is_book=False):
        self.is_book = is_book
        self.data = data
        self.children = ArrayList()


class Tree:
    def __init__(self):
        self.head = Node("root")

    def preorder(self, node):
        ret = ""
        head2 = node
        if head2 is None:
            return ""
        ret += str(head2.data)
        ret += "\n"
        for i in head2.children:
            if i is not None:
                ret += self.preorder(i) + "\n"
        return ret

    def __repr__(self):
        return self.preorder(self.head)

    def __str__(self):
        return self.preorder(self.head)

    def insert(self, node_name, data, is_book=False):
        if not self.find(data, is_book=is_book) and self.find(node_name, is_book=False):
            self.__insert(self.head, node_name, data, is_book)
        else:
            raise MyException("invalid insert")

    def __insert(self, node, node_name, data, is_book=False):
        if node is None:
            return
        elif node.data == node_name:
            node.children.add(Node(data, is_book))
        else:
            for i in node.children:
                self.__insert(i, node_name, data, is_book)

    def __find(self, node, data, is_book=False):
        if node is None:
            return False
        elif node.data == data:
            return True
        else:
            ret = False
            for i in node.children:
                ret = (ret or self.__find(i, data, is_book))
                if ret:
                    break
            return ret

    def find(self, data, is_book=False):
        return self.__find(self.head, data, is_book=is_book)

    def __delete(self, node, data):
        if node is None:
            return
        elif data == "root":
            self.head.children = ArrayList()
            return
        else:
            for i in range(node.children.filled):
                if node.children[i] is not None and node.children[i].data == data:
                    ret = node.children[i]
                    node.children.add(node.children[node.children.filled - 1], i)
                    node.children.remove_last()
                    return ret
            for i in node.children:
                ret = self.__delete(i, data)
                if ret is not None:
                    return ret
            return

    def delete(self, data):
        return self.__delete(self.head, data)

    def __get_books_by_category(self, node, category_name, array):
        if node is None:
            return
        elif node.data == category_name:
            self.__get_books(node, array)
            return
        else:
            for i in node.children:
                self.__get_books_by_category(i, category_name, array)

    def get_books_by_category(self, category_name, array):
        if self.find(category_name, is_book=False):
            self.__get_books_by_category(self.head, category_name, array)

    def __get_books(self, node, array):
        if node is None:
            return
        else:
            if node.is_book:
                array.add(node.data)
            for i in node.children:
                self.__get_books(i, array)

    def __get_book(self, node, name):
        if node is None:
            return
        else:
            if node.is_book and node.data == name:
                return node.data
            for i in node.children:
                ret = self.__get_book(i, name)
                if ret is not None:
                    return ret

    def get_book(self, name):
        if self.find(name, is_book=True):
            return self.__get_book(self.head, name)


class MyException(Exception):
    def __init__(self, message, errors=None):
        super().__init__(message)
        self.errors = errors
        err = tkinter.Toplevel(win)
        err.resizable(False, False)
        err.title("error")
        err.geometry("250x50")
        err.grab_set()
        err_label = tkinter.Label(err, text=message + "\nexception occurred", font=("default", 15))
        err_label.pack()
        err.mainloop()


class BinarySearchNode:
    def __init__(self, data=None, left=None, right=None):
        self.left = left
        self.right = right
        self.data = data


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def in_order(self, node):
        if node is None:
            return
        self.in_order(node.left)
        print(node.data)
        self.in_order(node.right)

    def insert(self, value):
        self.root = self.__insert(self.root, value)

    def __insert(self, node, value):
        if node is None:
            return BinarySearchNode(value)
        if node.data >= value:
            node.left = self.__insert(node.left, value)
        elif node.data < value:
            node.right = self.__insert(node.right, value)
        return node

    def delete(self, value):
        self.root = self.__delete(self.root, value)

    def __delete(self, node, name):
        if node is None:
            return node
        if name == node.data:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                temp = self.__find_min(node.right)
                node.data = temp.data
                node.right = self.__delete(node.right, temp.data)
        else:
            node.left = self.__delete(node.left, name)
            node.right = self.__delete(node.right, name)

        return node

    def __find_min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def clear(self):
        self.root = None

    def __get_lower_values(self, node, value, array):
        if node is None:
            return
        if node.data > value:
            self.__get_lower_values(node.left, value, array)
        elif node.data <= value:
            array.add(node.data)
            self.__get_lower_values(node.left, value, array)
            self.__get_lower_values(node.right, value, array)

    def get_lower_values(self, value):
        arr = ArrayList()
        self.__get_lower_values(self.root, value, arr)
        return arr


win = tkinter.Tk()
win.geometry("465x270")
win.resizable(False, False)
win.title("Guilan book")
main_frame = tkinter.Frame(win, bd=1, bg='black', height=20)


# commands:
def add_panel():
    by_book.forget()
    remove.forget()
    category.forget()
    by_budget.forget()
    add.pack(pady=0, padx=0, fill='both', expand=True, side="bottom")  # pady = 0


def delete_panel():
    by_book.forget()
    by_budget.forget()
    add.forget()
    category.forget()
    remove.pack(pady=0, padx=0, fill='both', expand=True, side="bottom")  # pady = 0


def search_panel():
    add.forget()
    by_budget.forget()
    remove.forget()
    category.forget()
    by_book.pack(pady=0, padx=0, fill='both', expand=True, side="bottom")  # pady = 0


def search_panel_category():
    by_book.forget()
    by_budget.forget()
    add.forget()
    remove.forget()
    category.pack(pady=0, padx=0, fill='both', expand=True, side="bottom")  # pady = 0


def budget_panel():
    by_book.forget()
    add.forget()
    remove.forget()
    category.forget()
    by_budget.pack(pady=0, padx=0, fill='both', expand=True, side="bottom")  # pady = 0


command_frame = tkinter.Frame(main_frame, bd=1, bg='black', height=20)
add_button = tkinter.Button(command_frame, text="new", command=add_panel, fg="yellow", bg="black", bd=2)
add_button.pack(side="left", padx=1)
remove_button = tkinter.Button(command_frame, text="delete", command=delete_panel, fg="yellow", bg="black", bd=2)
remove_button.pack(side="left", padx=1)
search_button = tkinter.Button(command_frame, text="search", command=search_panel, fg="yellow", bg="black", bd=2)
search_button.pack(side="left", padx=1)
search_button_category = tkinter.Button(command_frame, text=" by category", command=search_panel_category, fg="yellow",
                                        bg="black", bd=2)
search_button_category.pack(side="left", padx=1)
budget_button = tkinter.Button(command_frame, text="by budget", command=budget_panel, fg="yellow", bg="black", bd=2)
budget_button.pack(side="left", padx=1)
check_val = tkinter.IntVar()


def checked_auto():
    if check_val.get() == 1:
        category_trie.all_finder = True
        book_trie.all_finder = True
        category_trie_reverse.all_finder = True
        book_trie_reverse.all_finder = True
    elif check_val.get() == 0:
        category_trie.all_finder = False
        book_trie.all_finder = False
        category_trie_reverse.all_finder = False
        book_trie_reverse.all_finder = False


check = tkinter.Checkbutton(command_frame, text="full auto complete (slower)", variable=check_val, onvalue=1,
                            offvalue=0, bd=2, bg="black", fg="yellow", selectcolor="black", relief="raised",
                            command=checked_auto)
check.pack(side="right", padx=1)
command_frame.pack(pady=0, padx=0, fill='x', expand=False, side="top")  # pady = 0
# add
add = tkinter.Frame(main_frame, bd=1, bg='black')
add.pack(pady=0, padx=0, fill='both', expand=True, side="bottom")  # pady = 0
add_label = tkinter.Label(add, text="Adding new item : Press enter to add")
add_label.pack(side="top", fill='x', padx=1)
ent_frame = tkinter.Frame(add, bd=1, bg='black', width=20)
add_ent = tkinter.Entry(ent_frame, width=10, font=("default", 13))
add_ent2 = tkinter.Entry(ent_frame, width=10, font=("default", 13))
plh1 = "add to:"
plh2 = "new item name:"
add_ent.insert(0, plh1)
add_ent2.insert(0, plh2)
suggest_label = scrolledtext.ScrolledText(add, height=6, font=("Times New Roman", 15))
suggest_label.tag_configure('tag-center', justify='center')
suggest_label.tag_configure('tag-left', justify='left')
suggest_label.tag_configure('tag-right', justify='right')
suggest_label.insert(tkinter.INSERT, "suggest    ", "tag-right")
suggest_label.configure(state='disabled')
suggest_label.pack(side="bottom", fill='x')


def enter_pressed(event):
    if add_ent.get() != "" and add_ent2.get() != "" and add_ent.get() != plh1 and add_ent2.get() != plh2:
        for i in add_ent.get():
            if value_of(i) == -1:
                raise MyException("invalid name")
        for i in add_ent2.get():
            if value_of(i) == -1:
                raise MyException("invalid name")
        if v.get() == "1":
            category_trie.insert(add_ent2.get())
            category_trie_reverse.insert(reverse(add_ent2.get()))
            tree.insert(add_ent.get(), add_ent2.get(), False)
        elif v.get() == "2":
            book = Book(add_ent2.get())
            tree.insert(add_ent.get(), book, True)
            book_trie.insert(add_ent2.get())
            book_trie_reverse.insert(reverse(add_ent2.get()))
            book_win = tkinter.Toplevel(win)
            book_win.geometry("230x180")
            book_win.resizable(False, False)
            book_win.title("new book")
            book_win.grab_set()
            frame1 = tkinter.Frame(book_win, bd=1, bg='black', height=20)
            label1 = tkinter.Label(frame1, text="enter book details:", anchor="w", font=("default", 13))
            label2 = tkinter.Label(frame1, text="writer's name:", anchor="w", font=("default", 13))
            ent1 = tkinter.Entry(frame1, font=("default", 16))
            label3 = tkinter.Label(frame1, text="price:", anchor="w", font=("default", 13))
            ent2 = tkinter.Entry(frame1, font=("default", 16))

            def submit():
                if ent1.get() != "" and ent2.get() != "":
                    if not is_number(ent2.get()):
                        raise MyException("price should be a number")
                    book.writer, book.price = ent1.get(), int(ent2.get())
                    bst.insert(book)
                    book_win.destroy()

            but1 = tkinter.Button(frame1, text="submit", command=submit)
            label1.pack(side="top", anchor="w", fill="x", expand=True)
            label2.pack(side="top", anchor="w", fill="x", expand=True)
            ent1.pack(side="top", anchor="w", fill="x", expand=True)
            label3.pack(side="top", anchor="w", fill="x", expand=True)
            ent2.pack(side="top", anchor="w", fill="x", expand=True)
            but1.pack(side="top", anchor="w", fill="x", expand=True)
            frame1.pack(pady=5, padx=5, fill='both', expand=True)
            book_win.mainloop()


def erase_text_1(event):
    if add_ent.get() == plh1:
        add_ent.delete(0, 'end')


def insert_text_1(event):
    if add_ent.get() == '':
        add_ent.insert(0, plh1)


def erase_text_2(event):
    if add_ent2.get() == plh2:
        add_ent2.delete(0, 'end')


def insert_text_2(event):
    if add_ent2.get() == '':
        add_ent2.insert(0, plh2)


def auto_complete(event):
    arr = ArrayList()
    arr2 = ArrayList()
    text = ""
    if event.char == '\x08':
        category_trie.complete(category_trie.head, (add_ent.get()[:-1]), arr)
        category_trie_reverse.complete(category_trie_reverse.head, reverse((add_ent.get()[:-1])), arr2)
    else:
        category_trie.complete(category_trie.head, (add_ent.get() + event.char), arr)
        category_trie_reverse.complete(category_trie_reverse.head, reverse((add_ent.get() + event.char)), arr2)
    arr3 = ArrayList()
    for i in arr:
        if i is not None:
            arr3.add(i)
    for i in arr2:
        if i is not None:
            arr3.add(reverse(i))
    arr3 = unique(arr3)
    for i in arr3:
        if i is not None:
            text += (i + "    \n")
    suggest_label.configure(state='normal')
    suggest_label.delete('1.0', tkinter.END)
    suggest_label.insert(tkinter.INSERT, text, "tag-right")
    suggest_label.configure(state='disabled')


add_ent.bind('<Key>', auto_complete)
add_ent.bind('<FocusIn>', erase_text_1)
add_ent.bind('<FocusOut>', insert_text_1)
add_ent2.bind('<FocusIn>', erase_text_2)
add_ent2.bind('<FocusOut>', insert_text_2)

add_ent.bind('<Return>', enter_pressed)
add_ent.pack(side="top", fill='x', expand=True, ipady=6)
add_ent2.bind('<Return>', enter_pressed)
add_ent2.pack(side="top", fill='x', expand=True, ipady=6)
ent_frame.pack(side="right", anchor="ne", fill='x', expand=True)
v = tkinter.StringVar(add, "1")
select = tkinter.Frame(add, bd=1, bg='black')


def clicked():
    pass


tkinter.Radiobutton(select, text="new category", variable=v, value="1", command=clicked, width=12).pack(side="top",
                                                                                                        ipady=5)
tkinter.Radiobutton(select, text="new book      ", variable=v, value="2", command=clicked, width=12).pack(side="top",
                                                                                                          ipady=5)
select.pack(side="left", anchor="nw")
# add end
# remove:
remove = tkinter.Frame(main_frame, bd=1, bg='black')

remove_label = tkinter.Label(remove, text="Removing an item : Press enter to delete")
remove_label.pack(side="top", fill='x', padx=0, pady=1)
remove_ent = tkinter.Entry(remove, width=10, font=("default", 14))
plh3 = "to delete:"
remove_ent.insert(0, plh3)
suggest_label2 = scrolledtext.ScrolledText(remove, height=7, font=("Times New Roman", 15))
suggest_label2.tag_configure('tag-center', justify='center')
suggest_label2.tag_configure('tag-left', justify='left')
suggest_label2.tag_configure('tag-right', justify='right')
suggest_label2.insert(tkinter.INSERT, "suggest    ", "tag-right")
suggest_label2.configure(state='disabled')
suggest_label2.pack(side="bottom", fill='x', pady=1)


def enter_pressed2(event):
    if remove_ent.get() != "" and remove_ent.get() != plh3:
        for i in remove_ent.get():
            if value_of(i) == -1:
                raise MyException("invalid name")
        if remove_ent.get() == "root":
            category_trie.clear()
            category_trie_reverse.clear()
            category_trie.insert("root")
            category_trie_reverse.insert(reverse("root"))
            tree.delete(remove_ent.get())
            book_trie.clear()
            book_trie_reverse.clear()
            bst.clear()
        else:
            sub_tree = tree.delete(remove_ent.get())
            if sub_tree is not None:
                def recursive_delete(node):
                    if node is None:
                        return
                    else:
                        if node.is_book:
                            book_trie.delete(node.data.name)
                            book_trie_reverse.delete(reverse(node.data.name))
                            bst.delete(node.data.name)
                        else:
                            category_trie.delete(node.data)
                            category_trie_reverse.delete(reverse(node.data))
                    for j in node.children:
                        recursive_delete(j)

                recursive_delete(sub_tree)


def erase_text_12(event):
    if remove_ent.get() == plh3:
        remove_ent.delete(0, 'end')


def insert_text_12(event):
    if remove_ent.get() == '':
        remove_ent.insert(0, plh3)


def auto_complete2(event):
    arr = ArrayList()
    arr2 = ArrayList()
    arr3 = ArrayList()
    arr4 = ArrayList()
    text = ""
    if event.char == '\x08':
        category_trie.complete(category_trie.head, (remove_ent.get()[:-1]), arr)
        category_trie_reverse.complete(category_trie_reverse.head, reverse((remove_ent.get()[:-1])), arr3)
        book_trie.complete(book_trie.head, (remove_ent.get()[:-1]), arr2)
        book_trie_reverse.complete(book_trie_reverse.head, reverse((remove_ent.get()[:-1])), arr4)
    else:
        category_trie.complete(category_trie.head, (remove_ent.get() + event.char), arr)
        category_trie_reverse.complete(category_trie_reverse.head, reverse((remove_ent.get() + event.char)), arr3)
        book_trie.complete(book_trie.head, (remove_ent.get() + event.char), arr2)
        book_trie_reverse.complete(book_trie_reverse.head, reverse((remove_ent.get() + event.char)), arr4)
    arr5 = ArrayList()
    arr6 = ArrayList()
    for i in arr:
        if i is not None:
            arr5.add(i)
    for i in arr2:
        if i is not None:
            arr6.add(i)
    for i in arr3:
        if i is not None:
            arr5.add(reverse(i))
    for i in arr4:
        if i is not None:
            arr6.add(reverse(i))
    arr5 = unique(arr5)
    arr6 = unique(arr6)
    for i in arr5:
        if i is not None:
            text += ("(category)  " + i + "    \n")
    for i in arr6:
        if i is not None:
            text += ("(book)  " + i + "    \n")
    suggest_label2.configure(state='normal')
    suggest_label2.delete('1.0', tkinter.END)
    suggest_label2.insert(tkinter.INSERT, text, "tag-right")
    suggest_label2.configure(state='disabled')


remove_ent.bind('<Key>', auto_complete2)
remove_ent.bind('<FocusIn>', erase_text_12)
remove_ent.bind('<FocusOut>', insert_text_12)

remove_ent.bind('<Return>', enter_pressed2)
remove_ent.pack(side="top", fill='x', expand=True, ipady=10)
# remove end
# by category:
category = tkinter.Frame(main_frame, bd=1, bg='black')

category_label = tkinter.Label(category, text="Searching by category : Press enter to search")
category_label.pack(side="top", fill='x', padx=0, pady=1)
category_ent = tkinter.Entry(category, width=10, font=("default", 14))
plh4 = "to search:"
category_ent.insert(0, plh4)
suggest_label3 = scrolledtext.ScrolledText(category, height=7, font=("Times New Roman", 15))
suggest_label3.tag_configure('tag-center', justify='center')
suggest_label3.tag_configure('tag-left', justify='left')
suggest_label3.tag_configure('tag-right', justify='right')
suggest_label3.insert(tkinter.INSERT, "suggest    ", "tag-right")
suggest_label3.configure(state='disabled')
suggest_label3.pack(side="bottom", fill='x', pady=1)


def enter_pressed3(event):
    if category_ent.get() != "" and category_ent.get() != plh4:
        for i in category_ent.get():
            if value_of(i) == -1:
                raise MyException("invalid name")
        arr = ArrayList()
        tree.get_books_by_category(category_ent.get(), arr)
        text = ""
        for i in arr:
            if i is not None:
                text += (str(i))
        if text == "":
            text = "No book was found"
        suggest_label3.configure(state='normal')
        suggest_label3.delete('1.0', tkinter.END)
        suggest_label3.insert(tkinter.INSERT, text, "tag-right")
        suggest_label3.configure(state='disabled')


def erase_text_13(event):
    if category_ent.get() == plh4:
        category_ent.delete(0, 'end')


def insert_text_13(event):
    if category_ent.get() == '':
        category_ent.insert(0, plh4)


def auto_complete3(event):
    arr = ArrayList()
    arr2 = ArrayList()
    text = ""
    if event.char == '\x08':
        category_trie.complete(category_trie.head, (category_ent.get()[:-1]), arr)
        category_trie_reverse.complete(category_trie_reverse.head, reverse((category_ent.get()[:-1])), arr2)
    else:
        category_trie.complete(category_trie.head, (category_ent.get() + event.char), arr)
        category_trie_reverse.complete(category_trie_reverse.head, reverse((category_ent.get() + event.char)), arr2)
    arr3 = ArrayList()
    for i in arr:
        if i is not None:
            arr3.add(i)
    for i in arr2:
        if i is not None:
            arr3.add(reverse(i))
    arr3 = unique(arr3)
    for i in arr3:
        if i is not None:
            text += (i + "    \n")
    suggest_label3.configure(state='normal')
    suggest_label3.delete('1.0', tkinter.END)
    suggest_label3.insert(tkinter.INSERT, text, "tag-right")
    suggest_label3.configure(state='disabled')


category_ent.bind('<Key>', auto_complete3)
category_ent.bind('<FocusIn>', erase_text_13)
category_ent.bind('<FocusOut>', insert_text_13)

category_ent.bind('<Return>', enter_pressed3)
category_ent.pack(side="top", fill='x', expand=True, ipady=10)
# by category end
# by book name
by_book = tkinter.Frame(main_frame, bd=1, bg='black')

by_book_label = tkinter.Label(by_book, text="Searching by book name : Press enter to search")
by_book_label.pack(side="top", fill='x', padx=0, pady=1)
by_book_ent = tkinter.Entry(by_book, width=10, font=("default", 14))
plh5 = "to search:"
by_book_ent.insert(0, plh5)
suggest_label4 = scrolledtext.ScrolledText(by_book, height=7, font=("Times New Roman", 15))
suggest_label4.tag_configure('tag-center', justify='center')
suggest_label4.tag_configure('tag-left', justify='left')
suggest_label4.tag_configure('tag-right', justify='right')
suggest_label4.insert(tkinter.INSERT, "suggest    ", "tag-right")
suggest_label4.configure(state='disabled')
suggest_label4.pack(side="bottom", fill='x', pady=1)


def enter_pressed4(event):
    if by_book_ent.get() != "" and by_book_ent.get() != plh5:
        for i in by_book_ent.get():
            if value_of(i) == -1:
                raise MyException("invalid name")
        book = tree.get_book(by_book_ent.get())
        text = ""
        if book is None:
            text = "No book was found"
        else:
            text = f"name : {book.name}\nwriter : {book.writer}\nprice : {book.price}$"
        suggest_label4.configure(state='normal')
        suggest_label4.delete('1.0', tkinter.END)
        suggest_label4.insert(tkinter.INSERT, text, "tag-left")
        suggest_label4.configure(state='disabled')


def erase_text_14(event):
    if by_book_ent.get() == plh5:
        by_book_ent.delete(0, 'end')


def insert_text_14(event):
    if by_book_ent.get() == '':
        by_book_ent.insert(0, plh5)


def auto_complete4(event):
    arr = ArrayList()
    arr2 = ArrayList()
    text = ""
    if event.char == '\x08':
        book_trie.complete(book_trie.head, (by_book_ent.get()[:-1]), arr)
        book_trie_reverse.complete(book_trie_reverse.head, reverse((by_book_ent.get()[:-1])), arr2)
    else:
        book_trie.complete(book_trie.head, (by_book_ent.get() + event.char), arr)
        book_trie_reverse.complete(book_trie_reverse.head, reverse((by_book_ent.get() + event.char)), arr2)
    arr3 = ArrayList()
    for i in arr:
        if i is not None:
            arr3.add(i)
    for i in arr2:
        if i is not None:
            arr3.add(reverse(i))
    arr3 = unique(arr3)
    for i in arr3:
        if i is not None:
            text += (i + "    \n")
    suggest_label4.configure(state='normal')
    suggest_label4.delete('1.0', tkinter.END)
    suggest_label4.insert(tkinter.INSERT, text, "tag-right")
    suggest_label4.configure(state='disabled')


by_book_ent.bind('<Key>', auto_complete4)
by_book_ent.bind('<FocusIn>', erase_text_14)
by_book_ent.bind('<FocusOut>', insert_text_14)

by_book_ent.bind('<Return>', enter_pressed4)
by_book_ent.pack(side="top", fill='x', expand=True, ipady=10)
# by book name end
# by budget
by_budget = tkinter.Frame(main_frame, bd=1, bg='black')

by_budget_label = tkinter.Label(by_budget, text="Searching by your budget : Press enter to search")
by_budget_label.pack(side="top", fill='x', padx=0, pady=1)
by_budget_ent = tkinter.Entry(by_budget, width=10, font=("default", 14))
plh6 = "budget:"
by_budget_ent.insert(0, plh6)
suggest_label5 = scrolledtext.ScrolledText(by_budget, height=7, font=("Times New Roman", 15))
suggest_label5.tag_configure('tag-center', justify='center')
suggest_label5.tag_configure('tag-left', justify='left')
suggest_label5.tag_configure('tag-right', justify='right')
suggest_label5.insert(tkinter.INSERT, "    ", "tag-right")
suggest_label5.configure(state='disabled')
suggest_label5.pack(side="bottom", fill='x', pady=1)


def enter_pressed5(event):
    if by_budget_ent.get() != "" and by_budget_ent.get() != plh6:
        if not is_number(by_budget_ent.get()):
            raise MyException("budget should be a number")
        arr = bst.get_lower_values(int(by_budget_ent.get()))
        text = ""
        for i in arr:
            if i is not None:
                text += (str(i))
        suggest_label5.configure(state='normal')
        suggest_label5.delete('1.0', tkinter.END)
        suggest_label5.insert(tkinter.INSERT, text, "tag-left")
        suggest_label5.configure(state='disabled')


def erase_text_15(event):
    if by_budget_ent.get() == plh6:
        by_budget_ent.delete(0, 'end')


def insert_text_15(event):
    if by_budget_ent.get() == '':
        by_budget_ent.insert(0, plh6)


def auto_complete5(event):
    pass


by_budget_ent.bind('<Key>', auto_complete5)
by_budget_ent.bind('<FocusIn>', erase_text_15)
by_budget_ent.bind('<FocusOut>', insert_text_15)

by_budget_ent.bind('<Return>', enter_pressed5)
by_budget_ent.pack(side="top", fill='x', expand=True, ipady=10)
# by budget end
main_frame.pack(pady=5, padx=5, fill='both', expand=True)

category_trie = Trie(all_finder=False)
book_trie = Trie(all_finder=False)
category_trie_reverse = Trie(all_finder=False)
book_trie_reverse = Trie(all_finder=False)
category_trie.insert("root")
category_trie_reverse.insert(reverse("root"))
tree = Tree()
bst = BinarySearchTree()
win.mainloop()
