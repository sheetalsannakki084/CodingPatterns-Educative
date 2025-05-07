from collections import deque


class Node:
    def __init__(self ,data):
        self.left =None
        self.right =None
        self.data =data
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

    def levelorder(self,root):
        if root is None:
            return
        q=[]
        q.append(root)
        while q:
            root=q.pop(0)
            print(root.data,end="--")
            if root.left is not None:
                q.append(root.left)
            if root.right is not None:
                q.append(root.right)


    def levelwise(self,root):
        if root is None:
            return
        q=deque()
        result=[]
        q.append(root)
        while q:
            level=[]
            for i in range(len(q)):
                root=q.popleft()
                level.append(root.data)
                if root.left is not None:
                    q.append(root.left)
                if root.right is not None:
                    q.append(root.right)
            result.append(level)

        return result

















tree1=Binarytree()
tree1.insert(5)
tree1.insert(3)
tree1.insert(8)
tree1.insert(4)
tree1.insert(1)
tree1.insert(2)
tree1.insert(7)
tree1.insert(9)

print(tree1.levelorder(tree1.root))
print(tree1.levelwise(tree1.root))