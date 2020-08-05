#include<bits/stdc++.h>

using namespace std;

int compute(string s){
    int a=0, b=0, c=0;

    for(int i=0; i < s.size(); ++i){
        if(s[i] == 'a') a = 1 + 2*a;
        else if(s[i] == 'b') b = 2*b + a;
        else c = 2*c + b;
    }
    return c;
}

int main(){
    int t;
    cin >> t;
    while(t--){
        string s;
        cin >> s;
        cout << compute(s) << "\n";
    }

    return 0;
}