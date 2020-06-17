#include <bits/stdc++.h>

using namespace std;

void solve(vector<long> arr, vector<long> &dp, long n){

    dp[n-1] = 0;
    for(long i=n-2; i >= 0; --i){
        long steps = 100000000;
        for(int j=1; j <= arr[i] && i+j < n; ++j){
             if((1 + dp[i+j]) < steps) steps= 1+dp[i+j];
        }
        dp[i] = steps;
    }
}

int main(){
    int t;
    cin >> t;
    while(t--){
        long n;
        cin >> n;
        vector<long> arr(n);
        vector<long> dp(n, -1);
        for(int i=0; i<n; ++i) cin >> arr[i];
        solve(arr, dp, n);
        if(dp[0] == 100000000) cout << "-1\n";
        else cout << dp[0] << "\n";
    }
    return 0;
}