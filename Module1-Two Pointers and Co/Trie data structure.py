class Trienode:
    def __init__(self):
        self.children={}
        self.endofword=False

class Trie:
    def __init__(self):
        self.root=Trienode()




    def insert(self,word):
        curr=self.root
        for c in word:
            if c not in curr.children:
                curr.children[c]=Trienode()
            curr=curr.children[c]
        curr.endofword=True


    def search(self,word):
        curr=self.root

        for c in word:
            if c not in curr.children:
                return False
            curr=curr.children[c]
        return curr.endofword

    def startwith(self,prefix):
        curr=self.root
        for c  in prefix:
            if c not in curr.children:
                return False
            curr=curr.children[c]
        return True






obj=Trie()
print(obj.insert("apple"))
print(obj.search("apple"))
print(obj.startwith("app"))
print(obj.startwith("app"))
print(obj.insert("app"))
print(obj.search("app"))


#we are children as hashmap and we ahve endofword and value fr all nodes is false.insert wil insert node if nt present in hashmap
#if its dr den it wil go to next and at end curr will locat eto last letter of word and we set it to True
#in search it wil search letter by letter and end if search word ends and in tree if its not en dof word den its False
#IN start with just it will check until prefix end and if eveything is dr in tree den return TRue.no need to check end ofword

#we can hashmap to oslve this problem fr inserting and searching on o(n) but strat with prefix we cant do so we use trie ds