#include<bits/stdc++.h>

using namespace std;


int select_min(int n, int a, int b, int arr[]){

    int left = arr[a];
    if(a+2 < n && a+3 < n) left += select_min(n, a+2, a+3, arr);
    else if(a+2 < n) left += arr[a+2];
    
    int right = arr[b];
    if(b+2 < n && b+3 < n) right += select_min(n, b+2, b+3, arr);
    else if(b+2 < n) right += arr[b+2];
    if(left > right) return left;
    else return right;
}


int main(){
    int t;
    cin >> t;

    while(t--){
        int n;
        cin >> n;
        int arr[n];
        int sum=0;
        for(int i=0; i < n; ++i){
            cin >> arr[i];
            sum+=arr[i];
        }
        if(n == 1) cout << "0\n";
        else cout << sum - select_min(n, 0,1, arr) << "\n";
    }

    return 0;
}