/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

int rangeSumBST(struct TreeNode* root, int low, int high) {
    struct TreeNode *  p = root;
    int sum = 0;
    if (root == NULL)
        return 0;
        if (root->val >= low && root->val <= high){
            sum += root->val;
        }
        return sum+rangeSumBST(root->left,low,high)+rangeSumBST(root->right,low,high);
}