# Original Author: sreekeshpadmanabhan@gmail.com
# Implementation of Heapsort algorithms as described & analyzed from Introduction to Algorithms by CLRS
# https://drive.google.com/file/d/121Ih7X4AMuo4239af91vRYXHpwBfVIaq/view?usp=sharing
import random

class HeapClass:
    def __init__(self):
        self.heap_size  = int(input("Heap size: "))
        self.heap = [] #[4,1,3,2,16,9,10,14,8,7]
        #append non-repetative random numbers to heap
        for rand in range(self.heap_size):
            rnumber=random.randint(1,100)
            if rnumber not in self.heap: self.heap.append(rnumber)
        self.sorted = []
        self.itracker = []
        print(self.heap)

    #Run Time: O(lg n)~O(h
    def max_heapify(self,index):
        largest = index
        left = 2*index+1
        right = 2*index+2
        
        if (left<len(self.heap) and self.heap[left]>self.heap[index]):
            largest = left
        else:
            largest = index
        
        if (right<len(self.heap) and self.heap[right]>self.heap[largest]):   
            largest = right
        # print(f"max_heapify left:{left}|right:{right}|heap[{index}]={self.heap[index]}->heap[{largest}]={self.heap[largest]}")
        self.itracker.append(index)
        if(largest!=index):
            temp =  self.heap[index]
            self.heap[index] = self.heap[largest]
            self.heap[largest] = temp
            self.max_heapify(largest)

    #Run Time: O(nlgn)~O(n) tight
    def build_max_heap(self):
        print(f"{len(self.heap)}")
        #+1 to include /2 floor in range
        for index in range(0,int((len(self.heap)-1)//2)+1):
            x = int((len(self.heap)-1)//2)-index
            print(f"build_max_heap index: {len(self.heap)} {int((len(self.heap)-1)//2)} {index} {x}")
            self.itracker = []
            self.max_heapify(x)
            print(self.itracker)
            print(self.heap)

    #Run Time: O(nlgn), 
    def heapsort(self):
        # build_max_heaps
        self.build_max_heap()
        last = 0
        # for i in range(0,int(len(self.heap)-1)):
        while (int(len(self.heap))>0):
            last = len(self.heap)-1
            # print(self.heap)
            self.sorted.append(self.heap[0])
            temp = self.heap[last]          #temp<-last
            self.heap[last] = self.heap[0]  #last<-first
            self.heap[0] = temp             #first<-temp
            self.heap = self.heap[:-1]
            # print(self.sorted)
            self.max_heapify(0)

hp = HeapClass()
# hp.build_max_heap()
hp.heapsort()
print(hp.sorted)
