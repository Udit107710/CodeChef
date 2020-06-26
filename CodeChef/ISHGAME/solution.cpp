#include <bits/stdc++.h>

using namespace std;

int main(){
    int t;
    cin >> t;
    while(t--){
        string a, b;
        cin >> a >> b;

        for(int i=0; i < b.length(); ++i){
            a.erase(remove(a.begin(), a.end(), b[i]), a.end());
        }
        cout << a << "\n";
    }

    return 0;
}