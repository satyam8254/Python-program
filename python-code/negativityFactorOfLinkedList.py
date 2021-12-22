class Node:
    def __init__(self, key):
        self.data = key
        self.next = None


class LL:
    def __init__(self):
        self.head = None

    @staticmethod
    def insert_node(val, current):
        temp = Node(val)
        current.next = temp
        current = current.next
        return current
    
    #complete the function given below
    @staticmethod
    def Negativity(List):
        tc=0
        nc=0
        temp=List.head
        while(temp!=None):
            if temp.data<0:
                nc+=1
            tc+=1
            temp=temp.next
        return int((nc/tc)*100)
ll = LL()
num = [int(i) for i in input().split("->")]
ll.head = Node(num[0])
curr = ll.head
for i in num[1:]:
    curr = LL.insert_node(i, curr)
print(LL.Negativity(ll))