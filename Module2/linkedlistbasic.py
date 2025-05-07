class Node:
    def __init__(self,data):
        self.data=data
        self.next=None




class LinkedList():
    def __init__(self):
         self.head =None


    def insertatend(self,newnode):
        if self.head is None:
            self.head=newnode
        else:
            lastnode = self.head
            while True:
                if lastnode.next is None:
                    break
                lastnode=lastnode.next
            lastnode.next=newnode

    def insertathead(self,newnode): #inserting at head and new method defined fr that
        temp=self.head
        self.head=newnode
        self.head.next=temp
        del temp

    def lengthlist(self):

        currnode=self.head
        length=0
        while currnode is not None:
            length+=1
            currnode=currnode.next
        return length

    def insertmiddle(self,newnode,position):
        if position<0 or position>self.lengthlist():
            print("invalid position")
            return
        if position ==0:
            self.insertathead(newnode) #if thy are trying to add at 0 pos means at head den cal insertat head method
            return
        currentnode=self.head
        currpose=0
        while True:
            if currpose==position:
                prevnode.next=newnode
                newnode.next=currentnode
                break


            prevnode=currentnode
            currentnode=currentnode.next
            currpose+=1




    def printlist(self):
        if self.head is None:
            print("list s empty")
            return

        currntNode=self.head
        while True:
            if currntNode is None:
                break
            print(currntNode.data)
            currntNode = currntNode.next






node1=Node("kia")
link=LinkedList()
link.insertatend(node1)
node2=Node("mia")
link.insertatend(node2)
node3=Node("sia")
link.insertathead(node3)
node4=Node("via")
link.insertmiddle(node4,1)






# node will have 2 items.one is data and one s pointer which pointing to next so this will be in class node and whilw create
# node object node1 above .we pass node value which s data to classs node
#linkedlist wil be created by inserting nodes.1st always when you create linkedlist ,linkedlist head node wil be empty.
#next if its not empty den lastnode wil be newnode will be added-this process when we want to add newnode at end
#insertathead--when we want to add node at head den 1st make present head node to save in temp node and then point newnode
# as head node and we make headnode next as temp .den del temp noded which s nt needed further