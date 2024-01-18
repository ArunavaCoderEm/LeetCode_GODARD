/**
 * Definition for singly-linked list.
 * struct ListListNode {
 *     int val;
 *     struct ListListNode *next;
 * };
 */
// Easiest Concept with two pointers
struct ListNode * deleteMiddle(struct ListNode* head) {
    if (head == NULL || head->next == NULL){
        return NULL;
    }
    struct ListNode * fast = head, * slow = head, * prev = NULL;
    while(fast != NULL && fast->next != NULL){
        fast = fast->next->next;
        prev = slow;
        slow = slow->next;
        if (slow == fast){
            break;
        }
    }
    prev->next = slow->next;
    free(slow);
    return head;
}