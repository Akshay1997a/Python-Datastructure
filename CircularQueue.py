from os import *
from array import *

def cls():
    system('clear')

class Queue:
    def __init__(self):
        self.arr = array('i',[None for i in range(10)])
        self.front = 0
        self.rear = 0

    def printQueue(self):
        cls()
        if (self.front == self.rear):
            print('Queue is empty')
        elif (self.front< self.rear):
            for i in range(self.front, self.rear):
                print(self.arr[i])
        else:
            for i in range(self.front, self.arr.__len__()):
                print(self.arr[i])
            for i in range(0, self.rear):
                print(self.arr[i])
    
    def enqueue(self):
        if ((self.rear +1 )%self.arr.__len__() == self.front):
            cls()
            print('overflow')
        elif (self.front == -1):
            self.front = 0
            self.rear = 0
            self.arr[self.rear] = elem
        
        else:
            self.rear = (self.rear + 1)% self.arr.__len__()
            self.arr[self.rear] = elem
    
    def dequeue(self):
        if (self.front == -1)
            