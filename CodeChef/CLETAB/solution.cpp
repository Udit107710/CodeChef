#include <bits/stdc++.h>

using namespace std;

int main(){
    int t;
    cin >> t;
    while(t--){
        int n,m;
        cin >> n >> m;
        
        vector<int> orders(m);

        for(int i=0; i < m; ++i) cin >> orders[i];
        
        if(n >= m){
            set<int> s(orders.begin(), orders.end());
            cout << s.size() <<"\n";
            continue; 
        }
        
        int p=0;
        int count=0;
        vector<int> tables(n, -1);
        
        while(p+n <= m){
            int common=0;
            vector<int> temp;
            for(int i=0; i < n; ++i){
                if(find(tables.begin(), tables.end(), orders[i+p]) != tables.end()){
                    ++common;
                    temp.emplace_back(-1);
                    continue;
                }
                temp.emplace_back(orders[i+p]);
            }
            tables = temp;
            count+=(n-common);
            p+=n;
        }
        
        if(p < m){
            int common=0;
            vector<int> temp;
            for(int i=0; i < m-p; ++i){
                if(find(tables.begin(), tables.end(), orders[i+p]) != tables.end()){
                    ++common;
                    temp.emplace_back(-1);
                    continue;
                }
                temp.emplace_back(orders[i+p]);
            }
            tables = temp;
            count+=(m-p-common);
            p+=n;
        }
        
        cout << count << "\n";
    }

    return 0;
}