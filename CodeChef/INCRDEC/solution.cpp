#include<bits/stdc++.h>

using namespace std;

int main(){
    int t;
    cin >> t;
    while(t--){
        int n;
        cin >> n;
        int arr[n], result[n+2] = {-1};
        for(int i=0; i < n; ++i) cin >> arr[i];
        int flag =0;
        sort(arr, arr+n);
        int start = 0; int end=n+1;
        for(int i=0; i < n && start < end; ++i){
            if(result[start] != arr[i]){
                result[++start] = arr[i];
            }
            else if(result[end] != arr[i]){
                result[--end] = arr[i];
            }
            else{
                flag = 1;
                break;
            }
        }
        if(result[start] <= result[start+1]){ cout << "NO\n"; continue;}
        if(flag){ cout << "NO\n"; continue;}
        else{
            cout << "YES\n";
            for(int i=1; i <= n; ++i) cout << result[i] << " ";
            cout << "\n";
        }
    }
    return 0;
}