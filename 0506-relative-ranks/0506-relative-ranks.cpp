// LL, stack, queue, binary search, two pointers kind of done now maxheap and minheap concept must be cleared; 

class Solution
{
public:
    vector<string> findRelativeRanks(vector<int> &score)
    {

        int n = score.size();

        priority_queue<pair<int, int>> max_heap;

        for (int i = 0; i < n; ++i)
        {
            max_heap.push({score[i], i});
        }

        int rank = 1;

        map<int, string> mp;

        mp[1] = "Gold Medal";
        mp[2] = "Silver Medal";
        mp[3] = "Bronze Medal";

        vector<string> vret(score.size(), "");

        while (!max_heap.empty())
        {

            auto element = max_heap.top();
            
            int ind = element.second;

            if (rank <= 3)
            {
                vret[ind] = mp[rank];
            }
            else
            {
                vret[ind] = to_string(rank);
            }

            rank++;

            max_heap.pop();
        }

        return vret;
    }
};