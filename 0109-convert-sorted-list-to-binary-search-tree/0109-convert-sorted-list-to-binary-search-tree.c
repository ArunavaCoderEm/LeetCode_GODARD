/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

// LITERALLY TOOK MY SOUL ... 'C' IS THE WORST LANGUAGE 

struct TreeNode * Create(int data){
    struct TreeNode * ptr = (struct TreeNode *)malloc(sizeof(struct TreeNode));
    ptr->val = data;
    ptr->left = NULL;
    ptr->right = NULL;
    return ptr;
}

struct ListNode * mid (struct ListNode * head, struct ListNode * tail){
    struct ListNode * fast = head, * slow = head;
    while (fast != tail && fast->next != tail){
        fast = fast->next->next;
        slow = slow->next;
    }
    return slow;
}

struct TreeNode * returnBST (struct ListNode * head,struct ListNode * tail){
    if (head == tail){
        return NULL;
    }
    struct ListNode * middle = mid(head,tail);
    struct TreeNode * root = Create(middle->val);
    root->left = returnBST(head,middle);
    root->right = returnBST(middle->next,tail);
    return root; 
} 

struct TreeNode* sortedListToBST(struct ListNode* head) {
       struct TreeNode * root = returnBST(head,NULL);
        return root;

}