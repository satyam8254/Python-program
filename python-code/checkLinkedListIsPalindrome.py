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
          
    def isPalin(self):
        #####WRITE CODE HERE####
        temp=self.head
        arr=[]
        flag=True
        while temp!=None:
            arr.append(temp.data)
            temp=temp.next
        while self.head!=None:
            i=arr.pop()
            if self.head.data==i:
                flag=True
            else:
                flag= False
                
            self.head=self.head.next
        return flag

        

def read_list_input():
    vals = input().split(' ')
    linkedList = LinkedList() 
    for val in vals:
        linkedList.push(val)
    return linkedList

test_cases = int(input())
for i in range(test_cases):
    linkedList = read_list_input()
    print(linkedList.isPalin())