# sucessfully done
from array import *
from os import *


class Stack:
    def __init__(self):
        self.arr = array('i', [0, 0, 0, 0, 0])
        self.top = -1

    def push(self, elm):
        if (self.top != 5-1):
            self.top = self.top + 1
            self.arr[self.top] = elm
        else:
            print('over flow')

    def pop(self):
        if(self.isEmpty()):
            print('underflow')
        else:
            self.top = self.top-1

    def isEmpty(self):
        if(self.top == -1):
            return True
        else:
            return False

    def printStack(self):
        for i in range(self.top+1):
            print(self.arr[i])


stk = Stack()
while(True):
    print('which operation you want to perform')
    print('1-push')
    print('2-pop')
    print('3-print')
    print('4-exit')
    x = int(input('Enter your feed back:'))
    if (x == 1):
        stk.push(int(input('Enter value:')))
    if (x == 2):
        stk.pop()
    if (x == 3):
        stk.printStack()
    if (x == 4):
        exit()
