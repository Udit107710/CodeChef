#include<bits/stdc++.h>

using namespace std;

int main(){
    int t;
    cin >> t;
    while(t--){
        int n;
        cin >> n;
        vector<int> arr(n);
        for(int &x: arr) cin >> x;
        sort(arr.begin(), arr.end());

        int count= 0;
        for(int i =n-3; i >= 0; i-=3){
            count += (arr[i]);
        }
        cout << count << "\n";
    }

    return 0;
}