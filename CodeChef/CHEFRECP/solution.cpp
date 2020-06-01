#include <bits/stdc++.h>

using namespace std;

int main(){
    int t;
    cin >> t;
    while(t--){
        long int n;
        cin >> n;
        vector<int> array(n);
        vector<int>::iterator itr;
        vector<bool> appeared(1000, false);
        vector<int> count_array(1000, 0);
        for(int &x: array) cin >> x;
        itr=array.begin();
        appeared[*itr] = true;
        ++count_array[*itr];
        ++itr;
        bool flag = false;
        for(; itr != array.end(); ++itr){
            if(*itr != *prev(itr) && appeared[*itr]){
                flag = true;
                break;
            }
            appeared[*itr] = true;
            ++count_array[*itr];
        }
        sort(count_array.begin(), count_array.end());
        itr=count_array.begin();
        ++itr;
        for (; itr != count_array.end(); ++itr)
            if(*itr == *prev(itr) && *itr != 0){
                flag = true;
                break;
            }
        if(flag)
            cout << "NO" << endl;
        else
            cout << "YES" << endl;
    }
    return 0;
}