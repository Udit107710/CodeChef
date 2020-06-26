#include<bits/stdc++.h>

using namespace std;

int main(){
    int t;
    cin >> t;
    while(t--){
        int n,b,m;
        cin >> n >> b >> m;

        int count=0;
        int prev = -1;
        for(int i=0; i < m; ++i){
            int temp;
            cin >> temp;
            if(prev == temp/b){continue;}
            else { prev = temp/b; ++count; }
        }
        cout << count << "\n";

    }

    return 0;
}