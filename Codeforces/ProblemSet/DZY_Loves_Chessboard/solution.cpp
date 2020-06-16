#include <bits/stdc++.h>
using namespace std;

int main(){
    int n,m;
    cin >> n >> m;

    char word[2] = {'W', 'B'};
    char ans[n][m], r;
    char x;
    for(int i=0; i < n; ++i){
        for(int j=0; j < m; ++j){
           cin >> x;
           r = (i+j)%2;
           if(x == '.') ans[i][j] = word[r];
           else ans[i][j] = '-';
        }
    }
    for(int i=0; i<n; ++i){
        for(int j=0; j<m; ++j){
            cout << ans[i][j];
        }
        cout << "\n";
    }
            
    return 0;
}