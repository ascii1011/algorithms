#!/usr/bin/python2.7 -tt

"""

Binary Search Tree

### complexity break downs ###
Excellent === O(1)
Good      === O(log(n))
Fair      === O(n)
bad       === O(n log(n))
Horrible  === ...
### end break down ###

Stats:
~Complexity:   Ave        Worst
Space:         O(n)       O(n)          
Search:        log2(n)    O(n)
Insert:        log2(n)    O(n)
Delete:        log2(n)    O(n)

Notes:
Binary Search Tree appears great on average, but does look a little ugly for big data as we move toward worst cases.  Skip List seems to be almost identical, but does take up more space.  Better choices might come from B-Tree, Red-Black Tree, & AVL Tree with regards to complexity.

References:
wiki: https://en.wikipedia.org/wiki/Binary_search_tree
Initial code: https://www.youtube.com/watch?v=YlgPi75hIBc
Deeper functionality: http://interactivepython.org/runestone/static/pythonds/Trees/bst.html
Traversal notes on "*Order" methods: https://www.youtube.com/watch?v=xoU69C4lKlM
Complexity breakdowns: http://bigocheatsheet.com/
"""


class Node:

    """
    additional features:
    hasChild, isLRChild, isRoot, isLeaf,
    hasAnyChildren, hasBothChildren,
    replaceNodeData, etc...
    """

    def __init__(self, val):
        self.value = val
        self.leftChild = None
        self.rightChild = None

    def insert(self, data):
        if self.value == data:
            return False
        elif self.value > data:
            if self.leftChild:
                return self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
                return True
        else:
            if self.rightChild:
                return self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                return True

    def find(self, data):
        if self.value == data:
            return True
        elif self.value > data:
            if self.leftChild:
                return self.leftChild.find(data)
            else:
                return False

        else:
            if self.rightChild:
                return self.rightChild.find(data)
            else:
                return False

    def preorder(self):
        """
        Preorder traversal output is the same as the insert sequence
        process:
        1. Visit the root
        2. Traverse the left subtree
        3. Traverse the right subtree
        """
        if self:
            print (str(self.value))
            if self.leftChild:
                self.leftChild.preorder()
            if self.rightChild:
                self.rightChild.preorder()

    def postorder(self):
        """
        Process:
        1. Traverse the left subtree
        2. Traverse the right subtree
        3. Visit the root
        """
        if self:
            if self.leftChild:
                self.leftChild.postorder()
            if self.rightChild:
                self.rightChild.postorder()
            print (str(self.value))

    def inorder(self):
        """
        1. Traverse the left subtree
        2. Visit the root
        3. Traverse the right subtree
        """
        if self:
            if self.leftChild:
                self.leftChild.inorder()
            print (str(self.value))
            if self.rightChild:
                self.rightChild.inorder()


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False

    def preorder(self):
        print("PreOrder")
        self.root.preorder()

    def postorder(self):
        print("PostOrder")
        self.root.postorder()

    def inorder(self):
        print("InOrder")
        self.root.inorder()



def test1():
    bst = Tree()
    
    values = [7,1,0,3,2,5,4,6,9,8,10]
    for v in values:
        bst.insert(v)
        
    bst.preorder()
    bst.postorder()
    bst.inorder()
    

if __name__ == "__main__":
    pass
