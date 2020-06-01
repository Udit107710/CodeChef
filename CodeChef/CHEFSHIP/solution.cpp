#include <bits/stdc++.h>

using namespace std;

int main(){
    int t;
    cin >> t;
    while(t--){
        string s;
        cin >> s;
        int n = s.size();
        
        int m = 2;
        
        int ans = 0;
        for (; m < n; m+=2){
            string p = s.substr(0, m);
            string q = s.substr(m, n-1);
            if (p.compare(0, m/2, p, m/2, m) == 0 && q.compare(0, (n-m)/2, q, (n-m)/2, n-1)  == 0){
                ans += 1;
            }
        } 
        cout << ans << endl;
    }
    return 0;
}