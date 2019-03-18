from abc import ABC, abstractmethod

class AbstractHeap(ABC):

    def __len__(self):
        return len(self.data)

    def heapsort(self):
        for i in range(len(self.data) - 1, -1, -1):
            self.heapify(i)

    @abstractmethod
    def bubble_up(self, parentIndex, currentIndex):
        pass

    @abstractmethod
    def heapify(self, position):
        pass

    @abstractmethod
    def insert(self, val):
        pass

    @abstractmethod
    def delete(self, position):
        pass

    @abstractmethod
    def extract(self, position):
        pass

    @staticmethod
    def left(position):
        return position * 2 + 1

    @staticmethod
    def right(position):
        return position * 2 + 2

    @staticmethod
    def parent(position):
        return (position - 1)//2

class Heap(AbstractHeap):

    def __init__(self, data=[]):
        self.data = data
        if len(self.data) > 1:
            self.heapsort()

    def bubble_up(self, parentIndex, currentIndex):
        while parentIndex >= 0 and self.data[currentIndex] > self.data[parentIndex]:
            self.data[parentIndex], self.data[currentIndex] = self.data[currentIndex], self.data[parentIndex]
            currentIndex = parentIndex
            parentIndex = Heap.parent(currentIndex)

    def heapify(self, position):
        largest = position
        left_position = Heap.left(position)
        right_position = Heap.right(position)
        
        if left_position < len(self.data) and self.data[largest] < self.data[left_position]:
            
            largest = left_position
        if right_position < len(self.data) and self.data[largest] < self.data[right_position]:
            largest = right_position

        if largest != position:
            self.data[position], self.data[largest] = self.data[largest], self.data[position]
            self.heapify(largest)

    def insert(self, val):
        self.data.append(val)

        currentIndex = len(self.data) - 1
        parentIndex = Heap.parent(currentIndex)
        self.bubble_up(parentIndex, currentIndex)

    def delete(self, position):
        if len(self.data) > 0:
            deleted = self.data[position]
            lastIndex = len(self.data) - 1
    
            if len(self.data) > 2 and position != lastIndex:
                self.data[position] = self.data[lastIndex]
                self.data = self.data[:lastIndex]
                
                parentIndex = Heap.parent(position)
                if parentIndex >= 0 and self.data[parentIndex] < self.data[position]:
                    self.bubble_up(parent, position)
                else:
                    self.heapify(position)
            else:
                if position != lastIndex:
                    self.data[position] = self.data[lastIndex]
                self.data = self.data[:lastIndex]
            return deleted
        else:
            return None

    def extract(self):
        return self.delete(0)

    def peek(self):
        if len(self.data) < 1:
            return None
        return self.data[0]

class MinHeap(Heap):
    def __init__(self, data=[]):
        self.data = data
        if len(self.data) > 1:
            self.heapsort()

    def bubble_up(self, parentIndex, currentIndex):
        while parentIndex >= 0 and self.data[currentIndex] < self.data[parentIndex]:
            self.data[parentIndex], self.data[currentIndex] = self.data[currentIndex], self.data[parentIndex]
            currentIndex = parentIndex
            parentIndex = Heap.parent(currentIndex)

    def heapify(self, position):
        smallest = position
        left_position = Heap.left(position)
        right_position = Heap.right(position)
        
        if left_position < len(self.data) and self.data[smallest] > self.data[left_position]:
            smallest = left_position
        if right_position < len(self.data) and self.data[smallest] > self.data[right_position]:
            smallest = right_position

        if smallest != position:
            self.data[position], self.data[smallest] = self.data[smallest], self.data[position]
            self.heapify(smallest)

    def insert(self, data):
        self.data.append(data)

        currentIndex = len(self.data) - 1
        parentIndex = Heap.parent(currentIndex)
        self.bubble_up(parentIndex, currentIndex)

    def delete(self, position):
        if len(self.data) > 0:
            deleted = self.data[position]
            lastIndex = len(self.data) - 1
    
            if len(self.data) > 2 and position != lastIndex:
                self.data[position] = self.data[lastIndex]
                self.data = self.data[:lastIndex]
                
                parentIndex = Heap.parent(position)
                if parentIndex >= 0 and self.data[parentIndex] > self.data[position]:
                    self.bubble_up(parent, position)
                else:
                    self.heapify(position)
                return deleted
            else:
                if position != lastIndex:
                    self.data[position] = self.data[lastIndex]
                self.data = self.data[:lastIndex]
        else:
            return None
