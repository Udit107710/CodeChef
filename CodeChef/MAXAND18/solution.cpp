#include<bits/stdc++.h>

using namespace std;

void calculate(int n, int hmap[]){
    for(int i=0; i<32; ++i){
        if(n & 1<<i){
            hmap[i]++;
        }
    }
}

int main(){
    int t;
    cin >> t;
    while(t--){
        int n, k;
        cin >> n >> k;
        int arr[n];
        int hmap[32] = {0};
        set<pair<int, int>> sset;
        set<pair<int, int>, greater<pair<int, int>>>::iterator iterset;
        for(int i=0; i<n; ++i){
            cin >> arr[i];
            calculate(arr[i], hmap);
        }

        vector<pair<long long int, int>> result(32, make_pair(0, 0));
        long long int val;
        for(int i=0; i < 32; ++i){
            val = pow(2, i) * hmap[i];
            result.push_back(make_pair(val, i));
        }
        sort(result.begin(), result.end(), [](auto x,auto y){
	        if(x.first==y.first)
	            return x.second<y.second;
	       return x.first>y.first;
	    });
        long long int ans=0;
        
        for(int i=0; i < k; ++i){
            ans+=pow(2, result[i].second);
        }
        cout << ans<< "\n";
      
    }
    return 0;
}