from os import system


def cls():
    system('clear')


class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def addNode(self, list):
        for i in list:
            if self.head == None:
                self.head = Node(i)
            else:
                temp = self.head
                while(temp.next):
                    temp = temp.next
                temp.next = Node(i)

    def deleteNode(self, node, val):
        if node == None:
            print('Value not found')
            return False
        if self.head.data == val:
            self.head = self.head.next
        else:
            if node.data == val:
                return node.next
            else:
                temp = self.deleteNode(node.next, val)
                if temp != False:
                    node.next = temp
                    return False
                return False

    def printNode(self, node):
        if node != None:
            print(str(node.data), end=' ')
            self.printNode(node.next)


cls()
ll = LinkedList()
while(True):
    print()
    print('...................Linked List........................')
    print('1 - Add list')
    print('2 - Delete Node')
    print('3 - Print List')
    print('4 - Clear console')
    print('5 - exit')
    x = int(input('Enter your feedback :: '))
    if (x == 1):
        ll.addNode([int(x) for x in input('Enter List :: ').split(' ')])
        print('current list :: ', end='')
        ll.printNode(ll.head)
    elif (x == 2):
        ll.deleteNode(ll.head, int(input('Enter value: : ')))
        print('current list :: ', end='')
        ll.printNode(ll.head)
    elif (x == 3):
        ll.printNode(ll.head)
    elif (x == 4):
        cls()
    else:
        break
