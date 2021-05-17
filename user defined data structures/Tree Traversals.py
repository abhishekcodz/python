#creating a n:de class
class Node:
    def __init__(self,val):
        self.childleft = None
        self.childright = None
        self.nodedata = val

# Creating an instance of the Node class to construct
root = Node(1)
root.childleft = Node(2)
root.childright = Node(3)
root.childleft.childleft = Node(4)
root.childleft.childright = Node(5)
'''
def InOrder(root):
    if root:
        InOrder(root.childleft)
        print(root.nodedata, end = " ")
        InOrder(root.childright)
InOrder(root)
'''
'''
def preOrder(root):
    if root:
        print(root.nodedata, end = " ")
        preOrder(root.childleft)
        preOrder(root.childright)
preOrder(root)
'''
def preOrder(root):
    if root:
        preOrder(root.childleft)
        preOrder(root.childright)
        print(root.nodedata, end = " ")
preOrder(root)
