# Defining Node Class
class Node:
    def __init__(self, data = None, nextNode = None):
        self.data = data # Stores int values..
        self.nextNode = nextNode # Stores Node objects

# 


node1 = Node(1, None) # 1 -> None
head = node1
node2 = Node(2, None) # 2 -> None
node3 = Node(3, None) # 3 -> None
node4 = Node(4, None) # 4 -> None
node5 = Node(5, None)


node1.nextNode = node2 # 1 -> 2 -> None
node2.nextNode = node3 # 1 -> 2 -> 3 -> None
node3.nextNode = node4 # 1 -> 2 -> 3 -> 4 -> None

# Linked List I have a linkedlist -> Head pointer or Head Variable.. => head variable
# I have an array ? => arr = [1, 2, 3, 4] => a[3]

# Singly Linked list..!!

# node1.nextNode.nextNode # 3.
# node3.nextNode # 4
# node4.nextNode # None.!!
# node4 #

# Head..!
 # 3
 # head = 3
 # head2 = 3

# 1 -> 2 -> 3 -> 4 -> None
temp = head
while (temp != None):
    print(temp.data, end='->')
    temp = temp.nextNode

node1 # ? None.. 

# 1 , 2 , 3 , 4 ,

