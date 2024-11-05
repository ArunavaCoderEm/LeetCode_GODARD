// sorting is for noobs !! (also me still !)

class Solution {
public:
    int matchPlayersAndTrainers(vector<int>& players, vector<int>& trainers) {

        priority_queue <int> PQ;
        priority_queue <int> TQ;
        int count = 0;

        for (int i: players) {
            PQ.push(i);
        }
        
        for (int j: trainers) {
            TQ.push(j);
        }

        while (! PQ.empty() && ! TQ.empty()) {

            if (PQ.top() > TQ.top()) PQ.pop();

            else if (PQ.top() <= TQ.top()) {
                count++;
                PQ.pop();
                TQ.pop();
            }

        }

        return count;

    }
};