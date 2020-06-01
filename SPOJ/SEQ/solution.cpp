#include <bits/stdc++.h>

using namespace std;
const long long MOD = 1000000000;

vector<vector<long long>> mul(vector<vector<long long>> A, vector<vector<long long>> B, int k)
{
    vector<vector<long long>> ans(k, vector<long long>(k, 0));
    for(int i=0; i < k; ++i)
        for(int j=0; j < k; ++j)
            for(int l=0; l < k; ++l){
                ans[i][j] = (ans[i][j] + (A[i][l] * B[l][j])) % MOD;
                ans[i][j] %= MOD;
            }
    return ans;
}

vector<vector<long long>> pow(vector<vector<long long>> A, int p, int k)
{
    // cout << p << " ";
    if (p == 1)
        return A;
    if (p % 2)
        return mul(A, pow(A, p-1, k), k);
    vector<vector<long long>> X = pow(A, p/2, k);
    return mul(X, X, k);
}

int main(){
    int t;
    cin >> t;
    while (t--){
        int k;
        cin >> k;

        vector<long long> F1(k);
        vector<long long> C(k);
        vector<vector<long long>> matrix(k, vector<long long>(k, 0));
        
        for(long long &x: F1) cin >> x;
        for(long long &x: C) cin >> x;
        
        long long n;
        cin >> n;

        if (n <= k){
            cout << F1[n-1] << endl;
            continue;
        }

        for(int i=0; i < k-1; ++i)
            matrix[i][i+1] = 1;
        
        reverse(C.begin(), C.end());
        matrix[k-1] = C;
        matrix = pow(matrix, n-k, k);

        long long res = 0;
        for(int i=0; i < k; ++i)
            res = (res + matrix[k-1][i] * F1[i]) % MOD;
        cout << res % MOD << endl;
    }
    return 0;
}