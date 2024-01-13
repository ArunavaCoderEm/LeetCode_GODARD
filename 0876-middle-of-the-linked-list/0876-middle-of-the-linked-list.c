/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


// EZZ SOLUTION THANKS HACKERRANK
struct ListNode* middleNode(struct ListNode* head) {
    struct ListNode * p = head;
    struct ListNode * q = head;
    while (p != NULL && p->next != NULL){
        p = p->next->next;
        q = q->next;
    }
    return q;
}