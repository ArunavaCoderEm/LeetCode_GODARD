/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

// // I liteerally got 5 Wrong answers coz I wrote INT_MAX and INT_MIN instead of LONG 

bool checkforme(struct TreeNode* root, long minimum, long maximum){
    if(root == NULL) return true;
    if(root->val <= minimum || root->val >= maximum) return false;
    return (checkforme(root->left, minimum, root->val) && checkforme(root->right, root->val, maximum));
}
bool isValidBST(struct TreeNode* root) {
    if(root == NULL) return true;
    return checkforme(root, LONG_MIN, LONG_MAX);
}