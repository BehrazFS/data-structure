import math

from Graph import Graph, Vertex, Edge
from ArrayList import ArrayList
from HashMap import HashMap


class User:
    def __init__(self, username, password, code, bio="", city=None):
        self.hash_follow = ArrayList()
        self.code = code
        self.popularity = 0
        self.username = username
        self.password = password
        self.bio = bio
        self.city = city
        self.posts = ArrayList()
        self.notifications = ArrayList()
        self.feed = ArrayList()
        self.activity = ArrayList()

    def __str__(self):
        return f"{type(self).__name__}(username = {self.username!r})"

    def __repr__(self):
        return f"{type(self).__name__}(username = {self.username!r})"

    def __eq__(self, other):
        return self.username == other

    def __ne__(self, other):
        return self.username != other

    def get_followers(self, g: Graph):
        arr = ArrayList()
        for ii, i in enumerate(g.adjacency_list):
            # print(ii)
            for j in i:
                if j[0].data.username == self.username:
                    arr.add(g[ii].data)
            # print(arr)

        return arr

    def get_following(self, g: Graph):
        arr = ArrayList()
        for i in g.adjacency_list[self.code]:
            arr.add(i[0].data)
        return arr

    def get_vfollowers(self, g: Graph):
        arr = ArrayList()
        for ii, i in enumerate(g.adjacency_list):
            # print(ii)
            for j in i:
                if j[0].data.username == self.username:
                    arr.add(g[ii])
            # print(arr)

        return arr

    def get_vfollowing(self, g: Graph):
        arr = ArrayList()
        for i in g.adjacency_list[self.code]:
            arr.add(i[0])
        return arr


class Post:
    def __init__(self, writer: User, title="", text=""):
        self.title = title
        self.text = text
        self.writer = writer
        self.likes = 0
        self.likers = ArrayList()

    def __str__(self):
        ans = f"""       title: {self.title!r}
        text: {self.text!r}
        writer: {self.writer!r}
        likes: {self.likes!r}
        liked by : {self.likers!r}    
        """

        return ans

    def __repr__(self):
        ans = f"""       title: {self.title!r}
                text: {self.text!r}
                writer: {self.writer!r}
                likes: {self.likes!r}
                liked by : {self.likers!r}    
                """

        return ans

    def __eq__(self, other):
        return self.title == other

    def __ne__(self, other):
        return self.title != other

    def __le__(self, other):
        return self.title <= other

    def __ge__(self, other):
        return self.title >= other

    def __lt__(self, other):
        return self.title < other

    def __gt__(self, other):
        return self.title > other


class HashGraph(Graph):
    def __init__(self):
        self.hashes = ArrayList()
        self.posts = ArrayList()
        super().__init__()

    def add_vertex(self, data=None, kind="post"):
        if kind == "post":
            new_ver = Vertex(self.vertices.filled, data)
            self.vertices.add(new_ver)
            self.adjacency_list.add(ArrayList())
            self.adjacency_matrix.add_row(math.inf)
            self.adjacency_matrix.add_column(math.inf)
            self.posts.add(new_ver)
        elif kind == "hash":
            new_ver = Vertex(self.vertices.filled, data)
            self.vertices.add(new_ver)
            self.adjacency_list.add(ArrayList())
            self.adjacency_matrix.add_row(math.inf)
            self.adjacency_matrix.add_column(math.inf)
            self.hashes.add(new_ver)

    def get_hash(self, hash: str):
        for i in self.hashes:
            if i.data == hash:
                return i

    def get_post(self, post: Post):
        for i in self.posts:
            if i.data == post:
                return i

    def get_hashes_by_post(self, post: Post):
        arr = ArrayList()
        for i in self.adjacency_list[self.get_post(post).index]:
            arr.add(i[0].data)
        return arr

    def get_posts_by_hash(self, hash: str):
        arr = ArrayList()
        for i in self.adjacency_list[self.get_hash(hash).index]:
            arr.add(i[0].data)
        return arr


class SuggestGraph(Graph):
    def __init__(self, g: Graph):
        super().__init__()
        for i in g.vertices:
            self.add_vertex(i.data)
        for i in self.vertices:
            for j in self.vertices:
                self.add_edge(i, j, 0)
        for i in g.vertices:
            for j in g.adjacency_list[i.index]:
                for k in g.adjacency_list[j[0].index]:
                    self.update_edge_weight(i, k[0],
                                            new_weight=self.get_edge_weight(i, k[0]) + 1)

    def add_user(self, user: User):
        self.add_vertex(user)
        v = self.get(user)
        for i in self.vertices:
            if v != i:
                self.add_edge_two_way(v, i, 0)
            else:
                self.add_edge(v, i, 0)

    def unfollow(self, source: Vertex, destination: Vertex, source_followers, destination_followings):
        for i in source_followers:
            if self.get_edge_weight(i, destination) != 0:
                self.update_edge_weight(i, destination,
                                        new_weight=self.get_edge_weight(i, destination) - 1)

        for i in destination_followings:
            if self.get_edge_weight(source, i) != 0:
                self.update_edge_weight(source, i,
                                        new_weight=self.get_edge_weight(source, i) - 1)

    def follow(self, source: Vertex, destination: Vertex, source_followers: ArrayList,
               destination_followings: ArrayList):
        for i in source_followers:
            self.update_edge_weight(i, destination,
                                    new_weight=self.get_edge_weight(i, destination) + 1)

        for i in destination_followings:
            self.update_edge_weight(source, i,
                                    new_weight=self.get_edge_weight(source, i) + 1)

    def get_suggest(self, u: User):
        v: Vertex = self.get(u)
        arr = ArrayList()
        for i in self.adjacency_list[v.index]:
            if self.get_edge_weight(v, i[0]) != 0:
                arr.add(i)

        def compare(a, b):
            if a[1] >= b[1]:
                return True
            return False

        sort = MergeSort(compare)
        sort.sort(arr)
        return arr


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


class MergeSort:
    def __init__(self, compare):
        self.compare = compare

    def __merge_sort(self, Array: ArrayList, start, end):
        if start >= end:
            return
        mid = (start + end) // 2
        self.__merge_sort(Array, start, mid)
        self.__merge_sort(Array, mid + 1, end)
        self.__merge(Array, start, end)

    def __merge(self, Array, start, end):
        mid = (start + end) // 2
        i = start
        j = mid + 1
        arr = ArrayList()
        while i <= mid and j <= end:
            if self.compare(Array[i], Array[j]):
                arr.add(Array[i])
                i += 1
            else:
                arr.add(Array[j])
                j += 1
        while i <= mid:
            arr.add(Array[i])
            i += 1
        while j <= end:
            arr.add(Array[j])
            j += 1
        for k in range(start, end + 1):
            Array[k] = arr.list[k - start]

    def sort(self, Array: ArrayList):
        self.__merge_sort(Array, 0, Array.filled - 1)
