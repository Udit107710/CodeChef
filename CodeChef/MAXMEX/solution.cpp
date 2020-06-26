#include <bits/stdc++.h>

using namespace std;

int main(){
    int t;
    cin >> t;
    while(t--){
        int n, m;
        cin >> n >> m;
        vector<int> arr(n);
        vector<int>::reverse_iterator itr;
        for(int &x: arr) cin >> x;
        sort(arr.begin(), arr.end());
        vector<int> answer;
        int cal = 1;
        int count = 0;
        int flag = 1;

        for(itr=arr.rbegin(); itr != arr.rend(); ++itr){
            if(*itr > m) ++count;
            else if(m-*itr == cal){ ++count; ++cal;}
            else if(m-*itr == 0) continue;
            else if(*itr == *(itr-1)) ++count;
            else {flag = 0; break;};
        }
        if(flag && cal == m) cout << count << "\n";
        else cout << "-1\n";
    }

    return 0;
}