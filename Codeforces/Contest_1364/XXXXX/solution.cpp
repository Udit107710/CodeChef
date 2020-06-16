#include <bits/stdc++.h>

using namespace std;

int main(){
    int t;
    cin >> t;
    while(t--){
        int n, x;
        cin >> n >> x;
        vector<int> arr(n);
        vector<int> multiples;
        int addition=0;
        for(int i=0; i < n; ++i){ 
            cin >> arr[i];
            if(arr[i]%x == 0) multiples.push_back(i);
            else addition+=arr[i]; 
        } 
        if(x == 1) { cout << "-1\n"; continue; }
        if(multiples.size() == n){ cout << "-1\n"; continue; }
        if(addition%x == 0){ if(n-1 > 0) cout << n - 1 << "\n"; else cout << "-1\n"; }
        else cout << n << "\n";
    }

    return 0;
}