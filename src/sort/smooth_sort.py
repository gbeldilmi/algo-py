class SmoothTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def add_value(self, value):
        if value > self.value:
            return SmoothTree(value, self)
        if self.left == None:
            self.left = SmoothTree(value)
        elif self.left.value < value:
            if self.right == None:
                self.right = SmoothTree(value)
            else:
                self.right = self.right.add_value(value)
        else:
            self.left = self.left.add_value(value)
        return self

    def to_list(self):
        if self.right == None:
            if self.left == None:
                return [self.value]
            return self.left.to_list() + [self.value]
        return self.left.to_list() + self.right.to_list() + [self.value]


def smooth_sort(arr):
    t = SmoothTree(arr[0])
    for i in range(1, len(arr)):
        t = t.add_value(arr[i])
    return t.to_list()


if __name__ == '__main__':
    arr = [2, 8, 3, 1, 5, 7, 6, 4]
    print(smooth_sort(arr))
    print(arr)
