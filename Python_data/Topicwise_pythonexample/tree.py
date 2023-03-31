class Node:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def printTree(self):
        if self.leftChild:
            self.leftChild.printTree()
        print(self.data)
        if self.rightChild:
            self.rightChild.printTree()

    def insert(self, data):
        if data < self.data:
            if self.leftChild: 
                self.leftChild.insert(data)
            else:
                self.leftChild= Node(data)
                return
        else:
             
            if self.rightChild:
                self.rightChild.insert(data)
            else:
                self.rightChild= Node(data)
                return
            
    def search(self,value):
        if value == self.data:
            return str(value) +" is found in BST"
        elif value < self.data:
            if self.leftChild:
                return self.leftChild.search(value)
            else:
                return str(value) +" is not found in BST"
        else:
            if self.rightChild:
                return self.rightChild.search(value)
            else:
                return str(value)+" is not found in BST"

root = Node(27)

root.insert(12)
root.insert(45)
root.insert(5)
root.insert(16)
root.insert(99)
root.printTree()
print(root.search(12))
print(root.search(3))