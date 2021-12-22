class Node: 
    def __init__(self, value): 
        self.data = value 
        self.next = None
        
class LinkedList: 
  
    def __init__(self): 
        self.head = None
  
    def push(self, new_value): 
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node
          
    def makeListAndPrint(self):
        #####WRITE CODE HERE####
        ll=LinkedList()
        ll.head=None
        ll.tail=None
        temp=self.head
        while temp!=None:
            if int(temp.next.data)==0:
                currentLL=ll.head
                ll.head=Node(int(temp.data))
                if currentLL is None:
                    ll.tail=ll.head
                ll.head.next=currentLL
            else:
                ll.push(int(temp.data))
            temp=temp.next.next
        p=ll.head
        while p!=None:
            print(p.data,end=" ")
            p=p.next

        return
            
        

def read_list_input():
    vals = input().split(' ')
    linkedList = LinkedList() 
    for val in vals:
        linkedList.push(val)
    return linkedList

test_cases = int(input())
for i in range(test_cases):
    linkedList = read_list_input()
    linkedList.makeListAndPrint()