#include <bits/stdc++.h>

using namespace std;

int main(){
    int t;
    cin >> t;
    while(t--){
        int n;
        cin >> n;

        vector<int> arr(2*n);
        for(int &x: arr) cin >> x;
        
        vector<stack<int>> mmap(2);
        
        for(int i=0; i < 2*n; ++i) {
            mmap[arr[i]%2].push(i+1);
        }
        int p = mmap[1].size(),q = mmap[0].size();

        if(p%2 == 0 && q%2 == 0){ 
            if(q) { mmap[0].pop(); mmap[0].pop(); q-=2;} 
            else { mmap[1].pop(); mmap[1].pop(); p-=2; }
            }
        if(p%2 == 1 && q%2 == 1){ mmap[0].pop(); mmap[1].pop(); --p; --q;}
        
        for(int i=0; i+1 < p; i+=2){
            cout << mmap[1].top() << " ";
            mmap[1].pop();
            cout << mmap[1].top() << "\n";
            mmap[1].pop();
        }
        for(int i=0; i+1 < q; i+=2){
            cout << mmap[0].top() << " ";
            mmap[0].pop();
            cout << mmap[0].top() << "\n";
            mmap[0].pop();
        }
        
        if(mmap[0].size()) cout << mmap[0].top() << " " << mmap[1].top() << "\n";
    }

    return 0;
}