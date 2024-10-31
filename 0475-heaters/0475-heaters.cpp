// this less beatsss whattttt 40mins for 12% ?????

class Solution {

private:
    bool canHeat(vector<int> heaters, vector<int>houses, int mid) {
        int n = houses.size();
        int i = 0, k = 0;
        int heatRange = heaters.size();

        while (i < n) {
            if (houses[i] < heaters[k] - mid) {
                return false;
            }
            if (houses[i] > heaters[k] + mid) {
                k++;
                if (k == heatRange){
                    return false;
                }
            } else {
                i++;
            }
        }
        return true;
    }

public:
    int findRadius(vector<int>& houses, vector<int>& heaters) {
        sort(houses.begin(), houses.end());
        sort(heaters.begin(), heaters.end());

        int start = 0, end = INT_MAX;

        while (start <= end) {
            int mid = (start + (end - start) / 2);
            if (canHeat(heaters, houses, mid)) {
                end = mid - 1;
            } else {
                start = mid + 1;
            }
        }

        return start;

    }
};