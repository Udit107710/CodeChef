#include <bits/stdc++.h>

using namespace std;

long long dp[5005][5005];

long long solve(int n, int m, int k, vector<int> arr, vector<long long> sum){
    for(int i=1; i <= k; ++i){
        for(int j=(m*i); j <= n; ++j){
            dp[i][j] = max( dp[i][j-1] , dp[i-1][j-m] + (sum[j]-sum[j-m]));
        }
    }
    return dp[k][n];
}

int main(){

    int n, m, k;
    cin >> n >> m >> k;
    memset(dp, 0, sizeof(dp));

    vector<int> arr(n+1);
    vector<long long> sum(n+1, 0);
    for(int i=1; i <= n; ++i){
        cin >> arr[i];
        sum[i] = sum[i-1] + arr[i];
    }

    long long result = solve(n, m, k, arr, sum);
    cout << result;

    return 0;
}