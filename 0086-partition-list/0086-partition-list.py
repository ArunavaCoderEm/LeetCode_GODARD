# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        smaller_than_x_head = ListNode(0)
        greater_than_x_head = ListNode(0)
        small_x = smaller_than_x_head
        great_x = greater_than_x_head


        temp = head

        while (temp != None):

            if (temp.val < x):
                small_x.next = ListNode(temp.val)
                small_x = small_x.next
            else:
                great_x.next = ListNode(temp.val)
                great_x = great_x.next

            temp = temp.next

        small_x.next = greater_than_x_head.next

        return smaller_than_x_head.next