#include<bits/stdc++.h>

using namespace std;

int compute(int *dp, int high[], int low[], int p, int n){
    if(p < 0) return 0;
    if(dp[p] > 0) return dp[p];
    dp[p] = max(high[p] + compute(dp, high, low, p-2, n), low[p] + compute(dp, high, low, p-1, n));
    return dp[p];
}


int main(){
    int t;
    cin >> t;
    
    while(t--){
        int n;
        cin >> n;
        int high[n], low[n];
        int dp[n] = {0};
        for(int i=0; i<n; i++) cin >> high[i];
        for(int i=0; i<n; ++i) cin >> low[i];

        cout << compute(dp, high,low, n-1, n) << "\n";
    }

    return 0;
}