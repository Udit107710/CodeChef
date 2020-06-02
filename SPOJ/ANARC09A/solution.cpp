#include <bits/stdc++.h>

using namespace std;

map<string, int> dp;

int compute(string str){
    if(dp.find(str) != dp.end())
        return dp[str];
    int n = str.size();
    dp[str] = compute(str.substr(0, 2)) + compute(str.substr(2, n-2));
    return dp[str]; 
}


int main(){
    dp.insert(pair<string, int>("}}", 1));
    dp.insert(pair<string, int>("{{", 1));
    dp.insert(pair<string, int>("{}", 0));
    dp.insert(pair<string, int>("}{", 2));
    string s;
    int p=0;
    cin >> s;
    while (s.find("-") == string::npos){
        ++p;
        stack<char> st;
        string result = "";
        for(int i=0; i < s.size(); ++i){
            if(st.size() > 0 && s[i] == '}'){
                result.pop_back();
                st.pop();
            }
            else if(s[i] == '{'){
                st.push('{');
                result += '{';
            }
            else
            {
                result += '}';
            }
            
        }
        int cost = 0;
        if(result.size() > 0)
            cost = compute(result);
        cout << p << ". " << cost << "\n";
        cin >> s;
    }
    

    return 0;
}