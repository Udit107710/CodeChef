#include <bits/stdc++.h>

using namespace std;

int main(){
    int t;
    cin >> t;
    while(t--){
        string s;
        cin >> s;
        if(s.size() == 1){
            cout << "0\n";
            continue;
        }
        int pair=0;
        for(int i=0; i+1 < s.size(); ++i){
            if(s[i] != s[i+1]){
                ++pair;
                ++i;
            }
        }
        cout << pair << "\n";
    }
    return 0;
}