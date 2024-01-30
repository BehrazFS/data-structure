class ArrayList:
    def __init__(self):
        self.filled = 0
        self.size = 1
        self.list = [None for i in range(self.size)]
        self.changed = True

    def make_from_list(self, the_list: list):
        for i in the_list:
            self.add(i)

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
        for i in self.list:
            if i is not None:
                yield i

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
        # """
        # mixes the order of items
        # :param item:
        # :return:
        # """
        arr = ArrayList()
        first = True
        for ii in range(len(self.list)):
            if (self.list[ii] is not None) and self.list[ii] == item and first:
                first = False
            else:
                arr.add(self.list[ii])
        self.list = arr.list
        self.filled = arr.filled
        self.size = arr.size
        self.changed = True
        # for ii in range(len(self.list)):
        #     if (self.list[ii] is not None) and self.list[ii] == item:
        #         s = self.filled - 1
        #         self.list[ii] = self.list[s]
        #         self.remove_last()
        #         break

    def remove_all(self, item):
        arr = ArrayList()
        for ii in self.list:
            if (ii is not None) and (ii != item):
                arr.add(ii)
        self.list = arr.list
        self.filled = arr.filled
        self.size = arr.size
        self.changed = True

    def reverse(self):
        arr = ArrayList()
        for ii in range(len(self.list)):
            if self.list[len(self.list) - 1 - ii] is not None:
                arr.add(self.list[len(self.list) - 1 - ii])
        self.list = arr.list
        self.filled = arr.filled
        self.size = arr.size
        self.changed = True
