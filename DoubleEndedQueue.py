from os import *
from array import *


def cls():
    system('clear')


class Queue:
    def __init__(self):
        self.arr = array('i', [0 for i in range(10)])
        self.front = 0
        self.rear = 0

    def printQueue(self):
        for i in range(self.front, self.rear):
            print(self.arr[i])

    def insert_from_rear(self, elem):
        if (self.rear == self.arr.__len__()):
            cls()
            print('overflow')
        else:
            cls()
            self.arr[self.rear] = elem
            print('Pushed value into rear= '+str(self.arr[self.rear]))
            self.rear = self.rear + 1

    def insert_from_front(self, elem):
        if self.rear == self.arr.__len__():
            cls()
            print('overflow')
        else:
            for i in range(self.rear, self.front, -1):
                self.arr[i] = self.arr[i-1]
            self.arr[self.front] = elem
            print('Pushed value into front= '+str(self.arr[self.front]))
            self.rear = self.rear + 1

    def del_from_rear(self):
        if (self.front == self.rear):
            cls()
            print('underflow')
        else:
            cls()
            print('poped value from rear = '+str(self.arr[self.rear-1]))
            self.rear = self.rear - 1

    def del_from_front(self):
        if (self.front == self.rear):
            cls()
            print('underflow')
        else:
            cls()
            print('poped value from front= '+str(self.arr[self.front]))
            self.front = self.front + 1


que = Queue()
cls()
while(True):
    print('which operation you want to perform')
    print('1-insert_from_rear')
    print('2-insert_from_front')
    print('3-del_from_rear')
    print('4-del_from_front')
    print('5-printQueue')
    print('6-exit')
    x = int(input('Enter your feed back:'))
    if (x == 1):
        que.insert_from_rear(int(input('Enter value to add in rear:')))
    if (x == 2):
        que.insert_from_front(int(input('Enter Value to add in front:')))
    if (x == 3):
        que.del_from_rear()
    if (x == 4):
        que.del_from_front()
    if (x == 5):
        que.printQueue()
    if (x == 6):
        exit()
