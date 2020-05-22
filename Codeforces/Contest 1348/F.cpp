#include <stdio.h>
#include <iostream>
#include <string.h>
#include <map>
#include <queue>
#include <vector>
#include <algorithm>

using namespace std;

vector<vector<int>> solve(map<int, vector<int>> vect, int level, vector<vector<int>> &ans, vector<int> &temp) {
    for (int i = 0; i < vect[level].size(); ++i) {
        if (find(temp.begin(), temp.end(), vect[level][i]) != temp.end()) {
            continue;
        }
        else {
            temp.push_back(vect[level][i]);
            auto g = solve(vect, level+1, ans, temp);
            if (level == vect.size()) {
                if (temp.size() == vect.size())
                    ans.push_back(temp);
            }
            temp.pop_back();
        }
    }
    return ans;
}

int main() {
    int friends, f = 0;
    scanf("%d", &friends);
    map<int, vector<int>> vect;

    while (friends--) {
        ++f;
        int k,l;
        scanf("%d %d", &k, &l);
        for (int i = k; i <= l; ++i) {
            vect[i].push_back(f);
        }
    }
    vector<vector<int>> ans;
    vector<int> temp;
    
    ans = solve(vect, 1, ans, temp);
    
    vector<vector<int>>::iterator itr;
    vector<int>::iterator itr1;
    
    vector<vector<int>> sol;
    
    temp.assign(f, 0);

    for (itr = ans.begin(); itr < ans.end(); ++itr) {
        for (itr1 = itr->begin(); itr1 < itr->end(); ++itr1) {
            temp[*itr1-1] = (itr1 - itr->begin()) + 1;
        }
        sol.push_back(temp);
        temp.assign(f, 0);
    }

    if (sol.size() > 1) {
        cout << "No"<<endl;
        for (itr = sol.begin(); itr < (sol.begin() + 2); ++itr) {
            for (itr1 = itr->begin(); itr1 < itr->end(); ++itr1) {
                printf("%d ", *itr1);
            }
            if(itr == sol.begin())
                printf("\n");
        } 
    }
    else {
        cout << "Yes" << endl;
        for(auto v: sol){
            for (auto e : v) {
                cout << e << ' ';
            }
        }
    }
}