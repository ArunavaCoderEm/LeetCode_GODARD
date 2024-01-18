/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
// AFTER 10000 TRIES I GUESS \U0001fae0
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    long long int sum1 = 0;
    struct ListNode * p = l1, *q = l2;
    struct ListNode * returnL = NULL;
    struct ListNode * check = NULL;
    while (p != NULL || q != NULL || sum1 != 0){
        if (p != NULL){
            sum1 = sum1 + p->val;
            p = p->next;
        }
        if(q != NULL){
            sum1 = sum1 + q->val;
            q = q->next;
        }
        struct ListNode * ptr = (struct ListNode*)malloc(sizeof(struct ListNode));
        int rem = sum1 % 10;
        ptr->val = rem;
        sum1 = sum1 / 10;
        if (returnL != NULL){
            check->next = ptr;
            check = ptr;
        }
        else {
            returnL = ptr;
            check = ptr;
        }
    }
    check->next = NULL;
    return returnL;
}