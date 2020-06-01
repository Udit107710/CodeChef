#include <bits/stdc++.h>

using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    cin >> t;

    while(t--){
        long n;
        cin >> n;
        int arr[n];
        for(int i=0; i < n; ++i)
            cin >> arr[i];

        int loc=-1;

        for(int i=n-1; i > 0; --i){
            if(arr[i] > arr[i-1]){
                loc = i-1;
                break;
            }
        }

        if( loc < 0)
            cout << -1 << "\n";
        else{

            int rep = -1;
            for(int i=loc+1; i < n; ++i){
                if(arr[i] > arr[loc])
                    rep = i;
            }
            int temp = arr[rep];
            arr[rep] = arr[loc];
            arr[loc] = temp;
            
            int result[n];
            int i;
            for(i=0; i <= loc; ++i)
                result[i] = arr[i];
            
            for(int j=n-1; j > loc; ++i, --j)
                result[i] = arr[j];

            for(int i=0; i < n; ++i)
                cout << result[i];
            cout << "\n";  
        }
    }

    return 0;
}