class Node:
    def __init__(self,data):
        self.next=None
        self.data=data

class Binarytree:
    def __init__(self):
        self.head=None

    def insertatned(self,newnode):
        if self.head is None:
            self.head=newnode
        else:
            lastnode = self.head
            while True:
                if lastnode.next is None:
                    break
                lastnode = lastnode.next
            lastnode.next = newnode



    def mergelist(self,lst1,lst2):
        dummy=node=Node(None)
        while lst1 and lst2:
            if lst1.data < lst2.data:
                node.next=lst1
                lst1=lst1.next
            else:
                node.next = lst2
                lst2 = lst2.next



            node=node.next

        node.next=lst1 or lst2


        return dummy.next


    def printlist(self):
        currnode=self.head
        while True:
            if currnode is None:
                break

            print(currnode.data,end='--')
            currnode=currnode.next
node1=Node(2)
node2=Node(5)
node3=Node(9)
node4=Node(4)
node5=Node(7)
node6=Node(8)

lst1=Binarytree()
lst2=Binarytree()
lst1.insertatned(node1)
lst1.insertatned(node2)
lst1.insertatned(node3)
lst2.insertatned(node4)
lst2.insertatned(node5)
lst2.insertatned(node6)

print("list1 is")
lst1.printlist()
print()
print("list2 is")
lst2.printlist()

merge=Binarytree()
merge.head=merge.mergelist(lst1.head,lst2.head)
print("after merging")
merge.printlist()



