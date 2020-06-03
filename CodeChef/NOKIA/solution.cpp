#include <bits/stdc++.h>

using namespace std;

int min_[31] = {-1};
int max_[31] = {-1};

tuple<int, int> compute(int n){
    if(min_[n] <= 0){

        min_[n] = (n+1) + get<0>(compute(n/2)) + get<0>(compute(n-1-n/2));
        max_[n] = (n+1) + get<1>(compute(n-1));
    }
    return make_tuple(min_[n], max_[n]);
}

int main(){
    min_[1] = 2;
    max_[1] = 2;
    min_[2] = 5;
    max_[2] = 5;
    max_[3] = 9;
    min_[3] = 8;
    int t;
    cin >> t;
    while(t--){
        int n, m;
        cin >> n >> m;
        tuple<int, int> val = compute(n);

        if(get<0>(val) <= m && get<1>(val) >= m)
            cout << "0\n";
        else if(get<1>(val) < m)
            cout << m-get<1>(val) << "\n";
        else
            cout << "-1\n";
    }

    return 0;
}