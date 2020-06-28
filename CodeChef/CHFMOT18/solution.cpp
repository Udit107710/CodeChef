#include<bits/stdc++.h>

using namespace std;

int main(){

    int t;
    cin >> t;
    while(t--){
        int s, n;
        cin >> s >> n;
        if( s == 1){ cout << "1\n"; continue; }
        if(s%2){
            if(n > s){ cout << "2\n"; continue; }
            else{
                int c = 0;
                c+=(s/n);
                s%=n;
                if(s == 1) c++;
                else c+=2;
                cout << c << "\n"; continue;
            }
        }
        else{
            if(n > s){
                cout << "1\n"; continue;
            }
            else{
                int c = 0;
                c+=(s/n);
                s%=n;
                if(s) c++;
                cout << c << "\n"; continue;
            }
        }
    }

    return 0;
}