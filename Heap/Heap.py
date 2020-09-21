# use heapq library in python when allowed

class MinHeap():
    def __init__(self, nums):
        self.capacity = len(nums)
        self.heap = [n for n in nums] # copy of nums
        
        i = self.capacity-1
        
        while i >= 0:
            self.heapify_down(i)
            i=i-1
    
    def peek(self):
        if self.capacity > 0:
            return self.heap[0]
        else:
            return None
    
    def pop(self):
        if self.capacity > 0:
            minimum = self.heap[0]
            self.heap[0] = self.heap[self.capacity-1]
            self.capacity = self.capacity - 1
            self.heapify_down(0)
            return minimum
        else:
            return None
    
    def push(self, val):
        i = self.capacity
        self.capacity = self.capacity + 1
        if i < len(self.heap):
            self.heap[i] = val
        else:
            self.heap = self.heap + [val]
        self.heapify_up(i)
    
    def pushpop(self, val):
        if self.capacity > 0:
            if val <= self.heap[0]:
                return val
            else:
                minimum = self.heap[0]
                self.heap[0] = val
                self.heapify_down(0)
                return minimum
        else:
            return val
    
    def heapify_up(self, i):
        if i >= self.capacity or i <= 0:
            return None
        parent = (i-1)//2
        if parent >= 0 and self.heap[parent] > self.heap[i]:
            self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
            return self.heapify_up(parent)
        
    
    def heapify_down(self, i):
        if i >= self.capacity:
            return None
        left = 2*i + 1
        right = 2*i + 2
        
        lowest = i
        
        if left < self.capacity and self.heap[left] < self.heap[lowest]:
            lowest = left
        
        if right < self.capacity and self.heap[right] < self.heap[lowest]:
            lowest = right
        
        if lowest != i:
            self.heap[lowest], self.heap[i] = self.heap[i], self.heap[lowest]
            return self.heapify_down(lowest)


class MaxHeap():
    def __init__(self, nums=[]):
        self.heap = [-n for n in nums]
        heapq.heapify(self.heap)
        
    def push(self, val):
        heapq.heappush(self.heap, -val)
    def pop(self):
        return -heapq.heappop(self.heap)
    def pushpop(self, val):
        return -heapq.pushpop(self.heap, -val)
    def replace(self, val):
        return -heapq.heapreplace(self.heap, -val)

class KMinHeap():
    def __init__(self, k, nums):
        self.k = k
        self.heap = nums[:k]
        heapq.heapify(self.heap)
        for i in range(k, len(nums)):
            val = nums[i]
            if val > self.heap[0]:
                heapq.heappushpop(self.heap, val)
            
    def insert(self, val):
        # maintains the heap size k if it is already k or increases it by 1
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        else:
            if val > self.heap[0]:
                heapq.heappushpop(self.heap, val)


class KMaxHeap():
    def __init__(self, k, nums):
        self.k = k
        # using min heap to create a max heap by using negating the numbers
        self.heap = [-n for n in nums[:k]] 
        heapq.heapify(self.heap)
        for i in range(k, len(nums)):
            val = nums[i]
            # inoder to add an element to the k max heap, the element should be lesser than the top element
            # since we are dealing with negative numbers the comparision sign flips
            # val < heapmax
            # -val > -heapmax
            if -val > self.heap[0]:
                heapq.heappushpop(self.heap, -val)
            
    def insert(self, val):
        # val is the actual number to inserted into the max heap, not the negated number
        # maintains the heap size k if it is already k or increases it by 1
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, -val)
        else:
            # inoder to add an element to the k max heap, the element should be lesser than the top element
            # since we are dealing with negative numbers the comparision sign flips
            # val < heapmax
            # -val > -heapmax
            if -val > self.heap[0]:
                heapq.heappushpop(self.heap, -val)