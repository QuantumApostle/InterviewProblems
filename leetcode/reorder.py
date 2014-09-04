class ListNode:
        def __init__(self, x):
                self.val = x
                self.next = None

def reorder_list(head):
        if head == None:
                return
        elif head.next == None:
                return

        fakeHead = ListNode(0)
        fakeHead.next = head
        values_list = [head.val]
        while head.next is not None:
                values_list.append(head.next.val)
                head = head.next
        values_list.reverse()
        if len(values_list) < 3:
                return
        head = fakeHead.next
        if len(values_list)%2 == 0:
                list_size = len(values_list)/2 - 1
        else:
                list_size = len(values_list)/2
        
        
        for i in range(list_size):
                midNode = ListNode(values_list[i])
                midNode.next = head.next
                head.next = midNode
                head = head.next.next
        if len(values_list)%2 == 0:
                head.next.next = None
        else:
                head.next = None
        

        head = fakeHead.next

def print_list(head):
        while head is not None:
                print head.val
                head = head.next
        

if __name__ == "__main__":
        node0 = ListNode(0)
        node1 = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        node4 = ListNode(4)
        '''
        node5 = ListNode(5)
        node6 = ListNode(6)
        '''

        node0.next = node1
        node1.next = node2
        node2.next = node3
        node3.next = node4
        '''
        node4.next = node5
        node5.next = node6
        '''
        #print_list(node0)
        reorder_list(node0)
        print_list(node0)
        
	
