#include <bits/stdc++.h>

using namespace std;

int main(){
    int n;
    cin >> n;
    int x=0, y=0, z=0, a, b, c;
    while(n--){
        cin >> a >> b >> c;
        x+=a;
        y+=b;
        z+=c;
    }
    if(x == y && y == z && x == 0) cout << "YES\n";
    else cout << "NO\n";

    return 0;
}