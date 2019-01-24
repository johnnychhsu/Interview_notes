class MinHeap:
    def __init__(self):
        self.heaplist = [0]
        self.currentSize = 0

    def percUp(self, i):
        while i // 2 > 0:
            if self.heaplist[i] < self.heaplist[i//2]:
                self.heaplist[i], self.heaplist[i//2] = self.heaplist[i//2], self.heaplist[i]

    def insert(self, val):
        self.heaplist.append(val)
        self.currentSize += 1
        self.percUp(self.currentSize)

    def percDown(self, i):
        while i * 2 <= self.currentSize:
            mc = self.minChild(i)
            if self.heaplist[i] > self.heaplist[mc]:
                self.heaplist[i], self.heaplist[mc] = self.heaplist[mc], self.heaplist[i]
            i = mc

    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heaplist[i * 2] < self.heaplist[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def deleteMin(self):
        minVal = self.heaplist[1]
        last = self.heaplist.pop()
        self.currentSize -= 1
        self.heaplist[1] = last
        self.percDown(1)
        return minVal

    def buildHeap(self, alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heaplist += alist
        while i > 0:
            self.percDown(i)
            i -= 1

test = [9,6,5,2,3]
myHeap = MinHeap()
myHeap.buildHeap(test)
print(myHeap.heaplist)
