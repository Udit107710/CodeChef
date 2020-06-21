#include <bits/stdc++.h>

using namespace std;

int main(){
    int t;
    cin >> t;
    while(t--){
        int n;
        cin >> n;
        int i;
        for(i=1; i < n; ++i){
            if(i*2 > n) break;
        }
        cout << --i << "\n";
    }
    return 0;
}