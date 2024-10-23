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
class Solution
{
public:
    ListNode *insertBeg(ListNode *head, int value)
    {
        ListNode *newNode = new ListNode();
        newNode->val = value;
        newNode->next = head;
        return newNode;
    }

    ListNode *doubleIt(ListNode *head)
    {
        if (!head)
            return head;
        ListNode *slow = head;
        if (!head->next)
        {
            int temp = head->val * 2;
            if (temp >= 10)
            {
                head = insertBeg(head, (temp / 10));
                head->next->val = (temp % 10);
                return head;
            }
            else
            {
                head->val = temp;
                return head;
            }
        }

        ListNode *fast = head->next;
        stack<int> st;
        int carry = 0;

        ListNode *returnHead;

        bool flag = false;

        int storehead = head->val * 2;
        while (slow)
        {
            if (storehead < 10)
            {
                int store = (slow->val) * 2;
                st.push(store % 10);
                if (fast)
                {
                    carry = (fast->val * 2) / 10;
                }
                else
                {
                    carry = 0;
                }
                slow->val = st.top() + carry;
                slow = slow->next;
                if (fast)
                {
                    fast = fast->next;
                }
            }
            else
            {
                int store = (slow->val) * 2;
                if (!flag)
                {
                    st.push(store / 10);
                    flag = true;
                    returnHead = insertBeg(head, (store / 10));
                    returnHead->next = head;
                }
                st.push(store % 10);
                if (fast)
                {
                    carry = (fast->val * 2) / 10;
                }
                else
                {
                    carry = 0;
                }
                slow->val = st.top() + carry;
                slow = slow->next;
                if (fast)
                {
                    fast = fast->next;
                }
            }
        }
        if (flag)
        {
            return returnHead;
        }
        else
        {
            return head;
        }
    }
};