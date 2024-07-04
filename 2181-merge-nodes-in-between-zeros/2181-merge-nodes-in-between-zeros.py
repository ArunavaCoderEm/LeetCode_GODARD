# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

## I don't know after a lot of wrong answers !!!! still ...

class Solution:
    def mergeNodes(self, head: ListNode) -> ListNode:
        if(not head or not head.next): return head
        res = []
        ans = []
        temp = head
        while(temp != None):
            res.append(temp.val)
            temp = temp.next
        z = res.count(0)
        s = 0
        st = 0
        en = st + 1
        ans = []
        for i in range(z-1):
            while(res[en] != 0):
                s += res[en]
                en += 1
            st = en
            en = st + 1
            ans.append(s)
            s = 0
        if not ans:
            return None
        headret = ListNode(ans[0])
        current = headret
        for value in ans[1:]:
            new_node = ListNode(value)
            current.next = new_node
            current = current.next
        return headret