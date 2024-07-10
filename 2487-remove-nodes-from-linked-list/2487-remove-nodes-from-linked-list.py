# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

## Nice I am getting good at leetcode
## completed 2 from pendings

def add_node(head, value):
    new_node = ListNode(value)
    if not head:
        return new_node
    current = head
    while current.next:
        current = current.next
    current.next = new_node
    return head


class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        new_head = prev
        max_val = float('-inf')
        dummy = ListNode(0)
        result_tail = dummy
        
        while new_head:
            if new_head.val >= max_val:
                max_val = new_head.val
                result_tail.next = ListNode(new_head.val)
                result_tail = result_tail.next
            new_head = new_head.next
        
        prev = None
        current = dummy.next
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        return prev
        