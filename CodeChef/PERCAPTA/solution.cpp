#include<bits/stdc++.h>

using namespace std;

int main(){
    int t;
    cin >> t;
    while(t--){
        int n, m;
        cin >> n, m;
        vector<int> A(n), B(n);
        map<int, vector<int>> path;
        multiset<pair<double, int>> pc;
        multiset<pair<double, int>>::reverse_iterator itr;
        for(int &x: A) cin >> x;
        for(int &x: B) cin >> x;
        for(int i=0; i < m; ++i){
            int x,y;
            cin >> x >> y;
            path[x].push_back(y);
            path[y].push_back(x);
        }
        for(int i=0; i < n; ++i){
            pc.insert(make_pair(A[i]/B[i], i+1));
        }
        vector<int> result;
        if(m == (n*(n-1)/2)){
            for(itr=pc.rbegin(); itr != pc.rend(); ++itr){
                result.push_back(itr->second);
                if(itr->first > (itr+1)->first) break;
            }
            cout << result.size() << "\n";
            for(int x: result) cout << x << " ";
            cout << "\n";
            continue;
        }


    }

    return 0;
}