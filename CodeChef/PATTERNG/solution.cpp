#include<bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin >> n;
    string s;
    cin >> s;
    int q;
    cin >> q;

    while(q--){
        int l; char c;
        cin >> l >> c;
        
        if(s.length() == 1) cout << l << "\n";
        else if(l == 1 && c == s[0]) cout << "1\n";
        else if(l == 1) cout << "0\n";
        else{
            int end = l*(l+1)/2;
            end--;
            int start = end - l;
            start++;
            start = start%s.length();
            int count = 0;
            if( l > n){
                for(int i=0; i < l; ++i){
                    if(c == s[start])
                        count++;
                    ++start;
                    start%=s.length();
                }
            }
            else{
                for(int i=0; i < s.length(); ++i){
                    if(s[i] == c) count++;
                }
                count *= (l/s.length());    
                int left = l%s.length();
                for(int i=0; i < left; ++i){
                    if(c == s[start]) ++count;
                    ++start;
                    start%=s.length();
                }
            }
            cout << count << "\n";
        }
        
    }

    return 0;
}