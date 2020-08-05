#include<bits/stdc++.h>

using namespace std;

int compute(int arr[], int n){
    vector<int> l(n, 1), r(n, 1);

    for(int i=1; i<n; ++i){
        for(int j=0; j<i; ++j){
            if(arr[j] < arr[i]) l[i] = max(l[i], l[j]+1);
        }
    }

    for(int i=n-2; i>=0; --i){
        for(int j=n-1; j>i; --j){
            if(arr[j] < arr[i]) r[i] = max(r[i], r[j]+1);
        }
    }
    
    int max = -1;
    for(int i=0; i<n; ++i){
        if(l[i]+r[i]-1 > max){
            max = l[i]+r[i]-1;
        }
    }

    return max;
}

int main(){
    int t;
    cin >> t;
    while(t--){
        int n;
        cin >> n;
        int arr[n];
        for(int i=0; i<n; ++i) cin >> arr[i];
        
        cout << compute(arr, n) << "\n";
    }

    return 0;
}