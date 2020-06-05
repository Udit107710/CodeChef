#include <bits/stdc++.h>

using namespace std;

int main(){
    int t;
    cin >> t;
    while(t--){
        int n;
        cin >> n;

        if(n&1){
            long x=1;
            for(int i=0; i < n; ++i){
                for(int j=0; j < n; ++j, x++){
                    cout << x << " ";
                }
                cout << "\n";
            }
        }
        else{
            long x=1;
            bool flip=false;
            for(int i=0; i<n; ++i){
                if(flip){
                    x = x + n; ++x;
                    for(int j=0; j < n; ++j){
                        x--;
                        cout << x << " ";
                    }
                    cout << "\n";
                    x+=n;
                }
                else{
                    --x;
                    for(int j=0; j < n; ++j){
                        x++;
                        cout << x << " ";
                    }
                    cout << "\n";
                }
                flip= !flip;
            }
        }
        
    }

    return 0;
}