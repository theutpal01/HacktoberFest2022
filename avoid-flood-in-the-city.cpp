class Solution {
public:
    vector<int> avoidFlood(vector<int>& rains) {
        vector<int> ans; // Store the final answer here.
        int n = rains.size(); 
        unordered_map<int, int> fulllakes; // Lake number -> day on which it became full.
        set<int> drydays;     // Set of available days that can be used for drying a full lake.
        for (int i=0; i<n; i++) {  // For each day - 
            if (rains[i] == 0) {  // No rain on this day.
                drydays.insert(i); // This day can be used as a day to dry some lake.
                                   // We don't know which lake to prioritize for drying yet.
                ans.push_back(1);  // Any number would be ok. This will get overwritten eventually.
                                   // If it doesn't get overwritten, its totally ok to dry a lake
                                   // irrespective of whether it is full or empty.
            } else { // Rained in rains[i]-th lake.
                int lake = rains[i]; 
                if (fulllakes.find(lake) != fulllakes.end()) { // If it is already full -
                    // We must dry this lake before it rains in this lake.
                    // So find a day in "drydays" to dry this lake. Obviously, that day must be
                    // a day that is after the day on which the lake was full.
                    // i.e. if the lake got full on 7th day, we must find a dry day that is 
                    // greater than 7.
                    auto it = drydays.lower_bound(fulllakes[lake]);
                    if (it == drydays.end()) { // If there is no available dry day to dry the lake,
                                               // flooding is inevitable.
                        return {}; // Sorry, couldn't stop flooding.
                    }
                    int dryday = *it; // Great, we found a day which we can use to dry this lake.
                    ans[dryday] = lake; // Overwrite the "1" and dry "lake"-th lake instead.
                    drydays.erase(dryday); // We dried "lake"-th lake on "dryday", and we can't use
                                           // the same day to dry any other lake, so remove the day
                                           // from the set of available drydays.
                }
                fulllakes[lake] = i; // Update that the "lake" became full on "i"-th day.
                ans.push_back(-1); // As the problem statement expects.
            }
        }
        return ans; // Congratualtions, you avoided flooding.
    }
