from os import system

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
    
    def addChildFromHead(self, list):
        for i in list:
            if self.head == None:
                self.head = Node(i)
            else:
                temp = self.head
                while(temp.next):
                    temp = temp.next
                temp.next = Node(i)
                
    
    def addChildFromTail(self, list):
        for i in list:
            if self.tail == None:
                self.tail = Node(i)
            else:
                temp = self.tail
                while(temp.prev):
                    temp = temp.prev
                temp.prev = Node(i)
    
    def printList(self, node):
        if node != None:
            print(str(node.data), end=' ')
            self.printList(node.next)


cls()
ll = LinkedList()
while(True):
    print()
    print('..................Double Linked List.................')
    print('1 - Add elements from head')
    print('2 - add element from tail')
    print('3 - delete value')
    print('4 - Print List')
    print('5 - Clear Console')
    print('6 - Exit')
    x = int(input('Enter your feedback :: '))
    if x ==1 :
        ll.addChildFromHead([int(x) for x in input('Enter list :: ').split(' ')])
    elif x == 2:
        ll.addChildFromTail([int(x) for x in input('Enter list :: ').split(' ')])
    elif x == 3:
        ll.deleteNode(ll.head, int(input('Enter Value :: ')))
    elif x == 4:
        ll.printList(ll.head)
    elif x == 5:
        cls()
    else:
        break