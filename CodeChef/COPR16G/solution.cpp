#include <bits/stdc++.h>

using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    long t;
    cin >> t;
    while(t--){
        long long a, b;
        cin >> a >> b;
        if(__gcd(a,b) == 1){
            cout << (a*b-a-b+1) << "\n";
        }
        else
            cout << (-1) << "\n";
    }
    return 0;
}