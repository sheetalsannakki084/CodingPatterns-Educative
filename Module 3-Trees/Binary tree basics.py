class Node:
    def __init__(self,data):
        self.left=None
        self.data = data
        self.right=None


class Binarytree:
    def __init__(self):
        self.root =None


    def inserttree(self,data):
        if self.root is None:
            self.root=Node(data)


        root=self.root
        while root:
            if data < root.data:
                if root.left is None:
                    root.left=Node(data)
                    break


                else:
                    root=root.left


            elif data>root.data:
                if root.right is None:
                    root.right=Node(data)
                    break

                else:
                    root=root.right


            else:
                break

    def inorder(self,root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.data,end="--")
        self.inorder(root.right)

    def depth(self,root):
        if root is None:
            return 0
        lc=self.depth(root.left)
        rc=self.depth(root.right)

        return 1+max(lc,rc)


    def diameter(self,root):
        self.dia=0 #setting the diameter to 0
        def height(root):
            if root is None:
                return 0
            lc=height(root.left)# height of left child
            rc=height(root.right)  # height of rigth child

            self.dia=max(self.dia,lc+rc) #calculate dia bfr going to next node

            return 1+max(lc,rc)  #calculte height
        height(root)
        return self.dia



# Local variables (like dia without self) only exist within the method and do not persist across recursive calls.
# persist means its hols values as long as recursive call we do  it wil rest to 0
#if its local everytime it reset 0 not hold previous values
# Instance variables (like self.dia) are accessible throughout the class, and their values persist across recursive
# calls and method calls, which is why self.dia is necessary to track the maximum diameter of the tree correctly.








tree=Binarytree()
tree.inserttree(6)
tree.inserttree(4)
tree.inserttree(5)
tree.inserttree(8)
tree.inserttree(7)
print("inodeer is")
print(tree.inorder(tree.root))
# print("height of binary tree")
# print(tree.height(tree.root))
print("diameter of binary tree")
print(tree.diameter(tree.root))



# here down just adding values not based bst
# tree=Binarytree()
# tree.root=Node(1)
# tree.root.left=Node(2)
# tree.root.right=Node(3)
# tree.root.left.left=Node(4)
# print("inorder")
# tree.inorder(tree.root)
# print()
