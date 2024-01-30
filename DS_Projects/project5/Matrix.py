from ArrayList import ArrayList


class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.array = ArrayList()
        for i in range(self.rows):
            arr = ArrayList()
            arr.make_from_list([None for j in range(self.columns)])
            self.array.add(arr)

    def __str__(self):
        ret = ""
        for i in range(self.rows):
            st = ""
            for j in range(self.columns):
                st += repr(self.array[i][j]) + " "
            ret += st + "\n"
        return ret

    def __repr__(self):
        ret = ""
        for i in range(self.rows):
            st = ""
            for j in range(self.columns):
                st += repr(self.array[i][j]) + " "
            ret += st + "\n"
        return ret

    def __contains__(self, item):
        ans = False
        for i in self.array:
            if (i is not None) and (item in i):
                ans = True
                break
        return ans

    def __setitem__(self, key, value):
        self.array[key] = value

    def __getitem__(self, item):
        return self.array[item]

    def __len__(self):
        return self.rows * self.columns

    def __iter__(self):
        for i in range(self.rows):
            for j in range(self.columns):
                yield self.array[i][j]

    def add_row(self, filler=None):
        arr = ArrayList()
        arr.make_from_list([filler for i in range(self.columns)])
        self.array.add(arr)
        self.rows += 1

    def add_column(self, filler=None):
        for i in self.array:
            i.add(filler)
        self.columns += 1

    def remove_row(self):
        self.array.remove_last()
        self.rows -= 1

    def remove_column(self):
        for i in self.array:
            i.remove_last()
        self.columns -= 1
