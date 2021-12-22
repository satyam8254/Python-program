head = None
class Node:  
      
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data = data # Assign data  
        self.next =None
  
def segregateEvenOdd():
    global head
    end = head
    prev = None 
    curr =head
    while end.next!=None:
        end=end.next
    newEnd=end
    while curr.data %2!=0 and curr!=end:
        newEnd.next=curr
        curr=curr.next
        newEnd=newEnd.next
    if curr.data%2==0:
        head=curr
        while curr!=end:
            if curr.data%2==0:
                prev=curr
                curr=curr.next
            else:
                prev.next=curr.next
                curr.next=None
                newEnd.next=curr
                newEnd=curr
                curr=prev.next
    else:
        prev=curr
    if newEnd!=end and end.data%2!=0:
        prev.next=end.next
        end.next=None
        newEnd.next=end

  
  # Implement This only "BE CAREFUL HEAD IS GLOBALLY DECLARED"
          
# Given a reference (pointer to pointer) to the head 
# of a list and an int, push a new node on the front 
# of the list.  
def push(new_data): 
    global head 
  
    # 1 & 2: Allocate the Node & 
    #         Put in the data 
    new_node = Node(new_data) 
  
    # 3. Make next of new Node as head  
    new_node.next = head 
  
    # 4. Move the head to point to new Node  
    head = new_node 
  
# Utility function to print a linked list 
def printList(): 
    global head 
    temp = head 
    while(temp != None): 
          
        print(temp.data, end = " ") 
        temp = temp.next
          
    print(" ") 
  
# Driver program to test above functions  

n = int(input())
l = list(map(int, input().split()))
l.reverse()  
for i in l:
    push(i)  
segregateEvenOdd() 
printList()