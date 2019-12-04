from array import *
from os import *

def cls():
    system('clear')

class Quere:
    def __init__(self):
        self.arr = array('i',[0 for i in range(10)])
        self.front = -1
        self.rear = -1

    def printQueue(self):
        for i in range(self.front, self.rear+1):
            print(str(self.arr[i])+' ', end=' ')
    
    def enqueue(self, elem):
        if (self.rear == self.arr.__len__()-1):
            cls()
            print('overflow')
        elif self.front == -1:
            cls()
            self.front = self.rear = 0
            self.arr[self.rear] = elem
        else:
            cls()
            self.rear = self.rear + 1
            self.arr[self.rear] = elem

    def dequeue(self):
        if self.front == self.rear+1:
            cls()
            print('underflow')
        else:
            cls()
            print('poped item = '+str(self.arr[self.front]))
            self.front = self.front + 1

que = Quere()
cls()
while(True):
    print('which operation you want to perform')
    print('1-enque')
    print('2-dequeue')
    print('3-print')
    print('4-exit')
    x = int(input('Enter your feed back:'))
    if (x == 1):
        que.enqueue(int(input('Enter value:')))
    if (x == 2):
        que.dequeue()
    if (x == 3):
        que.printQueue()
    if (x == 4):
        exit()