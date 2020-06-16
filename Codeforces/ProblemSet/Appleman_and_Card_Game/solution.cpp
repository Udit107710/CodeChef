#include <bits/stdc++.h>

using namespace std;

int main(){

    long long n, k;
    cin >> n >> k;
    map<char,  long long> hashMap;
    map<char,  long long>::iterator itr;
    multiset< long long> values;
    multiset< long long>::reverse_iterator ritr;
    for(long long i=0; i < n; ++i){
        char c;
        cin >> c;
        hashMap[c]++;
    }
    if(k == 1){ cout << "1";}
    else{
        for(itr=hashMap.begin(); itr != hashMap.end(); ++itr){
            values.insert(itr->second);
        }
        long long count = 0;
        for(ritr=values.rbegin(); ritr != values.rend() && k > 0; ++ritr){
            if(*ritr >= k){ count += (k*k); break;}
            count += (*ritr * *ritr);
            k-=*ritr;
        }
        cout << count;
    }
    return 0;
}