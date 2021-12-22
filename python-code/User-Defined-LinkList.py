class Node:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next  = next


# create a linked list
# insert at head
# insert at tail
# insert in b/w
# display the linked list.
# delete position x in linkedlist.
# array.. !! a = [] , ll = SinglyLinkedList()
class SinglyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    # traversal of linked list !!!
    def display(self):
        temp = self.head
        while (temp != None):
            print(temp.val, end='->')
            temp = temp.next
    
    # Insert Head ..
    def insertAtHead(self, value):
        # create a new Node
        # point the new node to head 
        # change the head.. to new Node..

        # Exit first is always good ...
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            return

        newNode.next = self.head
        self.head = newNode

        # if self.head != None:
        #     newNode.next = self.head
        #     self.head = newNode
        #     return
        
        # self.head = newNode

    def insertAtEnd(self, value):
        # without tail..
        newNode = Node(value)
        temp = self.head
        while (temp.next != None):
            temp = temp.next
        
        # temp will be at last node now.
        temp.next = newNode




linkedlist = SinglyLinkedList()

linkedlist.insertAtHead(1) # 1 -> None
linkedlist.insertAtHead(2) # 2 -> 1 -> Noe..
linkedlist.insertAtHead(3) # ...
linkedlist.insertAtHead(4) # 4 -> 3 -> 2 -> 1 -> None..

linkedlist.display() # 4->3->2->1->None..!!
print("\n")

linkedlist.insertAtEnd(5)
linkedlist.insertAtEnd(6)
linkedlist.insertAtEnd(7)

linkedlist.display() # 4->3->2->1->5->6->7->None # 4->3->2->1->5->6->7->%    




