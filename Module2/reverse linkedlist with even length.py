class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linkedlist:
    def __init__(self):
        self.head=None

    def insertatend(self,newnode):
        if self.head is None:
            self.head=newnode
        else:
            lastnode=self.head
            while True:
                if lastnode.next is None:
                    break
                lastnode=lastnode.next
            lastnode.next=newnode

    def reverselist(self):
        prev=None
        next=None
        curr=self.head
        while curr is not None:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        self.head=prev


    def find(self):
        len=1
        curr=self.head
        prev=None
        while curr is not None:
            if len%2==0:
                next=curr.next
                curr.next=prev
                prev=curr
                curr=next
            prev=curr
            curr=curr.next
            len+=1




    def printlist(self):
        currnode=self.head
        while True:
            if currnode is None:
                break
            print(currnode.data)
            currnode=currnode.next



node1=Node("1")
node2=Node("2")
node3=Node("3")
node4=Node("4")
list=Linkedlist()
list.insertatend(node1)
list.insertatend(node2)
list.insertatend(node3)
list.insertatend(node4)

list.printlist()

print("after reversing")
list.reverselist()
list.printlist()
print("after revesring in even length")
list.find()
list.printlist()
