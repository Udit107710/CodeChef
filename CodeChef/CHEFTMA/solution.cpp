#include <bits/stdc++.h>

using namespace std;

int main(){
    int testcase;
    cin >> testcase;

    while(testcase--){
        long long int n, k, m;
        cin >> n >> k >> m;

        vector<long long int> task(n);
        vector<long long int> completed(n);
        multiset<long long int> white;
        multiset<long long int>::iterator itr;

        for (long long int &x : task) cin >> x;
        for (long long int &x : completed) cin >> x;
        long long int y;
        for(int i=0;i<k+m;i++){  
            cin>>y;
            white.insert(y);
        }

        long long int diff = 0;
        
        for (long long int i = 0; i < n; ++i){
            long long int d = task[i] - completed[i];
            if(white.empty() || *white.begin() > d)
				diff += d;
            else{
		        itr = white.upper_bound(d);
				itr--; 

				diff += d - *itr;
                white.erase(itr);
            }
        }
        cout << diff << endl;
    }
    return 0;
}