from abc import ABC, abstractmethod


class Heap(ABC):
    def __init__(self):
        self.heap = []

    def swap(self, index_1, index_2):
        self.heap[index_1], self.heap[index_2] = self.heap[index_2], self.heap[index_1]

    @staticmethod
    def parent(index):
        return index // 2

    @staticmethod
    def left_child(index):
        return index * 2

    @staticmethod
    def right_child(index):
        return index * 2 + 1

    @abstractmethod
    def sift_up(self, i):
        ...

    @abstractmethod
    def sift_down(self, i):
        ...

    @abstractmethod
    def build_heap(self, data):
        """
        :param data: Array to be converted to a heap
        :return: Heap array
        """


class MaxHeap(Heap):
    def __init__(self, data):
        super().__init__()
        self.heap = self.build_heap(data)

    def sift_up(self, i):
        while i > 1 and self.heap[self.parent(i)] < self.heap[i]:
            self.swap(self.parent(i), i)
            i = self.parent(i)

    def sift_down(self, i):
        max_index = i

        left = self.left_child(i)
        if left < self.size:
            if self.heap[left] > self.heap[max_index]:
                max_index = left

        right = self.right_child(i)
        if right < self.size:
            if self.heap[right] > self.heap[max_index]:
                max_index = right

        if i != max_index:
            self.swap(i, max_index)
            self.sift_down(max_index)

    def build_heap(self, data):
        self.heap = data
        self.size = len(data)

        for i in reversed(range(self.size // 2 + 1)):
            self.sift_down(i)

        return self.heap


class MinHeap(Heap):
    def __init__(self, data):
        super().__init__()
        self.heap = self.build_heap(data)

    def sift_up(self, i):
        while i > 1 and self.heap[self.parent(i)] > self.heap[i]:
            self.swap(self.parent(i), i)
            i = self.parent(i)

    def sift_down(self, i):
        max_index = i

        left = self.left_child(i)
        if left < self.size:
            if self.heap[left] < self.heap[max_index]:
                max_index = left

        right = self.right_child(i)
        if right < self.size:
            if self.heap[right] < self.heap[max_index]:
                max_index = right

        if i != max_index:
            self.swap(i, max_index)
            self.sift_down(max_index)

    def build_heap(self, data):
        self.heap = data
        self.size = len(data)

        for i in reversed(range(self.size // 2 + 1)):
            self.sift_down(i)

        return self.heap


A = [0, 2, 3, 1, 4, 5, 9]
max_heap = MaxHeap(A)
min_heap = MinHeap(A)
print(max_heap.heap)
print(min_heap.heap)
