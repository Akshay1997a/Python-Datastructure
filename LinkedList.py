from os import *

def cls():
    system('clear')

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def printList(self):
        cls()
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
    
    def addNode(self,val):
        cls()
        if self.head == None:
            self.head = Node(val)
        else:
            temp = self.head
            while(temp.next):
                temp = temp.next
            temp.next = Node(val)

cls()
ll = LinkedList()
while(True):
    print('which operation you want to perform')
    print('1-add Node')
    print('2-printList')
    print('3-exit')
    x = int(input('Enter your feed back:'))
    if (x == 1):
        ll.addNode(input('Enter value:'))
    if (x == 2):
        ll.printList()
    if (x == 3):
        break