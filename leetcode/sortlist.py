import copy
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def move(head, steps):
    while steps != 0:
        head = head.next
        steps -= 1
    return head

def sort(head, length):
    
    if length == 1:

        fakeHead = ListNode(head.val)
        fakeHead.next = None
        return fakeHead
    left = head
    right = head


    left = sort(left, length / 2)
    mid = move(right, length / 2)

    right = sort(mid, length - length / 2)
    return merge(left, right)
    
def merge(left, right):
    fakeHead1 = ListNode(0)
    fakeHead2 = ListNode(0)
    fakeHead1.next = fakeHead2
    
    while left != None or right != None:
        if left == None:
            fakeHead2.next = right
            break
        if right == None:
            fakeHead2.next = left
            break
        if left.val < right.val:
            fakeHead2.next = left
            fakeHead2 = fakeHead2.next
            left = left.next
        else:
            fakeHead2.next = right
            fakeHead2 = fakeHead2.next
            right = right.next

            
    return fakeHead1.next.next

def printResult(head):
	while head != None:
		print head.val,
		head = head.next	

if __name__ == "__main__":
    n1 = ListNode(6)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(1)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    
    printResult(sort(n1, 5))
  
	
