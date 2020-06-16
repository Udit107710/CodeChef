#include <bits/stdc++.h>

using namespace std;

int main(){
    int n, m, d, flag=1, prev, same = 1;
    cin >> n >> m >> d;
    int p = n*m;
    vector<int> arr(p);
    vector<int>::iterator itr;
    for(int i=0; i < p; ++i){ 
        cin >> arr[i];
        if(i == 0) prev = arr[i];
        else{
            if(prev != arr[i]) same = 0;
        }
    }
    if(d == 0 && !same) cout << "-1\n";
    else if(same) cout << "0\n";
    else{
        sort(arr.begin(), arr.end());
        m = p/2;
        int count=0;
        for(itr = arr.begin(); itr != arr.end(); ++itr){
            if(abs(*itr - arr[m])%d){ flag=0; break;}
            else count+=(abs(*itr - arr[m]));
        }
        if(flag) cout << count/d;
        else{
            m+=1;
            for(itr = arr.begin(); itr != arr.end(); ++itr){
                if(abs(*itr - arr[m])%d){ flag=0; break;}
                else count+=(abs(*itr - arr[m]));
            }
            if(flag) cout << count/d;
            else cout << "-1";
        }
    }

    return 0;
}