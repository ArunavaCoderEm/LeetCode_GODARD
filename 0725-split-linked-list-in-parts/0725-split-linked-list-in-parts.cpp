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
    vector<ListNode *> splitListToParts(ListNode *head, int k)
    {
        int N = 0;
        ListNode *temp = head;
        while (temp)
        {
            N++;
            temp = temp->next;
        }
        vector<ListNode *> v;
        if (N <= k)
        {
            ListNode *temp1 = head;
            while (k > 0)
            {
                if (temp1)
                {
                    ListNode *curr = new ListNode(temp1->val, nullptr);
                    v.push_back(curr);
                    temp1 = temp1->next;
                }
                else
                {
                    v.push_back(nullptr);
                }
                k--;
            }
        }
        else
        {
            int rem = N % k;
            int div = N / k;
            ListNode *dummyHead = head;
            if (rem == 0)
            {
                while (k > 0)
                {
                    ListNode *temp2 = dummyHead;

                    int count = div;

                    while (count > 1)
                    {
                        temp2 = temp2->next;
                        count--;
                    }
                    if (temp2 && temp2->next)
                    {
                        v.push_back(dummyHead);
                        dummyHead = temp2->next;
                        temp2->next = nullptr;
                    }
                    else
                    {
                        v.push_back(dummyHead);
                        dummyHead = nullptr;
                    }
                    k--;
                }
            }
            else
            {
                int orrem = rem;
                while (orrem > 0)
                {
                    ListNode *temp2 = dummyHead;

                    int count = div;
                    while (count > 0)
                    {
                        temp2 = temp2->next;
                        count--;
                    }
                    if (temp2 && temp2->next)
                    {
                        v.push_back(dummyHead);
                        dummyHead = temp2->next;
                        temp2->next = nullptr;
                    }
                    else
                    {
                        v.push_back(dummyHead);
                        dummyHead = nullptr;
                    }
                    orrem--;
                }
                int rest = k - rem;
                while (rest > 0)
                {

                    ListNode *temp2 = dummyHead;
                    int count = div;

                    while (count > 1)
                    {
                        temp2 = temp2->next;
                        count--;
                    }
                    if (temp2 && temp2->next)
                    { 
                        v.push_back(dummyHead);
                        dummyHead = temp2->next;
                        temp2->next = nullptr; 
                    }
                    else
                    {
                        v.push_back(dummyHead);
                        dummyHead = nullptr; 
                    }
                    rest--;
                }
            }
        }
        return v;
    }
};