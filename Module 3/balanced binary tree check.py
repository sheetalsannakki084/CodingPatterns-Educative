class Node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None


class Binarytree:
    def __init__(self):
        self.root=None

    def insert(self,data):
        if self.root is None:
            self.root=Node(data)
            return

        root=self.root
        while root:
            if data<root.data:
                if root.left is not None:
                    root=root.left
                else:
                    root.left=Node(data)
                    break

            elif data>root.data:
                if root.right is not None:
                    root=root.right
                else:
                    root.right=Node(data)
                    break
            else:
                break


    def inorder(self,root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.data,end="--")
        self.inorder(root.right)






    def balanced(self):
        return self.helper(self.root)!=-1


    def helper(self,root):
        if root is None:
            return 0

        left=self.helper(root.left)
        if left==-1:
            return -1
        right=self.helper(root.right)
        if right==-1:
            return -1

        if abs(left-right)>1:
            return -1

        return 1+max(left,right)





obj=Binarytree()
obj.insert(9)
obj.insert(5)
obj.insert(4)
obj.insert(12)
obj.insert(10)
obj.insert(11)
print("in order")
print(obj.inorder(obj.root))
print()
print(obj.balanced())


