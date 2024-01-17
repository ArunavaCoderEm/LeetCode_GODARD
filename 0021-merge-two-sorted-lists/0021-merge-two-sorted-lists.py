# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def appendll(head_ref, new_data):
    new_node = ListNode(new_data)
    last = head_ref
    new_node.next = None
    if head_ref is None:
        return new_node
    while last.next is not None:
        last = last.next
    last.next = new_node 
    return head_ref

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        l1,l2 = [],[]
        if (list1 == None):
            return list2
        elif(list2 == None):
            return list1
        while (list1 != None):
            l1.append(list1.val)
            list1 = list1.next
        while (list2 != None):
            l2.append(list2.val)
            list2 = list2.next
        l3 = l1+l2
        l3.sort()
        head = ListNode()
        head.val = l3[0]
        head.next = None
        for i in range(1,len(l3)):
            head = appendll(head,l3[i])
        return head
