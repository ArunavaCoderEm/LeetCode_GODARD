# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        length = len(nums)
        if (length == 0):
            return None
        mid = length // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[0:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:length])
        return root

'''
FOR C **
 struct TreeNode * Create(int data){
    struct TreeNode * ptr = (struct TreeNode *)malloc(sizeof(struct TreeNode));
    ptr->val = data;
    ptr->left = NULL;
    ptr->right = NULL;
    return ptr;
}

int mid (int head, int tail){
    int middle = ((head+tail) / 2) + 1;
    return middle;
}

struct TreeNode * returnBST (int * nums, int head, int tail){
    if (head == tail){
        return NULL;
    }
    int middle = mid(head,tail);
    struct TreeNode * root = Create(nums[middle]);
    root->left = returnBST(nums[head],nums[middle]);
    root->right = returnBST(nums[middle + 1],nums[tail]);
    return root; 
} 

struct TreeNode* sortedArrayToBST(int* nums, int numsSize) {
    struct TreeNode * root = returnBST(nums,0,numsSize-1);
    return root;
}
'''