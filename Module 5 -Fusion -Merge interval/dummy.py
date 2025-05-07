def mergedlist(list1,list2):
    dummy=node=Node(None)
    while list1 and list2:
        if list1.data<list2.data:
            node.next=list1
            list1=list1.next
        else:
            node.next=list2
            list2=list2.next

        node=node.next

    node.next=list1 or list2

    return dummy.next










node1=Node(1)
node2=Node(3)
node3=Node(4)
firstlist=LinkedList()
firstlist.insertatend(node1)
firstlist.insertatend(node2)
firstlist.insertatend(node3)


node4=Node(2)
node5=Node(7)
node6=Node(9)
secondlist=LinkedList()
secondlist.insertatend(node4)
secondlist.insertatend(node5)
secondlist.insertatend(node6)
print("firstlist are")
firstlist.printlist()
print("secondlist are")
secondlist.printlist()
merge=LinkedList()
merge.head=mergedlist(firstlist.head,secondlist.head)
print("after merging")
merge.printlist()
