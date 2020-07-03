#include<bits/stdc++.h>

using namespace std;

int main(){
    int a, b, i=1;
    vector<pair<pair<int, int>, int>> sset;
    while(scanf("%d %d", &a, &b) != EOF ){
        sset.emplace_back(make_pair(make_pair(a, b), i));
        ++i;
    }
    sort(sset.begin(), sset.end());
    vector<pair<int, int>> ans(i-1 , make_pair(1, -1));
    int maxx = 1;
    int last = 0;

    for(int j=1; j<i-1; ++j){
        for(int  k=0; k<j; ++k){
            if((sset[j].first.second < sset[k].first.second) && (ans[j].first < (1 + ans[k].first))){
                ans[j].first = ans[k].first + 1;
                ans[j].second = k;
                if(ans[j].first > maxx){
                    maxx = ans[j].first;
                    last = j;
                }
            }
        }
    }
    printf("%d\n", maxx);
    vector<int> answer(maxx); i=maxx-1;
    while(i >= 0){
        answer[i] = sset[last].second;
        --i;
        last = ans[last].second;
    }
    for(int x: answer) cout << x << "\n";

    return 0;
}