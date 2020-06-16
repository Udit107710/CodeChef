#include <bits/stdc++.h>

using namespace std;

int main(){
    vector<vector<int>> arr(5, vector<int>(5, 0));
    int step=0, x;
    for(int i=0; i < 5; ++i)
        for(int j=0; j < 5; ++j){
            cin >> x;
            if(x==1){
                arr[i][j] = 1;
                step+=(abs(2-i));
                step+=(abs(2-j));
            }
        }
    cout << step;
    return 0;
}