#include <bits/stdc++.h>

using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    cin>>t;
    while(t--){
        string s;

        cin >> s;
        map<char, pair<int, int>> mCount;
        map<char, pair<int, int>>::iterator itr;
        if(s.size()&1){
            int m = s.size()/2;
            int i = 0;
            while(i < s.size()){
                if(i < m)
                    ++mCount[s[i]].first;
                else if(i > m)
                    ++mCount[s[i]].second;
                ++i;
            }
            int flag = 0;
            for(itr=mCount.begin(); itr != mCount.end(); ++itr){
                if(itr->second.first != itr->second.second){
                    flag = 1;
                    break;
                }
            }
            if(flag)
                cout << "NO\n";
            else
                cout << "YES\n";
        }
        else{
            int m = s.size()/2;
            int i = 0;
            while(i < s.size()){
                if(i < m)
                    ++mCount[s[i]].first;
                else
                    ++mCount[s[i]].second;
                ++i;
            }
            int flag = 0;

            for(itr=mCount.begin(); itr != mCount.end(); ++itr){
                if(itr->second.first != itr->second.second){
                    flag = 1;
                    break;
                }
            }
            if(flag)
                cout << "NO\n";
            else
                cout << "YES\n";
        }
        
    }
    return 0;
}