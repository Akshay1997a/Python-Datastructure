from os import *

def cls():
    system('clear')


class Node:
    def __init__(self, val):
        self.left = None
        self.data = val
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def printTree(self, root):
        cls()
        if root:
            self.printTree(root.left)
            print(str(root.data)+' ', end=' ')
            self.printTree(root.right)

    def addChild(self, val):
        cls()
        for i in range(val.__len__()):
            if self.root == None:
                self.root = Node(val[i])
            else:
                temp = self.root
                while temp:
                    if val[i] <= temp.data:
                        # print(str(val)+'<'+str(temp.data))
                        if temp.left == None:
                            temp.left = Node(val[i])
                            temp = None
                        else:
                            temp = temp.left
                    else:
                        # print(str(val)+'>'+str(temp.data))
                        if temp.right == None:
                            temp.right = Node(val[i])
                            temp = None
                        else:
                            temp = temp.right


    def search(self, node, val):
        cls()
        if node:
            if node.data == val:
                return node
            else:
                if val<=node.data:
                    return self.search(node.left, val)
                else:
                    return self.search(node.right, val)
        return False
    
    def removeChild(self,node, val):
        cls()
        if node:
            if node.data == val:
                if node.left == None and node.right == None:
                    return None
                elif node.left:
                    return node.left
                elif node.right:
                    return node.right
            else:
                if val <= node.data:
                    #node.left = self.removeChild(node.left, val)
                    temp = self.removeChild(node.left , val)
                    if temp != True and temp != False:
                        node.left = temp
                        return True
                    else:
                        return temp
                else:
                    temp = self.removeChild(node.right, val)    
                    if temp != True and temp != False:
                        node.right = temp
                        return True
                    else:
                        return temp    

        return False
        

cls()
t = Tree()
while(True):
    print()
    print('which operation you want to perform')
    print('1-add tree')
    print('2-search value')
    print('3-remove child')
    print('4-print tree')
    print('5-exit')
    x = int(input('Enter your feed back:'))
    if (x == 1):
        t.addChild([8,4,1,2,7,4])
    if (x==2):
        node = t.search(t.root, int(input('value :: ')))
        if node:
            print(node.data)
        else:
            print('value not found')
    if (x == 3):
        if t.removeChild(t.root, int(input('value to remove :: '))):
            print('child remover')
        else:
            print('not found')
    if (x == 4):
        t.printTree(t.root)
    if (x == 5):
        break
