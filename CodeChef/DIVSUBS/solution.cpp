 #include <bits/stdc++.h>

using namespace std;

 int main(){
     int t;
     cin >> t;
     while(t--){
        int n;
        cin >> n;
        int x, flag=0, start, end, check[n+1] = {0}, temp=0;
        check[0] = 1;
        for(int i=1; i <= n; ++i){
            cin >> x;
            temp = (temp+x) % n;
            if(check[temp]){
                end = i; start = check[temp];
            }
            check[temp] = i+1;
        }
        cout << end-start+1 << endl;
        while(start<end) cout << start++ << " ";
        cout << end << endl;
    }
    return 0;
 }