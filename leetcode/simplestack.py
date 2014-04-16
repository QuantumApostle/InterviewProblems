import copy
class Node:
    def __init__(self, i):
        self.nextNode = None
        self.val = i

class Stack:
    def __init__(self):
        self.node = None
        print 'initial stack'

    def push(self, i):
        if self.node == None:
            self.node = Node(i)
        else:
            tmp = Node(i)
            tmp.nextNode = self.node
            self.node = tmp

    def pop(self):
        if self.node != None:
            returnVal = self.node.val
            self.node = self.node.nextNode
            return returnVal
        else:
            return
        
    
#class Stack:
    
if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print s.pop()
    print s.pop()
    print s.pop()
    print s.pop()
    
