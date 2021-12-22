# Node class 
class Node: 

	# Constructor to initialize the node object 
	def __init__(self, data): 
		self.data = data 
		self.next = None

class LinkedList:
# Function to initialize head 
    def __init__(self): 
        self.head = None

    def printList(self): 
        temp = self.head 
        while(temp): 
            print(temp.data, end=" ")
            temp = temp.next

# Do not change anything above this line
    def reorderList(self):
        # YOU ONLY NEED TO COMPLETE THIS FUNCTION.
        def reverseLL(h):
            curr=h
            prev=None
            while curr!=None:
                next=curr.next
                curr.next=prev
                prev=curr
                curr=next
            return prev
        a=self.head
        length=0
        while a:
            length+=1
            a=a.next
        mid=self.head
        for i in range(length//2):
            mid=mid.next
        b=reverseLL(mid.next)
        mid.next=None
        a=self.head
        while b:
            nextA=a.next
            a.next=b
            nextB=b.next
            b.next=nextA
            a=nextA
            b=nextB
        return self.head
# Do not change anything below this line
if __name__ == '__main__':
    
    n = int(input())

    # Start with the empty list 
    llist = LinkedList() 

    temp = [int(x) for x in input().split()]

    if(n<1):
        llist.head = None
    elif(n<2):
        llist.head = Node(temp[0])
    else:
        llist.head = Node(temp[0])
        second = Node(temp[1])
        llist.head.next = second
        curr = llist.head.next


    for i in range(2,n):
        t = Node(temp[i])
        curr.next = t
        curr = curr.next

    llist.head = llist.reorderList()
    llist.printList()