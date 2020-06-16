#include <bits/stdc++.h>

using namespace std;

int main(){

    long a, b, c;
    cin >> a >> b >> c;
    long mod = 1000000007;
    if(c == 1){ 
        if(a < 0) cout << ((a%mod) + mod) % mod;
        else cout << a % mod;
        } 
    else if(c == 2){
        if(b < 0) cout << ((b%mod) + mod) % mod;
        else cout << b % mod;
    }
    else{
        vector<long> result(3);
        result[0] = a;
        result[1] = b;
        result[2] = b-a;
        long ans = result[(c-1)%3];
        if(c%3 == 0 && (c/3)%2 == 0) ans = -ans;
        else if(c%3 && (c/3)%2) ans = -ans; 
        if(ans < 0) cout << ((ans%mod) + mod) % mod;
        else cout << ans%mod;
    }
    return 0;
}