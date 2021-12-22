

# Input -> head of a linked list
# output -> head of the reversed linked list..
def reverse_ll(head):
    # reverse the linked list
    # define prev and curr..
    prev = None
    curr = head

    # 1(p) -> 2(c)  3 -> 4 -> None..

    while(curr != None):
        temp = curr.next # temp(3)
        curr.next = prev # lost the next here... 2 -> 1

        # moving forward..
        prev = curr #  move prev to one step ahead
        curr = temp # move curr to one step ahead..

    return prev