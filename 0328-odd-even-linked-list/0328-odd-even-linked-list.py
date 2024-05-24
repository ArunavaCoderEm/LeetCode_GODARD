# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
## I dont know why remove not working if it works then ->
# def remove(head, val):
#     if (head == val):
#         head = head.next
#         return head
#     tmp = head.next
#     tmp_prev = head
#     while (tmp.next):
#         if (tmp.val == val):
#              tmp_prev.next = tmp.next
#         tmp = tmp.next
#         tmp_prev = tmp.next
#     return head
# def append(head, new_data):
#     new_node = ListNode(new_data)
#     if (head is None):
#         head = new_node
#         return head
#     last = head
#     while (last.next):
#        last = last.next
#     last.next =  new_node
#     return head
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        idx = 1
        res = []
        temp = head
        # then ->
        # while(temp != None):
        #     if(idx % 2 == 0):
        #         x = temp.val
        #         temp = remove(temp,x)
        #         temp = append(temp,x)
        #     idx += 1
        # return head
        while(temp != None):
            res.append(temp.val)
            temp = temp.next
        res1 = []
        i = 1
        res2 = []
        while(i < len(res) + 1):
            if(i % 2 == 0):
                temp = res[i-1]
                res1.append(temp)
            else:
                res2.append(res[i-1])
            i += 1
        j = 0
        temp2 = head
        res3 = res2 + res1
        while (temp2 != None):
            temp2.val = res3[j]
            temp2 = temp2.next
            j += 1
        return head