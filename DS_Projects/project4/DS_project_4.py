import datetime
import os
import re
import traceback


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


class MapNode:
    def __init__(self, key: str, value=None):
        self.key = key
        self.value = value

    def __str__(self):
        return f"({self.key!r}: {self.value!r})"

    def __repr__(self):
        return f"({self.key!r}: {self.value!r})"

    def __eq__(self, other: object):
        return self.key == other

    def __ne__(self, other: object):
        return self.key != other


class HashMap:
    def __init__(self, i_cap=1, hash_func=None):
        self.hash_func = hash_func
        if hash_func is None:
            self.hash_func = self.murmur3_x86_32_hash

        self.i_cap = i_cap
        self.filled = 0
        self.list = [LinkedList() for i in range(len(self))]

    def __len__(self):
        return (2 ** self.i_cap) - 1

    def load_factor(self):
        return self.filled / len(self)

    def clear(self, i_cap=1):
        self.i_cap = i_cap
        self.filled = 0
        self.list = [LinkedList() for i in range(len(self))]

    def resize(self, i_cap):
        temp = HashMap(i_cap=i_cap, hash_func=self.hash_func)
        for i in self.list:
            for j in i:
                temp.put(j.key, j.value)
        self.i_cap = temp.i_cap
        self.filled = temp.filled
        self.list = temp.list

    def put(self, key: str, value):
        m = MapNode(key, value)
        ll = self.list[self.hash_func(key, len(self))]
        if m in ll:
            ll.find(m).data = m
        else:
            ll.insert_at_start(m)
            self.filled += 1
        if self.load_factor() > 0.5:
            self.resize(self.i_cap + 1)

    def remove(self, key: str):
        ll = self.list[self.hash_func(key, len(self))]
        if key in ll:
            ll.remove(key)
            self.filled -= 1
        if self.load_factor() < 0.2:
            self.resize(max(1, self.i_cap - 1))

    def get(self, key: str):
        ll = self.list[self.hash_func(key, len(self))]
        if key in ll:
            return ll.find(key).data

    def find(self, key: str):
        ll = self.list[self.hash_func(key, len(self))]
        if key in ll:
            return True
        return False

    def __getitem__(self, key: str):
        return self.get(key)

    def __setitem__(self, key: str, value):
        self.put(key, value)

    def __contains__(self, key: str):
        return self.find(key)

    def __iter__(self):
        for i in self.list:
            for j in i:
                yield j

    def __str__(self):
        return str(self.list)

    def __repr__(self):
        return repr(self.list)

    def hash_function(self, data: str, limit: int):
        ans = 0
        for i, d in enumerate(data):
            ans += int(ord(d)) * i ** 3
        return ans % limit

    def murmur3_x86_32_hash(self, data: str, limit: int, seed=0):
        c1 = 0xcc9e2d51
        c2 = 0x1b873593

        length = len(data)
        h1 = seed
        roundedEnd = (length & 0xfffffffc)  # round down to 4 byte block
        for i in range(0, roundedEnd, 4):
            # little endian load order
            k1 = (ord(data[i]) & 0xff) | ((ord(data[i + 1]) & 0xff) << 8) | \
                 ((ord(data[i + 2]) & 0xff) << 16) | (ord(data[i + 3]) << 24)
            k1 *= c1
            k1 = (k1 << 15) | ((k1 & 0xffffffff) >> 17)  # ROTL32(k1,15)
            k1 *= c2

            h1 ^= k1
            h1 = (h1 << 13) | ((h1 & 0xffffffff) >> 19)  # ROTL32(h1,13)
            h1 = h1 * 5 + 0xe6546b64

        # tail
        k1 = 0

        val = length & 0x03
        if val == 3:
            k1 = (ord(data[roundedEnd + 2]) & 0xff) << 16
        # fallthrough
        if val in [2, 3]:
            k1 |= (ord(data[roundedEnd + 1]) & 0xff) << 8
        # fallthrough
        if val in [1, 2, 3]:
            k1 |= ord(data[roundedEnd]) & 0xff
            k1 *= c1
            k1 = (k1 << 15) | ((k1 & 0xffffffff) >> 17)  # ROTL32(k1,15)
            k1 *= c2
            h1 ^= k1

        # finalization
        h1 ^= length
        # fmix(h1)
        h1 ^= ((h1 & 0xffffffff) >> 16)
        h1 *= 0x85ebca6b
        h1 ^= ((h1 & 0xffffffff) >> 13)
        h1 *= 0xc2b2ae35
        h1 ^= ((h1 & 0xffffffff) >> 16)

        return (h1 & 0xffffffff) % limit


class SmartLink:
    def __init__(self, name, owner=None):
        self.name = name
        self.owner = owner
        self.files = HashMap()
        self.allowed_users = HashMap()

    def __str__(self):
        return f"{type(self).__name__}(name={self.name!r}, owner={self.owner!r})"

    def __repr__(self):
        return f"{type(self).__name__}(name={self.name!r}, owner={self.owner!r})"

    def print(self):
        print(str(self) + " : ")
        print("    allowed users:")
        for ii in self.allowed_users:
            print("        ", ii.value)
        print("    files:")
        for ii in self.files:
            print("    ", ii.value)


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.directory = Directory()
        self.smart_links = HashMap()
        self.files = None
        self.premium = False
        self.favorites = HashMap()
        self.backup = HashMap()
        self.trash = HashMap()

    def __str__(self):
        return f"{type(self).__name__}(username={self.username!r})"

    def __repr__(self):
        return f"{type(self).__name__}(username={self.username!r})"


class MutableBool:
    _value = False

    @property
    def value(self):
        return type(self)._value

    @value.setter
    def value(self, val):
        type(self)._value = val

    def __str__(self):
        return str(self._value)

    def __repr__(self):
        return repr(self._value)


class DNode:
    def __init__(self, name):
        self.name = name
        self.type = "null"
        self.parent = None
        self.last_modify = None
        self.full_path = ""
        self.by_date = MutableBool()

    def update_path(self):
        pass

    def clone(self):
        pass

    def __lt__(self, other):
        if self.by_date.value:
            return self.last_modify < other
        return (self.name + self.type) < other

    def __le__(self, other):
        if self.by_date.value:
            return self.last_modify <= other
        return (self.name + self.type) <= other

    def __gt__(self, other):
        if self.by_date.value:
            return self.last_modify > other
        return (self.name + self.type) > other

    def __ge__(self, other):
        if self.by_date.value:
            return self.last_modify >= other
        return (self.name + self.type) >= other

    def __eq__(self, other):
        if self.by_date.value:
            return self.last_modify == other
        return (self.name + self.type) == other

    def __ne__(self, other):
        if self.by_date.value:
            return self.last_modify != other
        return (self.name + self.type) != other


class FileNode(DNode):
    def __init__(self, name, creator=None):
        super().__init__(name)
        self.data = ""
        self.type = "textfile"
        self.creator = creator

    def clone(self):
        ret = FileNode(name=self.name, creator=self.creator)
        ret.data = self.data
        ret.modified()
        return ret

    def update_path(self):
        self.full_path = self.parent.full_path + self.name + "\\"

    def modified(self):
        self.last_modify = datetime.datetime.now()

    def __str__(self):
        ret = f"""    name = {self.name!r}
    creator = {self.creator.username!r}
    last modified at {self.last_modify!s}
    data : {self.data!r} """
        return ret

    def __repr__(self):
        ret = f"""    name = {self.name!r}
    creator = {self.creator.username!r}
    last modified at {self.last_modify!s}
    data : {self.data!r} """
        return ret


class DirectoryNode(DNode):
    def __init__(self, name):
        super().__init__(name)
        self.last_modify = datetime.datetime.now()
        self.type = "directory"
        self.content = HashMap()
        self.trie = Trie()

    def clone(self):
        ret = DirectoryNode(self.name)
        for item_ in self.content:
            ret.content.put(item_.key, item_.value.clone())
            if item_.value.type == "textfile":
                ret.trie.insert(item_.value.name, ret.content[item_.key].value)
        for item_ in ret.content:
            item_.value.parent = ret
        # print(ret.content)
        return ret

    def finder(self, to_find, array0, array1):
        self.trie.complete(self.trie.head, to_find, array0, array1)
        for item_ in self.content:
            if item_.value.type == "directory":
                item_.value.finder(to_find, array0, array1)

    def update_path(self):
        self.full_path = self.parent.full_path + self.name + "\\"
        for item_ in self.content:
            item_.value.update_path()

    def __str__(self):
        name = "None"
        if self.parent is not None:
            name = self.parent.name
        return f"{type(self).__name__}(name={self.name!r}, type={self.type!r}, parent={name!r})"

    def __repr__(self):
        name = "None"
        if self.parent is not None:
            name = self.parent.name
        return f"{type(self).__name__}(name={self.name!r}, type={self.type!r}, parent={name!r})"


class Directory:
    def __init__(self):
        self.root = DirectoryNode("root")
        self.root.parent = self.root
        self.root.full_path = "root\\"

    def get_node_by_path(self, path: str):
        if "" == path:
            return self.root
        path_nodes = path.split("\\")
        cur = self.root
        for p in path_nodes:
            if p == "..":
                cur = cur.parent
            elif cur.type == "directory" and (p + "directory") in cur.content:
                cur = cur.content[p + "directory"].value
            else:
                return cur
        return cur

    def get_node_by_path_and_node(self, path: str, node: DirectoryNode = None):
        if node is None:
            node = self.root
        if "" == path:
            return node
        path_nodes = path.split("\\")
        cur = node
        for p in path_nodes:
            if p == "..":
                cur = cur.parent
            elif cur.type == "directory" and (p + "directory") in cur.content:
                cur = cur.content[p + "directory"].value
            else:
                return cur
        return cur


class ArrayList:
    def __init__(self):
        self.filled = 0
        self.size = 1
        self.list = [None for i in range(self.size)]
        self.changed = True

    def __repr__(self):
        return repr(self.list)

    def __str__(self):
        return str(self.list)

    def __contains__(self, item):
        ans = False
        for ii in self.list:
            if (ii is not None) and ii == item:
                ans = True
                break
        return ans
        # return self.find(item) >= 0

    def __iter__(self):
        return iter(self.list)

    def __len__(self):
        return len(self.list)

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

    def __setitem__(self, key, value):
        self.add(value, index=key)

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

    def unique(self):
        arr = ArrayList()
        for ii in self.list:
            if (ii is not None) and (ii not in arr):
                arr.add(ii)
        self.list = arr.list
        self.filled = arr.filled
        self.size = arr.size
        self.changed = True

    def remove(self, item):
        """
        mixes the order of items
        :param item:
        :return:
        """
        for ii in range(len(self.list)):
            if (self.list[ii] is not None) and self.list[ii] == item:
                s = self.filled - 1
                self.list[ii] = self.list[s]
                self.remove_last()
                break

    def remove_all(self, item):
        arr = ArrayList()
        for ii in self.list:
            if (ii is not None) and (ii != item):
                arr.add(ii)
        self.list = arr.list
        self.filled = arr.filled
        self.size = arr.size
        self.changed = True


class MD5:
    def __init__(self):
        pass

    def newArray(self, num):
        array = [0 for t in range(num)]
        return array

    def convertToWordArray(self, string):
        # print(string)
        lMessageLength = len(string)
        # print(lMessageLength)
        lNumberOfWords_temp1 = lMessageLength + 8
        # print(lNumberOfWords_temp1)
        lNumberOfWords_temp2 = (lNumberOfWords_temp1 - (lNumberOfWords_temp1 % 64)) / 64
        # print(lNumberOfWords_temp2)
        lNumberOfWords = int((lNumberOfWords_temp2 + 1) * 16)
        # print(lNumberOfWords)
        lWordArray = self.newArray(lNumberOfWords - 1)
        lBytePosition = 0
        lByteCount = 0
        while lByteCount < lMessageLength:
            lWordCount = int((lByteCount - (lByteCount % 4)) / 4)
            lBytePosition = (lByteCount % 4) * 8
            # print(string[int(lByteCount)])
            lWordArray[lWordCount] = (lWordArray[lWordCount] | (ord(string[int(lByteCount)]) << lBytePosition))
            lByteCount += 1
        lWordCount = int((lByteCount - (lByteCount % 4)) / 4)
        lBytePosition = (lByteCount % 4) * 8
        lWordArray[lWordCount] = lWordArray[lWordCount] | (0x80 << lBytePosition)
        lWordArray[lNumberOfWords - 2] = lMessageLength << 3
        lWordArray.append(lMessageLength >> 29)
        return lWordArray

    def F(self, x, y, z):
        # print(x, y, x)
        return (x & y) | ((~x) & z)

    def G(self, x, y, z):
        return (x & z) | (y & (~z))

    def H(self, x, y, z):
        return x ^ y ^ z

    def I(self, x, y, z):
        return y ^ (x | (~z))

    def XX(self, func, a, b, c, d, x, s, ac):
        res = 0
        res = res + a + func(b, c, d)
        res += x
        res += ac
        res = res & 0xffffffff
        res = self.rol(res, s)
        res = res & 0xffffffff
        res += b
        return res & 0xffffffff

    def addu(self, x, y):
        return (x + y) & 0xffffffff

    def rol(self, v, s):
        return (v << s) | (v >> (32 - s))

    def wordToHex(self, lValue):
        wordToHexValue = ''
        wordToHexValue_temp = ''
        for lCount in range(4):
            lByte = (lValue >> (lCount * 8)) & 255
            wordToHexValue_temp = "0" + format(lByte, 'x')
            wordToHexValue = wordToHexValue + wordToHexValue_temp[-2:]
        return wordToHexValue

    def md5hash(self, message):
        x = self.convertToWordArray(message)
        a = 0x67452301
        b = 0xEFCDAB89
        c = 0x98BADCFE
        d = 0x10325476
        xl = len(x)
        j = 0
        while j < xl:
            aa = a
            bb = b
            cc = c
            dd = d
            a = self.XX(self.F, a, b, c, d, x[j + 0], 7, 0xD76AA478)
            d = self.XX(self.F, d, a, b, c, x[j + 1], 12, 0xE8C7B756)
            c = self.XX(self.F, c, d, a, b, x[j + 2], 17, 0x242070DB)
            b = self.XX(self.F, b, c, d, a, x[j + 3], 22, 0xC1BDCEEE)
            a = self.XX(self.F, a, b, c, d, x[j + 4], 7, 0xF57C0FAF)
            d = self.XX(self.F, d, a, b, c, x[j + 5], 12, 0x4787C62A)
            c = self.XX(self.F, c, d, a, b, x[j + 6], 17, 0xA8304613)
            b = self.XX(self.F, b, c, d, a, x[j + 7], 22, 0xFD469501)
            a = self.XX(self.F, a, b, c, d, x[j + 8], 7, 0x698098D8)
            d = self.XX(self.F, d, a, b, c, x[j + 9], 12, 0x8B44F7AF)
            c = self.XX(self.F, c, d, a, b, x[j + 10], 17, 0xFFFF5BB1)
            b = self.XX(self.F, b, c, d, a, x[j + 11], 22, 0x895CD7BE)
            a = self.XX(self.F, a, b, c, d, x[j + 12], 7, 0x6B901122)
            d = self.XX(self.F, d, a, b, c, x[j + 13], 12, 0xFD987193)
            c = self.XX(self.F, c, d, a, b, x[j + 14], 17, 0xA679438E)
            b = self.XX(self.F, b, c, d, a, x[j + 15], 22, 0x49B40821)
            a = self.XX(self.G, a, b, c, d, x[j + 1], 5, 0xF61E2562)
            d = self.XX(self.G, d, a, b, c, x[j + 6], 9, 0xC040B340)
            c = self.XX(self.G, c, d, a, b, x[j + 11], 14, 0x265E5A51)
            b = self.XX(self.G, b, c, d, a, x[j + 0], 20, 0xE9B6C7AA)
            a = self.XX(self.G, a, b, c, d, x[j + 5], 5, 0xD62F105D)
            d = self.XX(self.G, d, a, b, c, x[j + 10], 9, 0x2441453)
            c = self.XX(self.G, c, d, a, b, x[j + 15], 14, 0xD8A1E681)
            b = self.XX(self.G, b, c, d, a, x[j + 4], 20, 0xE7D3FBC8)
            a = self.XX(self.G, a, b, c, d, x[j + 9], 5, 0x21E1CDE6)
            d = self.XX(self.G, d, a, b, c, x[j + 14], 9, 0xC33707D6)
            c = self.XX(self.G, c, d, a, b, x[j + 3], 14, 0xF4D50D87)
            b = self.XX(self.G, b, c, d, a, x[j + 8], 20, 0x455A14ED)
            a = self.XX(self.G, a, b, c, d, x[j + 13], 5, 0xA9E3E905)
            d = self.XX(self.G, d, a, b, c, x[j + 2], 9, 0xFCEFA3F8)
            c = self.XX(self.G, c, d, a, b, x[j + 7], 14, 0x676F02D9)
            b = self.XX(self.G, b, c, d, a, x[j + 12], 20, 0x8D2A4C8A)
            a = self.XX(self.H, a, b, c, d, x[j + 5], 4, 0xFFFA3942)
            d = self.XX(self.H, d, a, b, c, x[j + 8], 11, 0x8771F681)
            c = self.XX(self.H, c, d, a, b, x[j + 11], 16, 0x6D9D6122)
            b = self.XX(self.H, b, c, d, a, x[j + 14], 23, 0xFDE5380C)
            a = self.XX(self.H, a, b, c, d, x[j + 1], 4, 0xA4BEEA44)
            d = self.XX(self.H, d, a, b, c, x[j + 4], 11, 0x4BDECFA9)
            c = self.XX(self.H, c, d, a, b, x[j + 7], 16, 0xF6BB4B60)
            b = self.XX(self.H, b, c, d, a, x[j + 10], 23, 0xBEBFBC70)
            a = self.XX(self.H, a, b, c, d, x[j + 13], 4, 0x289B7EC6)
            d = self.XX(self.H, d, a, b, c, x[j + 0], 11, 0xEAA127FA)
            c = self.XX(self.H, c, d, a, b, x[j + 3], 16, 0xD4EF3085)
            b = self.XX(self.H, b, c, d, a, x[j + 6], 23, 0x4881D05)
            a = self.XX(self.H, a, b, c, d, x[j + 9], 4, 0xD9D4D039)
            d = self.XX(self.H, d, a, b, c, x[j + 12], 11, 0xE6DB99E5)
            c = self.XX(self.H, c, d, a, b, x[j + 15], 16, 0x1FA27CF8)
            b = self.XX(self.H, b, c, d, a, x[j + 2], 23, 0xC4AC5665)
            a = self.XX(self.I, a, b, c, d, x[j + 0], 6, 0xF4292244)
            d = self.XX(self.I, d, a, b, c, x[j + 7], 10, 0x432AFF97)
            c = self.XX(self.I, c, d, a, b, x[j + 14], 15, 0xAB9423A7)
            b = self.XX(self.I, b, c, d, a, x[j + 5], 21, 0xFC93A039)
            a = self.XX(self.I, a, b, c, d, x[j + 12], 6, 0x655B59C3)
            d = self.XX(self.I, d, a, b, c, x[j + 3], 10, 0x8F0CCC92)
            c = self.XX(self.I, c, d, a, b, x[j + 10], 15, 0xFFEFF47D)
            b = self.XX(self.I, b, c, d, a, x[j + 1], 21, 0x85845DD1)
            a = self.XX(self.I, a, b, c, d, x[j + 8], 6, 0x6FA87E4F)
            d = self.XX(self.I, d, a, b, c, x[j + 15], 10, 0xFE2CE6E0)
            c = self.XX(self.I, c, d, a, b, x[j + 6], 15, 0xA3014314)
            b = self.XX(self.I, b, c, d, a, x[j + 13], 21, 0x4E0811A1)
            a = self.XX(self.I, a, b, c, d, x[j + 4], 6, 0xF7537E82)
            d = self.XX(self.I, d, a, b, c, x[j + 11], 10, 0xBD3AF235)
            c = self.XX(self.I, c, d, a, b, x[j + 2], 15, 0x2AD7D2BB)
            b = self.XX(self.I, b, c, d, a, x[j + 9], 21, 0xEB86D391)
            a = self.addu(a, aa)
            b = self.addu(b, bb)
            c = self.addu(c, cc)
            d = self.addu(d, dd)
            j += 16
        return (self.wordToHex(a) + self.wordToHex(b) + self.wordToHex(c) + self.wordToHex(d)).lower()


class TrieNode:
    def __init__(self, data="", is_word=False, pointer=None):
        self.data = data
        self.children = [None for iii in range(256)]
        self.is_word = is_word
        self.pointer = pointer


def value_of(val):
    for iii in range(256):
        if val == chr(iii):
            return iii
    return -1


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

    def complete(self, node, value, array, darray):
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
                darray.add(head2.pointer)
            for i in head2.children:
                if i is not None and (has_child if not self.all_finder else True):
                    self.complete(i, value, array, darray)

    def insert(self, value, pointer):
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
                head2.pointer = pointer
            if len(value) > 0:
                for i in value:
                    head2.children[value_of(i)] = TrieNode(to_insert + i, False)
                    to_insert += i
                    head2 = head2.children[value_of(i)]
                head2.is_word = True
                head2.pointer = pointer

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
                head2.pointer = None

    def clear(self):
        self.head = TrieNode()


sort_by = MutableBool()
md5 = MD5()
all_users = HashMap()
all_users["admin"] = User("admin", md5.md5hash("admin"))
all_links = HashMap()
valid_commands = [
    re.compile(r"^\s*exit\s*$", re.IGNORECASE),  # 0
    re.compile(r"^\s*sign up (\w+) (\w+)\s*$", re.IGNORECASE),  # 1
    re.compile(r"^\s*sign in (\w+) (\w+)\s*$", re.IGNORECASE),  # 2
    re.compile(r"^\s*sign out\s*$", re.IGNORECASE),  # 3
    re.compile(r"^\s*cd root\\([\w\\\.]*)\s*$", re.IGNORECASE),  # 4
    re.compile(r"^\s*mkdir (\w+)\s*$", re.IGNORECASE),  # 5
    re.compile(r"^\s*cd \\([\w\\\.]*)\s*$", re.IGNORECASE),  # 6
    re.compile(r"^\s*dir (Date|Name)\s*$", re.IGNORECASE),  # 7
    re.compile(r"^\s*type nul (\w+)\s*$", re.IGNORECASE),  # 8
    re.compile(r"^\s*del (\w+) (file|dir)\s*$", re.IGNORECASE),  # 9
    re.compile(r"^\s*open (\w+)\s*$", re.IGNORECASE),  # 10
    re.compile(r"^\s*clink (\w+) ([\w,]+)\s*$", re.IGNORECASE),  # 11
    re.compile(r"^\s*links\s*$", re.IGNORECASE),  # 12
    re.compile(r"^\s*flink (\w+) (\w+)\s*$", re.IGNORECASE),  # 13
    re.compile(r"^\s*dlink (\w+)\s*$", re.IGNORECASE),  # 14
    re.compile(r"^\s*link (\w+)\s*$", re.IGNORECASE),  # 15
    re.compile(r"^\s*buy Premium\s*$", re.IGNORECASE),  # 16
    re.compile(r"^\s*bash (\w+\.txt)\s*$", re.IGNORECASE),  # 17 bash
    re.compile(r"^\s*cut (\w+) (dir|file)\s*$", re.IGNORECASE),  # 18
    re.compile(r"\s*paste\s*$", re.IGNORECASE),  # 19
    re.compile(r"^\s*copy (\w+) (dir|file)\s*$", re.IGNORECASE),  # 20
    re.compile(r"\s*trash\s*$", re.IGNORECASE),  # 21
    re.compile(r"\s*restore (\w+) (dir|file)\s*$", re.IGNORECASE),  # 22
    re.compile(r"\s*backup (\w+)\s*$", re.IGNORECASE),  # 23
    re.compile(r"\s*backups\s*$", re.IGNORECASE),  # 24
    re.compile(r"\s*faves\s*$", re.IGNORECASE),  # 25
    re.compile(r"\s*addfav (\w+)\s*$", re.IGNORECASE),  # 26
    re.compile(r"\s*delfav (\w+)\s*$", re.IGNORECASE),  # 27
    re.compile(r"\s*search (\w+)\s*$", re.IGNORECASE),  # 28
    re.compile(r"\s*find (\w+)\s*$", re.IGNORECASE),  # 29
    re.compile(r"\s*help\s*$", re.IGNORECASE),  # 30
    re.compile(r"\s*cls\s*$", re.IGNORECASE),  # 31
]
current_user: User = None
current_path: DirectoryNode = None
to_paste: DNode = None
exited = False
count = 0
while not exited:
    try:
        full_name = (current_user.username if current_user is not None else "null")
        full_path = (current_path.full_path if current_path is not None else "null")
        if count == 0:
            command = input(fr"{full_name}:\{full_path}> ")
        else:
            command = lines[len(lines) - count]
            print(fr"{full_name}:\{full_path}> " + command)
            count -= 1
        # exit:
        match = re.match(valid_commands[0], command)
        if match:
            exited = True
        # cls:
        match = re.match(valid_commands[31], command)
        if match:
            os.system("cls")
        # help
        match = re.match(valid_commands[30], command)
        if match:
            help_ = r"""    valid commands:
        [00] exit -> to exit
        [01] help -> to show help
        [02] sign up 'username' 'password' -> to sign up
        [03] sign in 'username' 'password' -> to sign in
        [04] sign out -> to sign out
        [05] cd root\'...' -> to go to the given address from root
        [06] cd \'...' -> to go to the given address from current path
        [07] mkdir 'directory_name' -> to make a directory
        [08] dir name|date -> to show content of current directory sorted by date|name
        [09] type nul 'file_name' -> to create a file
        [10] del 'name' dir|file -> to delete a file|directory
        [11] open 'file_name' -> to open|edit a file
        [12] clink 'link_name' 'user0,user2,...' -> to create a smart_link and set allowed users
        [13] links -> to show all your smart_links
        [14] flink 'file_name' 'link_name' -> to add a file to a smart_link
        [15] dlink 'link_name' -> to delete a smart_link
        [16] link 'link_name' -> to enter a link
        [17] buy Premium -> to buy Premium
        [18] bash 'file_name.txt' -> to run commands from a bash file
        [19] cut 'name' dir|file -> to cut a directory|file
        [20] paste -> to paste 
        [21] copy 'name' dir|file -> to copy a file|directory
        [22] trash -> to see trash can
        [23] restore 'name' dir|file -> to restrore a file|directory from trash can
        [24] backup 'file_name' -> to back up a file
        [25] backups -> to show all backed up files
        [26] faves -> to show favorites
        [27] addfav 'file_name' -> to add a file to favorites
        [28] delfav 'file_name' -> to remove a file from favorites
        [29] search 'partial_file_name' -> to search for a file in current directory (faster)
        [30] find 'partial_file_name' to search for a file in current directory and its sub directories (slower)
        [31] cls -> to clear console"""
            print(help_)
        # sign up:
        match = re.match(valid_commands[1], command)
        if match:
            if current_user is None:
                new_user = User(match.groups()[0], md5.md5hash(match.groups()[1]))
                if all_users.find(new_user.username):
                    print("duplicate username")
                else:
                    all_users[new_user.username] = new_user
                    print("signed up successfully")
        # sign in:
        match = re.match(valid_commands[2], command)
        if match:
            if current_user is None:
                if all_users.find(match.groups()[0]) and all_users[match.groups()[0]].value.password == md5.md5hash(
                        match.groups()[1]):
                    current_user = all_users[match.groups()[0]].value
                    current_path = current_user.directory.root
                    # print(all_users[match.groups()[0]])
                    print("signed in successfully")
                else:
                    print("invalid username or password")
        # sign out:
        match = re.match(valid_commands[3], command)
        if match:
            current_user = None
            current_path = None
            print("signed out successfully")
        # cd root\...:
        match = re.match(valid_commands[4], command)
        if match:
            if current_path is not None:
                current_path = current_user.directory.get_node_by_path(match.groups()[0])
                # print(current_path)
        # mkdir:
        match = re.match(valid_commands[5], command)
        if match:
            if current_path is not None:
                new_dir = DirectoryNode(match.groups()[0])
                if current_path.content.find(new_dir.name + new_dir.type):
                    print("duplicate directory name")
                else:
                    current_path.content[new_dir.name + new_dir.type] = new_dir
                    new_dir.parent = current_path
                    new_dir.full_path = new_dir.parent.full_path + new_dir.name + "\\"
                    print("directory created")
                # print(new_dir)
        # cd \...:
        match = re.match(valid_commands[6], command)
        if match:
            if current_path is not None:
                current_path = current_user.directory.get_node_by_path_and_node(match.groups()[0], current_path)
                # print(current_path)
        # dir name|date:
        match = re.match(valid_commands[7], command)
        if match:
            if current_path is not None:
                list_to_show = ArrayList()
                for mp in current_path.content:
                    list_to_show.add(mp.value)
                if match.groups()[0].lower() == "name":
                    sort_by.value = False
                elif match.groups()[0].lower() == "date":
                    sort_by.value = True
                list_to_show.sort()
                for lts in list_to_show:
                    if lts is not None:
                        print(f"{lts.name} : {lts.type}", lts.last_modify)
        # type null ...:
        match = re.match(valid_commands[8], command)
        if match:
            if current_path is not None:
                new_file = FileNode(match.groups()[0])
                if current_path.content.find(new_file.name + new_file.type):
                    print("duplicate file name")
                else:
                    current_path.content[new_file.name + new_file.type] = new_file
                    new_file.parent = current_path
                    new_file.full_path = new_file.parent.full_path + new_file.name + "\\"
                    new_file.creator = current_user
                    new_file.modified()
                    if current_user.premium:
                        current_path.trie.insert(new_file.name, new_file)
                    print("file created")
        # del ...:
        match = re.match(valid_commands[9], command)
        if match:
            if current_path is not None:
                del_type = ""
                if match.groups()[1].lower() == "file":
                    del_type = "textfile"
                elif match.groups()[1].lower() == "dir":
                    del_type = "directory"
                if current_user.premium:
                    current_user.trash[match.groups()[0] + del_type] = current_path.content[
                        match.groups()[0] + del_type].value
                    if del_type == "textfile":
                        current_path.trie.delete(match.groups()[0])
                current_path.content.remove(match.groups()[0] + del_type)
                print("deleted successfully")
        # open ...:
        match = re.match(valid_commands[10], command)
        if match:
            if current_path is not None:
                file_data = current_path.content[match.groups()[0] + "textfile"].value
                print(file_data)
                edit = input("edit[y/n]: ")
                if edit.lower() == "y":
                    file_data.data = input("enter new data:\n")
                    file_data.modified()
                else:
                    pass
        # clink name users:
        match = re.match(valid_commands[11], command)
        if match:
            if current_user is not None:
                name_ = match.groups()[0]
                users = match.groups()[1].split(",")
                if name_ in all_links:
                    print("duplicate link name")
                else:
                    sl = SmartLink(name_, owner=current_user)
                    for un in users:
                        if all_users[un] is not None:
                            sl.allowed_users[un] = all_users[un].value
                    current_user.smart_links[name_] = sl
                    all_links[name_] = sl
                    print("link created")

        # links :
        match = re.match(valid_commands[12], command)
        if match:
            if current_user is not None:
                for ii in current_user.smart_links:
                    ii.value.print()
        # flink file_name link_name :
        match = re.match(valid_commands[13], command)
        if match:
            if current_user is not None:
                file_name = match.groups()[0]
                link_name = match.groups()[1]
                if (current_path.content[file_name + "textfile"] is not None) and (
                        current_user.smart_links[link_name] is not None):
                    current_user.smart_links[link_name].value.files[file_name + "textfile"] = current_path.content[
                        file_name + "textfile"].value
                    print("file added to the link")
        # dlink link_name :
        match = re.match(valid_commands[14], command)
        if match:
            if current_user is not None:
                link_name = match.groups()[0]
                if current_user.smart_links[link_name] is not None:
                    current_user.smart_links.remove(link_name)
                    all_links.remove(link_name)
                    print("link deleted")
        # link link_name :
        match = re.match(valid_commands[15], command)
        if match:
            if current_user is not None:
                name_ = match.groups()[0]
                if all_links[name_] is not None:
                    if current_user.username in all_links[name_].value.allowed_users:
                        all_links[name_].value.print()
                    else:
                        print("access denied")
                else:
                    print("invalid link")
        # buy premium :
        match = re.match(valid_commands[16], command)
        if match:
            if current_user is not None:
                current_user.premium = True
                print("now you are a premium user")
        #  bash bash_name.txt:
        match = re.match(valid_commands[17], command)
        if match:
            file_name = match.groups()[0]
            with open(file_name, "r") as bash_file:
                lines = bash_file.readlines()
                for kk in range(len(lines)):
                    if lines[kk][-1] == '\n':
                        lines[kk] = lines[kk][:-1]
                count = len(lines)
                print("bash loaded")
        # cut name dir|file
        match = re.match(valid_commands[18], command)
        if match:
            if (current_user is not None) and current_user.premium:
                the_type = ""
                name_ = match.groups()[0]
                if match.groups()[1].lower() == "file":
                    the_type = "textfile"
                elif match.groups()[1].lower() == "dir":
                    the_type = "directory"
                if current_path.content[name_ + the_type] is not None:
                    to_paste = current_path.content[name_ + the_type].value
                    current_path.content.remove(name_ + the_type)
                    if the_type == "textfile":
                        current_path.trie.delete(name_)
                    print("cut was successful")
                else:
                    print("nothing is there to cut!")
            elif (current_user is not None) and not current_user.premium:
                print("please buy premium")
        # paste
        match = re.match(valid_commands[19], command)
        if match:
            if (current_user is not None) and current_user.premium:
                if to_paste is not None:
                    the_type = to_paste.type
                    name_ = to_paste.name
                    if current_path.content.find(name_ + the_type):
                        print("duplicate name")
                    else:
                        current_path.content[name_ + the_type] = to_paste
                        to_paste.parent = current_path
                        to_paste.update_path()
                        if to_paste.type == "textfile":
                            current_path.trie.insert(to_paste.name, to_paste)
                        to_paste = None
                        print("pasted successfully")
                else:
                    print("nothing to paste!")
            elif (current_user is not None) and not current_user.premium:
                print("please buy premium")
        # copy name dir|file
        match = re.match(valid_commands[20], command)
        if match:
            if (current_user is not None) and current_user.premium:
                the_type = ""
                name_ = match.groups()[0]
                if match.groups()[1].lower() == "file":
                    the_type = "textfile"
                elif match.groups()[1].lower() == "dir":
                    the_type = "directory"
                if current_path.content[name_ + the_type] is not None:
                    to_paste = current_path.content[name_ + the_type].value.clone()
                    print("copy was successful")
                else:
                    print("nothing is there to copy!")
            elif (current_user is not None) and not current_user.premium:
                print("please buy premium")
        # trash
        match = re.match(valid_commands[21], command)
        if match:
            if (current_user is not None) and current_user.premium:
                for item in current_user.trash:
                    print("=============================")
                    print(item.value)
                    print("=============================")
            elif (current_user is not None) and not current_user.premium:
                print("please buy premium")
        # restore name (dir/file)
        match = re.match(valid_commands[22], command)
        if match:
            if (current_user is not None) and current_user.premium:
                the_type = ""
                name_ = match.groups()[0]
                if match.groups()[1].lower() == "file":
                    the_type = "textfile"
                elif match.groups()[1].lower() == "dir":
                    the_type = "directory"
                if (name_ + the_type) in current_user.trash:
                    current_user.trash[name_ + the_type].value.parent.content[name_ + the_type] = current_user.trash[
                        name_ + the_type].value
                    if the_type == "textfile":
                        current_user.trash[name_ + the_type].value.parent.trie.insert(name_, current_user.trash[
                            name_ + the_type].value)
                    current_user.trash.remove(name_ + the_type)
                    print("restored successfully")
            elif (current_user is not None) and not current_user.premium:
                print("please buy premium")
        # backup filename
        match = re.match(valid_commands[23], command)
        if match:
            if (current_user is not None) and current_user.premium:
                name_ = match.groups()[0]
                the_type = "textfile"
                if (name_ + the_type) in current_path.content:
                    current_user.backup[name_ + the_type] = current_path.content[name_ + the_type].value.clone()
                    print("backed up successfully")
            elif (current_user is not None) and not current_user.premium:
                print("please buy premium")
        # backups
        match = re.match(valid_commands[24], command)
        if match:
            if (current_user is not None) and current_user.premium:
                for item in current_user.backup:
                    print("=============================")
                    print(item.value)
                    print("=============================")
            elif (current_user is not None) and not current_user.premium:
                print("please buy premium")
        # faves
        match = re.match(valid_commands[25], command)
        if match:
            if (current_user is not None) and current_user.premium:
                for item in current_user.favorites:
                    print("=============================")
                    print(item.value)
                    print("=============================")
            elif (current_user is not None) and not current_user.premium:
                print("please buy premium")
        # addfav name
        match = re.match(valid_commands[26], command)
        if match:
            if (current_user is not None) and current_user.premium:
                name_ = match.groups()[0]
                the_type = "textfile"
                if (name_ + the_type) in current_path.content:
                    current_user.favorites[name_ + the_type] = current_path.content[name_ + the_type].value
                    print("added successfully")

            elif (current_user is not None) and not current_user.premium:
                print("please buy premium")
        # delfav name
        match = re.match(valid_commands[27], command)
        if match:
            if (current_user is not None) and current_user.premium:
                name_ = match.groups()[0]
                the_type = "textfile"
                if (name_ + the_type) in current_user.favorites:
                    current_user.favorites.remove(name_ + the_type)
                    print("removed successfully")

            elif (current_user is not None) and not current_user.premium:
                print("please buy premium")
        # search name
        match = re.match(valid_commands[28], command)
        if match:
            if (current_user is not None) and current_user.premium:
                name_ = match.groups()[0]
                the_type = "textfile"
                arr0 = ArrayList()
                arr1 = ArrayList()
                current_path.trie.complete(current_path.trie.head, name_, arr0, arr1)
                # print(arr0)
                # print(arr1)
                for l in arr1:
                    if l is not None:
                        print(l.name, " at ", l.full_path)
            elif (current_user is not None) and not current_user.premium:
                print("please buy premium")
        # find name
        match = re.match(valid_commands[29], command)
        if match:
            if (current_user is not None) and current_user.premium:
                name_ = match.groups()[0]
                the_type = "textfile"
                arr0 = ArrayList()
                arr1 = ArrayList()
                current_path.finder(name_, arr0, arr1)
                for l in arr1:
                    if l is not None:
                        print(l.name, " at ", l.full_path)
            elif (current_user is not None) and not current_user.premium:
                print("please buy premium")
    except Exception as ex:
        print("an unknown error has occurred")
        print("more info : ", ex)
        print(traceback.format_exc())
