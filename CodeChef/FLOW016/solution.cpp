#include <bits/stdc++.h>

using namespace std;

long int gcd(long int a, long int b){
    while (b) {
        a %= b;
        swap(a, b);
    }
    return a;
}

int main(){
    int t;
    long int a, b;
    cin >> t;
    while(t--){
        cin >> a >> b;
        long g = gcd(a, b);
        long l = (a*b)/g;
        
        cout << g << " " << l << endl;
    }

    return 0;
}