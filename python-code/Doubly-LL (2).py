# single node for DLL
class Node:
    def __init__(self, data = None, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev


# var1 = Node(0) =>  None <- 0 -> none
# var2 = None..!! => None!!

# var3 = var1.next => var3.next ..??



class DLL:

    def __init__(self):
        self.head = None
        self.tail = None
    
    def forwardTraversal(self):
        temp = self.head
        while (temp != None):
            print(temp.data, end="<->")
            temp = temp.next
        print("\n") # just for new Line..
    
    def backTraversal(self):
        temp = self.tail
        while (temp != None):
            print(temp.data, end="<->")
            temp = temp.prev
        print("\n")  

    def append(self, val): # Insersion at end..
        newNode = Node(val)
        # exit first code..
        if self.head is None:
            self.head = newNode
            self.tail = self.head # when only one node tail and head are same..
            return
        
        # if head not none you traverse unitl tail or if you have tail already you 
        # just point the 
        self.tail.next = newNode # 1 -> 2
        newNode.prev = self.tail # 1 <-> 2 -> None
        # None is Null.. so it is not a object.. so it wont have prev and next Nodes..!!!

        # change the tail..
        self.tail = newNode
    
    def insertionAtHead(self, val):
        newNode = Node(val)

        if self.head is None:
            self.head = newNode
            self.tail = self.head # when only one node tail and head are same..
            return
        
        # None <- 1 -> None
        newNode.next = self.head # 2 -> 1 -> None
        self.head.prev = newNode # 2 -> <- 1

        self.head = newNode # 2..is the head now..

    # We assume our first node position is 1
    # 
    def insertAfterPositionX(self, x, val):
        if x < 0: # (-1, -2 , -3....)
            # invalid position..
            return
        newNode = Node(val)
        if x == 0:
            # Adding at head..
            newNode.next = self.head # f -> a -> b -> c -> d-> e ->
            self.head.prev = newNode # f <-> a <-> b <-> c <-> d <-> e ->
            self.head = newNode # 
            return
        # x 5...
        temp = self.head
        temp_p = 1
        while (temp_p < x and temp != None):
            temp = temp.next
            temp_p += 1
        
        if temp is None:
            # Invalid position x is greater than linked lenght..
            return

        # Now temp is at e -> None , f - newNode..
        # e - temp, None - d_node, f - newNode
        # a -> b -> c -> d-> e ->
        d_node = temp.next
        # new nodes pointerss..
        newNode.next =  d_node # f.next = (c.next)d
        if d_node != None: # this case is last Node case..
            d_node.prev = newNode # d.prev = f
        newNode.prev = temp # f.prev = c
        temp.next = newNode # c.next = f

    # a -> b -> c -> d-> e ->, f...
    # move the temp variable xth positon => 3
    # x, temp_p, temp
    # 3, 1 , a - intial
    # (1 <= 3)
        # 3, 2, b - Iter 1
    # (2 <= 3)
        # 3, 3, c - Iter 2
    # (3 <= 3)
        # 3, 4, d - Iter 3..
    # (4 <= 3)
        # while breaks....

     # We assume our first node position 1..
     # a <-> b(h) -> c -> d-> e ->, f...
    def deletePositionX(self, x):
        if x <= 0:
            # invalid position
            return
        
        if x == 1:
            # deleting head..
            temp = self.head # so that we can free the space..

            self.head = self.head.next # <- b <-> c <-> d <-> e <-> f...
            self.head.prev = None 
            del(temp) # freeing up the space.. # test without assiging to None..
        
        # if any other position..
        # move temp to x-1 th position..

        temp = self.head
        temp_p = 1
        
        # a(h) <-> b(temp) -> c(del) -> d-> e -> f...
        while (temp_p < (x-1) and temp != None):
            temp_p += 1
            temp = temp.next
    
        
        if temp is None:
            # invalid position.. x value is greater than ll length..
            return
        
        # x 7
        # a <-> b -> c -> d-> e -> f -> None..
        delNode = temp.next #...
        if delNode is None:
            return
        
        # Handling tail case..
        if delNode.next is not None:
            delNode.next.prev = temp # b <- d # temp.next.next.prev = temp

        temp.next = delNode.next # = temp.next.next.. b -> d

        del(delNode)

        # 1(h1) -> 2  5(h2) -> 4 -> 3 

        # 1 -> 5 -> 2 -> 4 -> 3...

        # 1  2-> 
        # 5  4(temp2) -> 3

        # 1 -> 5 -> 2 -> 4


            
        
# Merging two sorted linked..

        

        








dll = DLL()
dll.append(1)
dll.append(2)
dll.append(3)
dll.append(4)
dll.append(5)
dll.append(6)

# dll.forwardTraversal() # 1 <-> 2 <-> 3 <-> 4 <-> 5 <-> 6 <->
# dll.backTraversal() # 6 <-> 5 <-> 4 <-> 3 <-> 2 <-> 1 <->

dll.insertAfterPositionX(1,'7')
dll.forwardTraversal() # 1 <-> 7 <-> 2 <-> 3 <-> 4 <-> 5 <-> 6 <->

dll.insertAfterPositionX(3,'8')
dll.forwardTraversal() # 1 <-> 7 <-> 2 <-> 8 <-> 3 <-> 4 <-> 5 <-> 6 <->

dll.insertAfterPositionX(8,'9')
dll.forwardTraversal() # 
        

        

        


