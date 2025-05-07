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

    def reverselinkedlist(self):
        dummy=Node()
        k=3
        dummy.next=self.head
        ptr=dummy
        while (ptr!=None):
            tracker=ptr
            for i in range(k):
                if tracker==None:
                    break
                tracker=tracker.next
            if tracker==None:
                break












    def printlist(self):
        currnode=self.head
        while True:
            if currnode is None:
                break
            print(currnode.data)
            currnode=currnode.next




node1=Node("sheet")
node2=Node("sam")
node3=Node("mad")
node4=Node("god")
list=Linkedlist()
list.insertatend(node1)
list.insertatend(node2)
list.insertatend(node3)
list.insertatend(node4)
print("insert at end")
list.printlist()




# list.insertathead(node3)
# print("insert at head")
# list.printlist()
# list.insertatmiddle(node4,1)
# print("insert at middle")
# list.printlist()




