class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data

class Binarytree:
    def __init__(self):
        self.root=None

    def insert(self,data):
        if self.root is None:
            self.root=Node(data)
            return
        root=self.root
        while root:
            if data < root.data:
                if root.left is not None:
                    root = root.left
                else:
                    root.left = Node(data)
                    break
            elif data > root.data:
                if root.right is not None:
                    root = root.right
                else:
                    root.right = Node(data)
                    break
            else:
                break
    def preorder(self,root):
        if root is None:
            return
        print(root.data,end=" ")
        self.preorder(root.left)
        self.preorder(root.right)


    def ancestor(self,root,p,q):
        curr=root
        while curr:
            if p.data>curr.data and q.data >curr.data:
                curr=curr.right
            elif p.data < curr.data and q.data < curr.data:
                curr = curr.left
            else:
                return curr.data

    def validbfs(self,root,left,right):
        if root is None:
            return True
        if left>root.data and right<root.data:
            return False
        return (self.validbfs(root.left,left,root.data) and self.validbfs(root.right,root.data,right))














tree1=Binarytree()
tree1.insert(5)
tree1.insert(3)
tree1.insert(8)
tree1.insert(4)
tree1.insert(1)
tree1.insert(2)
tree1.insert(7)
tree1.insert(9)
node8=Node(2)
node9=Node(4)

print("tree1 preorder ",end=" ")
tree1.preorder(tree1.root)
print()
print(tree1.ancestor(tree1.root,node8,node9))
print("is it valid bst")
print(tree1.validbfs(tree1.root,float("-inf"),float("inf")))
