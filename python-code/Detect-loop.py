class Node:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

# Input is a linkedlist or LinkedList's head..
# Return -> boolean true or false..! 
def detect_loop_ll(head):
    # detect if there is  loop in linked list
    # Define Slow pointer and fast pointer
    slow_p = head # move slow pointer one node
    fast_p = head # move fast pointer 2 nodes..

    while(fast_p != None and slow_p != None and fast_p.next != None):
        slow_p = slow_p.next
        fast_p = fast_p.next.next

        if (slow_p == fast_p):
            return True # cycle present..
    
    return False # no cycle present..



