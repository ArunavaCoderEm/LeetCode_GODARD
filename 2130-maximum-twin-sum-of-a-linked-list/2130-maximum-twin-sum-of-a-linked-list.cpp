/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    int pairSum(ListNode* head) {
        vector <int> v;
        ListNode * temp = head;
        int j = -1;

        while (temp) {
            v.push_back(temp->val);
            temp = temp->next;
            j++;
        }

        int i = 0, maxSum = INT_MIN;

        while (i < j) {
            int currSum = v[i] + v[j];
            maxSum = max(maxSum, currSum);
            i++; j--; 
        }

        return maxSum;

    }
};