class Node:
    def __init__(self, nodeValue):
        self.data = nodeValue
        self.next = None

#do not change anything above This
def removeZreo(n):
    if n!=None and n.data==0:
        return removeZreo(n.next)
    else:
        return n 
def Compare(list1 ,list2):
    #compelete the code
    list1=removeZreo(list1)
    list2=removeZreo(list2)
    l1=list1
    l2=list2
    lc1=0
    lc2=0
    while l1:
        lc1+=1
        l1=l1.next
    
    while l2:
        lc2+=1
        l2=l2.next
    
    size1=lc1
    size2=lc2
    if size1>size2:
        return 1
    elif size2>size1:
        return -1
    while list1!=None and list2!=None:
        if list1.data>list2.data:
            return 1
        elif list1.data<list2.data:
            return -1
        list1=list1.next
        list2=list2.next
    return 0

#do not change anything below this



def buildListFromArray(givenArray):

    numElements = len(givenArray)
    if numElements == 0:
        return None
    head = Node(givenArray[0])
    prevNode = head
    for index in range(1, numElements):
        newNode = Node(givenArray[index])
        prevNode.next = newNode
        prevNode = newNode
    return head

if __name__ == '__main__':

    numTest = int(input())

    for i in range(numTest):

        n, m = map(int, input().split())

        arr1 = list(map(int, input().split()))
        arr2 = list(map(int, input().split()))

        head1, head2 = buildListFromArray(arr1), buildListFromArray(arr2)


        flag = Compare(head1, head2)

        print(flag)