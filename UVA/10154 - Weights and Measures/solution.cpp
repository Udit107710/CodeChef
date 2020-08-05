#include<bits/stdc++.h>

using namespace std; 

bool sortinrev(const pair<int,int> &a,  
               const pair<int,int> &b){
    return (a.first > b.first);
} 

int main(){
    int a, b;
    vector<pair<int, int>> arr;
    while ( scanf("%d %d", &a, &b)){
        arr.push_back(make_pair(b-a, a));
    }
    int n = arr.size();
    sort(arr.begin(), arr.end(), sortinrev);
    vector<int> dp(n+1, 0);
    int maxx = 1;
    dp[1] = arr[0].first;
    for(int i=0; i<n; ++i){
        for(int j=1; j <=i+1; ++j){
            if(dp[j-1] - arr[i].second >= dp[j] && arr[i].first >= dp[j]){
                dp[j] =  min(dp[j-1] - arr[i].second, arr[i].first);
                maxx = max(maxx, j);
            }
        }
    }
    for(auto x: dp) cout << x << " ";
    cout << endl;
    cout << maxx <<"\n";
    return 0;
}