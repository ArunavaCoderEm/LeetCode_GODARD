/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

 // Copied from my GH \U0001fae0
struct TreeNode* removeLeafNodes(struct TreeNode* root, int target) {
        if(root == NULL) return root;
        root->left = removeLeafNodes(root->left,target);
        root->right = removeLeafNodes(root->right,target);
        if(root->left == NULL && root->right == NULL && root->val == target){
            free(root);
            return NULL;
        }
        return root;    
}