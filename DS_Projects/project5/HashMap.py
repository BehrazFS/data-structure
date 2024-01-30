import LinkedList
from LinkedList import LinkedList


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
