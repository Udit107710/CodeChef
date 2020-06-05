#include <bits/stdc++.h>

using namespace std;

int main(){
    int t;
    cin >> t;
    while(t--){
        int n, k;
        cin >> n >> k;
        int loss=0;
        for(int i=0; i < n; ++i){
            int p;
            cin >> p;
            if(p > k)
                loss+=(p-k);
        }
        cout << loss << "\n";
    }

    return 0;
}