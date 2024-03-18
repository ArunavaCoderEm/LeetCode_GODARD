/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode *detectCycle(struct ListNode *head) {
    struct ListNode * p = head, * q = head;
    while(p != NULL && p->next != NULL){
        p = p->next->next;
        q = q->next;
        if(p == q){
            q = head;
            while(p != q){
                p = p->next;
                q = q->next;
            }
            return q;
        }
    }
    return NULL;
}

/*
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p,q = head,head
        while(p != None and p.next != None):
            p = p.next.next
            q = q.next
            if(p == q):
                q = head
                while(p != q):
                    p,q = p.next,q.next
                return q
        return None    
*/