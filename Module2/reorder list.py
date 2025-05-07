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

    def insertathead(self,newnode):
        temp=self.head
        self.head=newnode
        self.head.next=temp

    def insertatmiddle(self,newnode,pos):
        currnode=self.head
        count=0
        while True:
            if count==pos:
                prevnode.next=newnode
                newnode.next=currnode
                break
            prevnode = currnode
            currnode= currnode.next
            count += 1

    def findcircle(self):
        slow,fast=self.head

        while fast and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True

        return False

    def middleoflinkedlist(self):
        slow, fast = self.head,self.head

        while fast and fast.next is not None:
            slow = slow.next
            fast = fast.next.next



        curr=slow
        prev=None
        next=None
        while curr is not None:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next


        first=self.head
        second=prev
        while first and second:
            t1=first.next
            t2=second.next
            first.next=second
            second.next=t1
            first=t1
            second=t2



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
node5=Node("5")
list=Linkedlist()
list.insertatend(node1)
list.insertatend(node2)
list.insertatend(node3)
list.insertatend(node4)
list.insertatend(node5)
print("insert at end")
list.printlist()
print("after reorder")

list.middleoflinkedlist()
list.printlist()


# list.insertathead(node3)
# print("insert at head")
# list.printlist()
# list.insertatmiddle(node4,1)
# print("insert at middle")
# list.printlist()




