class stack:
    def __init__(self):
        self.stack=[]

    def is_empty(self):
        return len(self.stack)==0

    def push(self,value):
        return self.stack.append(value)

    def size(self):
        return len(self.stack)

    def top(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()
# class queue():
#     def __init__(self):
#         self.stack1=[]
#         self.stack2=[]
#
#     def push(self,x):
#         while not self.stack1 is_empty():
#             self.stack2.append(self.stack1.pop())
#
#         self.stack1.append(x)
#
#         while not self.stack2 is _empty():
#             self.stack1.append(self.stack2.pop())
#
#      def pop():
#          return self.satck1.pop()
#      def peek():
#          retrun stack1.top()
#
#       def empty(self):
#           retrun self.stack1.is_empty()


    #  so create queue we need 2 stacks.ex 1,2,3,4
    # 1st add 1 to stack1 and den when 2 comes 1st move all stack1 to tsack 2 to keep fifo quality of queue
    # next add 2 to stack1,den 3 comes move stack1 to stack2 and put new elemnt in stack1
    # den at last move all elemnts frrom stack2 to stack one to keep fifo polity

    # space n time complexity -push-it will be 2 stacks so 2n so o(n)-
    # pop,peek,empty wil be o(1)
