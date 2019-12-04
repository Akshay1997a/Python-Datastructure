from os import *


def cls():
    system('clear')


class Node:
    def __init__(self, val):
        self.prev = None
        self.data = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def printList(self, direction):
        if direction == 1:
            temp = self.head
            while temp:
                print(str(temp.data)+' ', end=' ')
                temp = temp.next
        else:
            temp = self.tail
            while temp:
                print(str(temp.data)+' ', end=' ')
                temp = temp.prev

    def addNodeInTail(self, val):
        if self.head == None:
            cls()
            self.head = Node(val)
        else:
            cls()
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(val)
            temp.next.prev = temp
            self.tail = temp.next

    def addNodeInHead(self, val):
        if self.tail == None:
            self.tail = Node(val)
        else:
            temp = self.tail
            while temp.prev:
                temp = temp.prev
            temp.prev = Node(val)
            temp.prev.next = temp
            self.head = temp.prev

    def searchElem(self, elem):
        temp = self.head
        flag = 0
        while temp:
            if elem == temp.data:
                flag = 1
                temp = None
            else:
                temp = temp.next
        if flag == 1:
            print('element found')
        else:
            print('elemwnt not found')

    def deleteElem(self, elem):
        temp = self.head
        while temp:
            if elem == temp.data:
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
                temp = None
            else:
                temp = temp.next


cls()
ll = LinkedList()
while(True):
    print()
    print('which operation you want to perform')
    print('1-add Node in tail')
    print('2-add node in head')
    print('3-printList')
    print('4-search element')
    print('5-delete element')
    print('6-exit')
    x = int(input('Enter your feed back:'))
    if (x == 1):
        ll.addNodeInTail(input('Enter value to add node in tail:'))
    if (x == 2):
        ll.addNodeInHead(input('Enter value to add node in head'))
    if (x == 3):
        ll.printList(int(input('1-forword \n2-reverse \n=')))
    if (x == 4):
        ll.searchElem(input('enter element to search:'))
    if (x == 5):
        ll.deleteElem(input('element to delete:'))
    if (x == 6):
        break
