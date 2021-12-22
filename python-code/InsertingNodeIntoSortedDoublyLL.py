#!/bin/python3

import math
import os
import random
import re
import sys

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

#
# Complete the 'sortedInsert' function below.
#
# The function is expected to return an INTEGER_DOUBLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_DOUBLY_LINKED_LIST llist
#  2. INTEGER data
#

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#

def sortedInsert(llist, data):
    # Write your code here
    newNode=DoublyLinkedListNode(data)
    temp=llist
    if data<temp.data:
        newNode.next=temp
        newNode.prev=None
        temp.prev=newNode
        return newNode
    while temp.data<=data and temp.next!=None and temp.next.data<=data:
        temp=temp.next
    newNode.prev=temp
    newNode.next=temp.next
    temp.next=newNode
    if newNode.next!=None:
        newNode.next.prev=newNode
    return llist



if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        llist_count = int(input())

        llist = DoublyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        data = int(input())

        llist1 = sortedInsert(llist.head, data)

    #     print_doubly_linked_list(llist1)
    #     #fptr.write('\n')

    # #fptr.close()























    # temp=llist
    # if data<=temp.data:
    #     p=DoublyLinkedListNode(data)
    #     p.next=temp
    #     temp.prev=p
    #     return p
    # while temp.next!=None:
    #     if temp.data>=data:
    #         p=DoublyLinkedListNode(data)
    #         p.next=temp.next
    #         p.prev=temp
    #         temp.next=p
    #         p.next.prev=p
    #         return llist
    #     temp=temp.next
    # p=DoublyLinkedListNode(data)
    # temp.next=p
    # p.prev=temp
    # return llist






    # cur=llist
    # node=DoublyLinkedListNode(data)
    # if cur.data>data or cur.data==data:
    #     node.next=cur
    #     cur.prev=node
    #     llist=node
    #     return llist
    # while cur.next:
    #     if (cur.data<data and cur.next.data>data) or cur.data==data:
    #         node.next=cur.next
    #         cur.next.prev=node
    #         node.prev=cur
    #         cur.next=node
    #         return llist
    #     cur=cur.next
    # if cur.data<data or cur.data==data:
    #     node.prev=cur
    #     cur.next=node
    #     return llist





















